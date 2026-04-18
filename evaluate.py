#!/usr/bin/env python3
"""
DELFOS Evaluator - Validação Científica Multi-Experimento

Suporta:
  --dir <diretório>   : executa um único experimento conforme config.yaml
  --all               : executa um único experimento em todos os diretórios output-exp*
  --full-validation   : executa TODOS os experimentos para um diretório e gera relatório consolidado
"""
import argparse
import json
import sys
import time
import math
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

import numpy as np
import yaml
from scipy.stats import pearsonr

# Adiciona diretório pai ao path para imports relativos
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from evaluate.evaluator import DelfosEvaluator
from evaluate.provenance import ProvenanceTracker

# -----------------------------------------------------------------------------
# Constantes e critérios de validação
# -----------------------------------------------------------------------------
EXPERIMENT_TYPES = ["isomorphism", "masking_efficacy", "cardinality", "performance", "reidentification_risk"]

CRITERIA = {
    "isomorphism": {
        "correlation_min": 0.95,
        "p_value_max": 0.05
    },
    "masking_efficacy": {
        "substitution_rate_min": 1.0,      # 100%
        "entropy_gain_min": 0.0
    },
    "cardinality": {
        "tolerance": 0                      # todas as contagens devem ser idênticas
    },
    "performance": {
        "max_parsing_time_ms": 1000,        # 1 segundo
        "max_memory_mb": 100                # 100 MB
    },
    "reidentification_risk": {
        "k_anonymity_min": 5
    }
}

# -----------------------------------------------------------------------------
# Funções auxiliares para localização de artefatos
# -----------------------------------------------------------------------------
def find_experiment_dirs(base_dir: Path = Path('.'), pattern: str = "output-exp*") -> List[Path]:
    """Retorna todos os diretórios que casam com o padrão e contêm os três artefatos."""
    candidates = [d for d in base_dir.glob(pattern) if d.is_dir()]
    valid_dirs = []
    for d in candidates:
        if (list(d.glob("*original.json")) and 
            list(d.glob("*masked.json")) and 
            list(d.glob("*mapping.json"))):
            valid_dirs.append(d)
    return valid_dirs


def find_artifacts_in_dir(directory: Path) -> Tuple[Path, Path, Path]:
    """Localiza os três arquivos obrigatórios dentro de um diretório específico."""
    orig_candidates = list(directory.glob("*original.json"))
    mask_candidates = list(directory.glob("*masked.json"))
    map_candidates  = list(directory.glob("*mapping.json"))
    
    if not (orig_candidates and mask_candidates and map_candidates):
        raise FileNotFoundError(f"Diretório {directory} não contém todos os artefatos necessários.")
    
    return orig_candidates[0], mask_candidates[0], map_candidates[0]


# -----------------------------------------------------------------------------
# Funções de avaliação para cada tipo de experimento
# -----------------------------------------------------------------------------
def evaluate_isomorphism(orig_file: Path, mask_file: Path, map_file: Path, 
                         weights: Dict[str, float]) -> Dict[str, Any]:
    """Avalia preservação topológica via SRE."""
    evaluator = DelfosEvaluator(weights)
    correlation, p_value, results_table, num_tables = evaluator.evaluate(orig_file, mask_file, map_file)
    
    passed = (correlation > CRITERIA["isomorphism"]["correlation_min"] and 
              p_value < CRITERIA["isomorphism"]["p_value_max"])
    
    return {
        "correlation": correlation,
        "p_value": p_value,
        "num_tables": num_tables,
        "results_table": results_table,
        "passed": passed
    }


