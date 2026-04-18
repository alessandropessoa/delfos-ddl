#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from typing import List, Tuple
import yaml

from evaluate.evaluator import DelfosEvaluator
from evaluate.provenance import ProvenanceTracker


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
    
    # Se houver múltiplos, pega o primeiro (deveria haver apenas um de cada)
    return orig_candidates[0], mask_candidates[0], map_candidates[0]


def run_evaluation(orig_file: Path, mask_file: Path, map_file: Path, weights: dict, 
                   auto_generate: bool = True) -> dict:
    """Executa a avaliação para um conjunto de artefatos e retorna métricas."""
    print(f"\n📂 Processando: {orig_file.parent.name}")
    print(f"   Original : {orig_file.name}")
    print(f"   Mascarado: {mask_file.name}")
    print(f"   Mapeamento: {map_file.name}")
    
    evaluator = DelfosEvaluator(weights)
    correlation, p_value, results_table, num_tables = evaluator.evaluate(orig_file, mask_file, map_file)
    
    # Exibe tabela resumida (opcional, mas útil)
    print("\n   " + "="*50)
    print(f"   {'Tabela':<25} | {'SRE Orig':>8} | {'SRE Mask':>8}")
    print("   " + "-"*50)
    for orig_name, orig_score, mask_score in results_table[:5]:  # mostra só as 5 primeiras
        print(f"   {orig_name:<25} | {orig_score:>8.1f} | {mask_score:>8.1f}")
    if len(results_table) > 5:
        print(f"   ... e mais {len(results_table)-5} tabelas.")
    
    # Storytelling
    story = evaluator.generate_storytelling(correlation, p_value, num_tables)
    print("\n   " + story.replace('\n', '\n   '))
    
    # Proveniência (salva dentro do diretório do experimento)
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


def main():
    parser = argparse.ArgumentParser(
        description="DELFOS Evaluator - Validação Científica de Isomorfismo e SRE",
        epilog="Exemplos:\n"
               "  python evaluate.py --dir ./output-exp-oracle\n"
               "  python evaluate.py --all\n"
               "  python evaluate.py --auto        # modo antigo (primeiro encontrado)"
    )
    parser.add_argument('--config', default='evaluate/config.yaml', help='YAML de configuração')
    
    # Grupo mutuamente exclusivo para seleção de diretório(s)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--dir', type=str, help='Processa apenas o diretório especificado')
    group.add_argument('--all', action='store_true', help='Processa todos os diretórios output-exp*')
    
    # Argumentos legados (ainda funcionam se --dir/--all não forem usados)
    parser.add_argument('--orig', help='Caminho explícito para JSON original')
    parser.add_argument('--mask', help='Caminho explícito para JSON mascarado')
    parser.add_argument('--map', help='Caminho explícito para JSON de mapeamento')
    parser.add_argument('--auto', action='store_true', help='(modo legado) Busca global automática')
    
    args = parser.parse_args()

    # 1. Carregar configuração
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"❌ Arquivo de configuração não encontrado: {config_path}")
        sys.exit(1)
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    weights = config.get('sre_weights', {})

    # 2. Decidir modo de operação
    if args.dir:
        # Modo diretório único
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
        # Modo todos os experimentos
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
        # Modo legado: argumentos explícitos ou busca global
        from evaluate import get_first_match, find_file_interactive  # import local para evitar quebra
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