def evaluate_masking_efficacy(orig_file: Path, mask_file: Path) -> Dict[str, Any]:
    """Mede taxa de substituição e ganho de entropia."""
    with open(orig_file, 'r', encoding='utf-8') as f:
        orig_data = json.load(f)
    with open(mask_file, 'r', encoding='utf-8') as f:
        mask_data = json.load(f)
    
    # Coleta todos os nomes de tabelas e colunas originais e mascarados
    def collect_names(data: dict) -> List[str]:
        names = []
        for table_name, table_info in data.get("tables", {}).items():
            names.append(table_name)
            for col in table_info.get("columns", []):
                names.append(col.get("name", ""))
            if table_info.get("primary_key"):
                names.append(table_info["primary_key"].get("name", ""))
        for idx in data.get("indexes", []):
            names.append(idx.get("name", ""))
        for fk in data.get("foreign_keys", []):
            names.append(fk.get("constraint_name", ""))
        return [n for n in names if n]
    
    orig_names = collect_names(orig_data)
    mask_names = collect_names(mask_data)
    
    # Taxa de substituição: quantos nomes originais foram de fato trocados?
    # Consideramos que se o nome mascarado é diferente do original, foi substituído.
    # Como não temos mapeamento 1:1 garantido, comparamos comprimento e padrão.
    substitution_count = 0
    for orig, mask in zip(orig_names, mask_names):
        if orig != mask and not mask.startswith(orig):  # heurística simples
            substitution_count += 1
    substitution_rate = substitution_count / len(orig_names) if orig_names else 0.0
    
    # Entropia dos nomes mascarados
    def shannon_entropy(strings: List[str]) -> float:
        if not strings:
            return 0.0
        joined = "".join(strings)
        freq = Counter(joined)
        length = len(joined)
        probs = [f/length for f in freq.values()]
        return -sum(p * math.log2(p) for p in probs)
    
    entropy_orig = shannon_entropy(orig_names)
    entropy_mask = shannon_entropy(mask_names)
    entropy_gain = entropy_mask - entropy_orig
    
    # Unicidade
    unique_orig = len(set(orig_names)) / len(orig_names) if orig_names else 0.0
    unique_mask = len(set(mask_names)) / len(mask_names) if mask_names else 0.0
    
    passed = (substitution_rate >= CRITERIA["masking_efficacy"]["substitution_rate_min"] and
              entropy_gain > CRITERIA["masking_efficacy"]["entropy_gain_min"])
    
    return {
        "substitution_rate": substitution_rate,
        "entropy_gain": entropy_gain,
        "unique_ratio_orig": unique_orig,
        "unique_ratio_mask": unique_mask,
        "passed": passed
    }


def evaluate_cardinality(orig_file: Path, mask_file: Path) -> Dict[str, Any]:
    """Compara contagens de objetos."""
    with open(orig_file, 'r', encoding='utf-8') as f:
        orig_data = json.load(f)
    with open(mask_file, 'r', encoding='utf-8') as f:
        mask_data = json.load(f)
    
    def count_objects(data: dict) -> Dict[str, int]:
        return {
            "tables": len(data.get("tables", {})),
            "columns": sum(len(tbl.get("columns", [])) for tbl in data.get("tables", {}).values()),
            "primary_keys": sum(1 for tbl in data.get("tables", {}).values() if tbl.get("primary_key")),
            "foreign_keys": len(data.get("foreign_keys", [])),
            "indexes": len(data.get("indexes", [])),
            "views": len(data.get("views", []))
        }
    
    orig_counts = count_objects(orig_data)
    mask_counts = count_objects(mask_data)
    
    comparison = {}
    all_match = True
    for key in orig_counts.keys():
        match = orig_counts[key] == mask_counts[key]
        comparison[key] = {"original": orig_counts[key], "masked": mask_counts[key], "match": match}
        if not match:
            all_match = False
    
    passed = all_match
    
    return {
        "comparison": comparison,
        "passed": passed
    }


def evaluate_performance(orig_file: Path, iterations: int = 10, warmup: bool = True) -> Dict[str, Any]:
    """Mede tempo de parsing e uso de memória do DDL original."""
    import timeit
    import tracemalloc
    
    # Encontrar o arquivo DDL original .sql correspondente
    ddl_file = orig_file.parent / "01_original.sql"  # convenção do pipeline
    if not ddl_file.exists():
        # tenta achar qualquer .sql no diretório
        sql_files = list(orig_file.parent.glob("*.sql"))
        if sql_files:
            ddl_file = sql_files[0]
        else:
            return {
                "parsing_time_ms": None,
                "memory_usage_mb": None,
                "passed": False,
                "error": "Arquivo SQL original não encontrado para medição de performance."
            }
    
    # Função de parsing (simulada - na prática usaria o parser real do DELFOS)
    def parse_ddl():
        from core import DDLReportEmitter, AnalyzerConfig, ReportStyle
        cfg = AnalyzerConfig(style=ReportStyle.TERMINAL, emit_json=False)
        emitter = DDLReportEmitter()
        ddl_text = ddl_file.read_text(encoding='utf-8')
        emitter.emit(ddl_text, cfg)
    
    # Warmup
    if warmup:
        parse_ddl()
    
    # Medição de tempo
    timer = timeit.Timer(parse_ddl)
    times = timer.repeat(repeat=iterations, number=1)
    avg_time_ms = np.mean(times) * 1000
    std_time_ms = np.std(times) * 1000
    
    # Medição de memória
    tracemalloc.start()
    parse_ddl()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    peak_mb = peak / (1024 * 1024)
    
    passed = (avg_time_ms < CRITERIA["performance"]["max_parsing_time_ms"] and
              peak_mb < CRITERIA["performance"]["max_memory_mb"])
    
    return {
        "parsing_time_ms": avg_time_ms,
        "parsing_time_std_ms": std_time_ms,
        "memory_usage_mb": peak_mb,
        "passed": passed
    }


def evaluate_reidentification_risk(mask_file: Path, map_file: Path) -> Dict[str, Any]:
    """Estima risco de reidentificação via k-anonymity em quasi-identificadores."""
    with open(mask_file, 'r', encoding='utf-8') as f:
        mask_data = json.load(f)
    with open(map_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    # Coleta nomes mascarados e seus comprimentos
    mask_names = []
    for table_name, table_info in mask_data.get("tables", {}).items():
        mask_names.append(("table", table_name))
        for col in table_info.get("columns", []):
            mask_names.append(("column", col.get("name", "")))
    
    # Quasi-identificadores
    qi_values = {
        "table_name_length": [],
        "column_name_length": [],
        "prefix_pattern": []
    }
    
    for obj_type, name in mask_names:
        if obj_type == "table":
            qi_values["table_name_length"].append(len(name))
        else:
            qi_values["column_name_length"].append(len(name))
        # prefixo comum (primeiras 2 letras)
        qi_values["prefix_pattern"].append(name[:2] if len(name) >= 2 else name)
    
    # Calcula k-anonymity para cada QI
    k_values = {}
    for qi, values in qi_values.items():
        if values:
            freq = Counter(values)
            k_values[qi] = min(freq.values())
        else:
            k_values[qi] = 0
    
    min_k = min(k_values.values()) if k_values else 0
    threshold = CRITERIA["reidentification_risk"]["k_anonymity_min"]
    passed = all(v >= threshold for v in k_values.values())
    
    return {
        "k_values": k_values,
        "min_k": min_k,
        "threshold": threshold,
        "passed": passed
    }


# -----------------------------------------------------------------------------
# Validação completa (--full-validation)
# -----------------------------------------------------------------------------
def run_full_validation(directory: Path, config: dict) -> Dict[str, Any]:
    """Executa todos os experimentos para um diretório."""
    orig_file, mask_file, map_file = find_artifacts_in_dir(directory)
    weights = config.get("sre_weights", {})
    
    results = {}
    print(f"\n🔬 Executando validação completa em: {directory.name}")
    
    # 1. Isomorphism
    print("   → Isomorfismo...")
    results["isomorphism"] = evaluate_isomorphism(orig_file, mask_file, map_file, weights)
    
    # 2. Masking Efficacy
    print("   → Eficácia da máscara...")
    results["masking_efficacy"] = evaluate_masking_efficacy(orig_file, mask_file)
    
    # 3. Cardinality
    print("   → Cardinalidade...")
    results["cardinality"] = evaluate_cardinality(orig_file, mask_file)
    
    # 4. Performance
    print("   → Desempenho...")
    perf_cfg = config.get("performance", {})
    iterations = perf_cfg.get("iterations", 10)
    warmup = perf_cfg.get("warmup", True)
    results["performance"] = evaluate_performance(orig_file, iterations, warmup)
    
    # 5. Reidentification Risk
    print("   → Risco de reidentificação...")
    results["reidentification_risk"] = evaluate_reidentification_risk(mask_file, map_file)
    
    return results


def generate_markdown_report(results: Dict[str, Any], directory: Path) -> Path:
    """Gera relatório consolidado em Markdown."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = directory / f"full_validation_report_{timestamp}.md"
    
    all_passed = all(exp["passed"] for exp in results.values())
    verdict = "✅ **APROVADO**" if all_passed else "⚠️ **REPROVADO (parcial ou total)**"
    
    lines = [
        f"# 🔬 Relatório de Validação Completa – DELFOS",
        "",
        f"**Diretório analisado:** `{directory.name}`  ",
        f"**Data/Hora:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ",
        f"**Versão do Avaliador:** 2.0.0  ",
        "",
        "---",
        "",
        "## 📊 Sumário Executivo",
        "",
        "| Experimento              | Resultado | Métricas Principais |",
        "|--------------------------|-----------|---------------------|",
    ]
    
    # Preenche sumário
    iso = results["isomorphism"]
    lines.append(f"| **Isomorfismo**          | {'✅ PASSOU' if iso['passed'] else '❌ FALHOU'} | r = {iso['correlation']:.4f}, p = {iso['p_value']:.2e} |")
    
    mask = results["masking_efficacy"]
    lines.append(f"| **Eficácia da Máscara**  | {'✅ PASSOU' if mask['passed'] else '❌ FALHOU'} | Subst. = {mask['substitution_rate']*100:.1f}%, Entropia = {mask['entropy_gain']:+.2f} bits |")
    
    card = results["cardinality"]
    lines.append(f"| **Cardinalidade**        | {'✅ PASSOU' if card['passed'] else '❌ FALHOU'} | {'Todas idênticas' if card['passed'] else 'Discrepâncias encontradas'} |")
    
    perf = results["performance"]
    if perf.get("error"):
        lines.append(f"| **Desempenho**           | ⚠️ N/A | {perf['error']} |")
    else:
        lines.append(f"| **Desempenho**           | {'✅ PASSOU' if perf['passed'] else '❌ FALHOU'} | Tempo = {perf['parsing_time_ms']:.1f} ms, Memória = {perf['memory_usage_mb']:.1f} MB |")
    
    risk = results["reidentification_risk"]
    lines.append(f"| **Risco de Reidentif.**  | {'✅ PASSOU' if risk['passed'] else '⚠️ FALHOU'} | k mínimo = {risk['min_k']} (limiar {risk['threshold']}) |")
    
    lines.extend([
        "",
        f"**Veredito Final:** {verdict}",
        "",
        "---",
        "",
        "## 🔍 Detalhamento por Experimento",
        "",
        "### 1. Isomorfismo Topológico (`isomorphism`)",
        "",
        f"- **Correlação de Pearson:** {iso['correlation']:.4f}  ",
        f"- **p‑valor:** {iso['p_value']:.2e}  ",
        f"- **Tabelas avaliadas:** {iso['num_tables']}  ",
        f"- **Critério:** r > {CRITERIA['isomorphism']['correlation_min']} **E** p < {CRITERIA['isomorphism']['p_value_max']}  ",
        f"- **Status:** {'✅ **PASSOU**' if iso['passed'] else '❌ **FALHOU**'}  ",
        "",
        "### 2. Eficácia da Máscara (`masking_efficacy`)",
        "",
        f"- **Taxa de substituição:** {mask['substitution_rate']*100:.2f}%  ",
        f"- **Ganho de entropia:** {mask['entropy_gain']:+.2f} bits  ",
        f"- **Razão de unicidade (original):** {mask['unique_ratio_orig']:.2f}  ",
        f"- **Razão de unicidade (mascarado):** {mask['unique_ratio_mask']:.2f}  ",
        f"- **Critério:** Substituição = {CRITERIA['masking_efficacy']['substitution_rate_min']*100:.0f}% **E** ganho > {CRITERIA['masking_efficacy']['entropy_gain_min']}  ",
        f"- **Status:** {'✅ **PASSOU**' if mask['passed'] else '❌ **FALHOU**'}  ",
        "",
        "### 3. Integridade de Cardinalidade (`cardinality`)",
        "",
        "| Objeto      | Original | Mascarado | Status |",
        "|-------------|----------|-----------|--------|",
    ])
    
    for obj, comp in card["comparison"].items():
        status = "✅" if comp["match"] else "❌"
        lines.append(f"| {obj:<11} | {comp['original']:>8} | {comp['masked']:>9} | {status:<6} |")
    
    lines.extend([
        "",
        f"- **Critério:** Todas as linhas com ✅  ",
        f"- **Status:** {'✅ **PASSOU**' if card['passed'] else '❌ **FALHOU**'}  ",
        "",
        "### 4. Desempenho (`performance`)",
    ])
    
    if perf.get("error"):
        lines.append(f"\n⚠️ {perf['error']}\n")
    else:
        lines.extend([
            f"- **Tempo médio de parsing:** {perf['parsing_time_ms']:.1f} ms (desvio: {perf['parsing_time_std_ms']:.1f} ms)  ",
            f"- **Pico de memória:** {perf['memory_usage_mb']:.1f} MB  ",
            f"- **Critério:** Tempo < {CRITERIA['performance']['max_parsing_time_ms']} ms **E** memória < {CRITERIA['performance']['max_memory_mb']} MB  ",
            f"- **Status:** {'✅ **PASSOU**' if perf['passed'] else '❌ **FALHOU**'}  ",
        ])
    
    lines.extend([
        "",
        "### 5. Risco de Reidentificação (`reidentification_risk`)",
        "",
        "| Quasi‑identificador     | k mínimo | Limiar | Status      |",
        "|-------------------------|----------|--------|-------------|",
    ])
    
    for qi, k in risk["k_values"].items():
        status = "✅ OK" if k >= risk["threshold"] else "❌ Abaixo"
        lines.append(f"| {qi:<23} | {k:>8} | {risk['threshold']:>6} | {status:<11} |")
    
    lines.extend([
        "",
        f"- **Critério:** k ≥ {risk['threshold']} para todos os QIs  ",
        f"- **Status:** {'✅ **PASSOU**' if risk['passed'] else '⚠️ **FALHOU**'}  ",
        "",
        "---",
        "",
        "## 📌 Recomendações",
    ])
    
    if all_passed:
        lines.append("\n✅ Todos os critérios foram atendidos. O artefato mascarado está **validado para uso seguro** com LLMs e terceiros.\n")
    else:
        lines.append("\n⚠️ Foram detectadas não conformidades. Recomenda-se:\n")
        if not iso["passed"]:
            lines.append("- **Isomorfismo:** Ajustar pesos do SRE no `config.yaml` conforme paradigma do banco (OLTP, OLAP, etc.) ou usar `--mode scoped`.")
        if not mask["passed"]:
            lines.append("- **Eficácia:** Aumentar comprimento do hash (`--length 12`) ou usar `--mode scoped` para maior entropia.")
        if not card["passed"]:
            lines.append("- **Cardinalidade:** Revisar parser SQL para dialetos específicos (views, sinônimos, etc.).")
        if not perf["passed"] and not perf.get("error"):
            lines.append("- **Desempenho:** Otimizar estruturas de dados ou paralelismo no pipeline.")
        if not risk["passed"]:
            lines.append("- **Risco de reidentificação:** Usar `--mode scoped` ou aumentar `--length` para homogeneizar tamanhos.")
    
    lines.extend([
        "",
        "---",
        "",
        f"**Arquivos de proveniência detalhada disponíveis em:**  ",
        f"`{directory}/provenance_*.json`  ",
        f"`{directory}/provenance_*.md`",
    ])
    
    # Grava arquivo
    report_content = "\n".join(lines)
    report_path.write_text(report_content, encoding='utf-8')
    
    return report_path


# -----------------------------------------------------------------------------
# Execução padrão (single experiment)
# -----------------------------------------------------------------------------
def run_evaluation(orig_file: Path, mask_file: Path, map_file: Path, weights: dict, 
                   auto_generate: bool = True) -> dict:
    """Executa a avaliação para um conjunto de artefatos e retorna métricas."""
    print(f"\n📂 Processando: {orig_file.parent.name}")
    print(f"   Original : {orig_file.name}")
    print(f"   Mascarado: {mask_file.name}")
    print(f"   Mapeamento: {map_file.name}")
    
    evaluator = DelfosEvaluator(weights)
    correlation, p_value, results_table, num_tables = evaluator.evaluate(orig_file, mask_file, map_file)
    
    # Exibe tabela resumida
    print("\n   " + "="*50)
    print(f"   {'Tabela':<25} | {'SRE Orig':>8} | {'SRE Mask':>8}")
    print("   " + "-"*50)
    for orig_name, orig_score, mask_score in results_table[:5]:
        print(f"   {orig_name:<25} | {orig_score:>8.1f} | {mask_score:>8.1f}")
    if len(results_table) > 5:
        print(f"   ... e mais {len(results_table)-5} tabelas.")
    
    # Storytelling
    story = evaluator.generate_storytelling(correlation, p_value, num_tables)
    print("\n   " + story.replace('\n', '\n   '))
    
    # Proveniência
    tracker = ProvenanceTracker(output_dir=orig_file.parent)
    json_prov, md_prov = tracker.record(orig_file, mask_file, map_file, correlation, p_value, weights)
    print(f"\n   📄 Proveniência salva em:\n      {json_prov}\n      {md_prov}")
    
    return {
        "dir": orig_file.parent.name,
        "correlation": correlation,
        "p_value": p_value,
        "num_tables": num_tables,
        "isomorphism": correlation > 0.95 and p_value < 0.05
    }


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="DELFOS Evaluator - Validação Científica de Isomorfismo e SRE",
        epilog="Exemplos:\n"
               "  python evaluate.py --dir ./output-exp-oracle\n"
               "  python evaluate.py --all\n"
               "  python evaluate.py --dir ./output-exp-oracle --full-validation\n"
               "  python evaluate.py --auto        # modo antigo (primeiro encontrado)"
    )
    parser.add_argument('--config', default='evaluate/config.yaml', help='YAML de configuração')
    
    # Grupo mutuamente exclusivo para seleção de diretório(s)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--dir', type=str, help='Processa apenas o diretório especificado')
    group.add_argument('--all', action='store_true', help='Processa todos os diretórios output-exp*')
    
    # Argumentos legados
    parser.add_argument('--orig', help='Caminho explícito para JSON original')
    parser.add_argument('--mask', help='Caminho explícito para JSON mascarado')
    parser.add_argument('--map', help='Caminho explícito para JSON de mapeamento')
    parser.add_argument('--auto', action='store_true', help='(modo legado) Busca global automática')
    
    # Nova flag para validação completa
    parser.add_argument('--full-validation', action='store_true', 
                        help='Executa TODOS os experimentos e gera relatório consolidado em Markdown')
    
    args = parser.parse_args()

    # 1. Carregar configuração
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"❌ Arquivo de configuração não encontrado: {config_path}")
        sys.exit(1)
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    weights = config.get('sre_weights', {})

    # 2. Validação completa (novo fluxo)
    if args.full_validation:
        if not args.dir:
            print("❌ A flag --full-validation requer --dir <diretório>")
            sys.exit(1)
        exp_dir = Path(args.dir)
        if not exp_dir.is_dir():
            print(f"❌ Diretório não encontrado: {exp_dir}")
            sys.exit(1)
        results = run_full_validation(exp_dir, config)
        report_path = generate_markdown_report(results, exp_dir)
        print(f"\n✅ Relatório completo salvo em: {report_path}")
        sys.exit(0)

    # 3. Fluxo padrão (um experimento conforme config.yaml)
    if args.dir:
        exp_dir = Path(args.dir)
        if not exp_dir.is_dir():
            print(f"❌ Diretório não encontrado: {exp_dir}")
            sys.exit(1)
        try:
            orig_file, mask_file, map_file = find_artifacts_in_dir(exp_dir)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            sys.exit(1)
        run_evaluation(orig_file, mask_file, map_file, weights)
        
    elif args.all:
        exp_dirs = find_experiment_dirs()
        if not exp_dirs:
            print("❌ Nenhum diretório output-exp* com artefatos completos encontrado.")
            sys.exit(1)
        
        print(f"🔍 Encontrados {len(exp_dirs)} experimentos.")
        results_summary = []
        for exp_dir in sorted(exp_dirs):
            try:
                orig, mask, mapf = find_artifacts_in_dir(exp_dir)
                res = run_evaluation(orig, mask, mapf, weights)
                results_summary.append(res)
            except Exception as e:
                print(f"⚠️ Erro ao processar {exp_dir}: {e}")
                continue
        
        # Resumo final
        print("\n" + "="*80)
        print("📊 RESUMO CONSOLIDADO DOS EXPERIMENTOS")
        print("="*80)
        print(f"{'Experimento':<20} | {'r Pearson':>10} | {'p-valor':>12} | {'Isomorfismo':>12} | {'Tabelas':>8}")
        print("-"*80)
        for res in results_summary:
            iso = "✅ SIM" if res['isomorphism'] else "❌ NÃO"
            print(f"{res['dir']:<20} | {res['correlation']:>10.4f} | {res['p_value']:>12.2e} | {iso:>12} | {res['num_tables']:>8}")
        print("="*80)
        
    else:
        # Modo legado
        from evaluate import get_first_match, find_file_interactive
        print("\n🔎 Modo legado: busca global de artefatos...")
        if args.auto:
            orig_file = Path(args.orig) if args.orig else get_first_match('*original.json')
            mask_file = Path(args.mask) if args.mask else get_first_match('*masked.json')
            map_file  = Path(args.map) if args.map else get_first_match('*mapping.json')
        else:
            orig_file = Path(args.orig) if args.orig else find_file_interactive("ORIGINAL?", "*original.json")
            mask_file = Path(args.mask) if args.mask else find_file_interactive("MASCARADO?", "*masked.json")
            map_file  = Path(args.map) if args.map else find_file_interactive("MAPEAMENTO?", "*mapping.json")
        
        run_evaluation(orig_file, mask_file, map_file, weights)


if __name__ == "__main__":
    main()