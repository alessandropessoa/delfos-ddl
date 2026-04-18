import json
import numpy as np
from scipy.stats import pearsonr

class DelfosEvaluator:
    def __init__(self, weights: dict):
        # Se os pesos vierem vazios do YAML, assume um default de segurança
        self.weights = weights if weights else {"pk": 2.0, "fk": 1.5, "idx": 1.0, "joins": 3.0}

    def load_json(self, filepath: str) -> dict:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def calculate_sre(self, structure_data: dict) -> dict:
        scores = {}
        tables = structure_data.get("tables", {})
        indexes = structure_data.get("indexes", [])
        fks = structure_data.get("foreign_keys", [])
        
        join_stats = structure_data.get("join_statistics")
        table_joins = join_stats.get("table_join_frequency", {}) if join_stats else {}

        for tbl_name, tbl_info in tables.items():
            score = 0.0
            if tbl_info.get("primary_key"):
                score += len(tbl_info["primary_key"]["columns"]) * float(self.weights.get("pk", 0))
            
            tbl_fks = [fk for fk in fks if fk["from_table"] == tbl_name or fk["to_table"] == tbl_name]
            score += len(tbl_fks) * float(self.weights.get("fk", 0))
            
            tbl_idxs = [idx for idx in indexes if idx["table"] == tbl_name]
            score += len(tbl_idxs) * float(self.weights.get("idx", 0))
            
            joins_freq = table_joins.get(tbl_name, 0)
            score += joins_freq * float(self.weights.get("joins", 0))
            
            scores[tbl_name] = score
        return scores

    def evaluate(self, orig_path, mask_path, map_path):
        orig_struct = self.load_json(orig_path)
        mask_struct = self.load_json(mask_path)
        mapping     = self.load_json(map_path)
        
        orig_scores = self.calculate_sre(orig_struct)
        mask_scores = self.calculate_sre(mask_struct)
        
        # CORREÇÃO: normaliza os dois lados para uppercase
        mask_scores_upper = {k.upper(): v for k, v in mask_scores.items()}
        tbl_mapping = {k: v.upper() for k, v in mapping.get("tables", {}).items()}
        
        vec_orig, vec_mask, results_table = [], [], []
        
        for orig_name, orig_score in orig_scores.items():
            mask_name  = tbl_mapping.get(orig_name)
            mask_score = mask_scores_upper.get(mask_name, 0.0)
            
            vec_orig.append(orig_score)
            vec_mask.append(mask_score)
            results_table.append((orig_name, orig_score, mask_score))
            
        # Proteção contra arrays constantes (Scipy ConstantInputWarning)
        std_orig = np.std(vec_orig) if len(vec_orig) > 0 else 0
        std_mask = np.std(vec_mask) if len(vec_mask) > 0 else 0
        
        if len(vec_orig) < 2 or std_orig == 0 or std_mask == 0:
            # Se não houver variação nos dados (ex: todas as tabelas tiraram zero)
            correlation, p_value = 0.0, 1.0
        else:
            correlation, p_value = pearsonr(vec_orig, vec_mask)
        
        return correlation, p_value, results_table, len(orig_scores)

    def generate_storytelling(self, correlation: float, p_value: float, num_tables: int) -> str:
        story = [
            "\n" + "="*80,
            " 📖 DATA STORYTELLING: INTERPRETAÇÃO DOS RESULTADOS",
            "="*80 + "\n",
            "📍 O QUE OS NÚMEROS DIZEM:"
        ]
        
        if correlation == 0.0 and p_value == 1.0:
             story.append(f"⚠️ Atenção: O teste analisou {num_tables} tabelas, mas todas obtiveram a mesma pontuação (SRE Constante). Isso geralmente significa que o schema é muito pequeno, não possui Chaves Estrangeiras/Índices suficientes para gerar variação, ou os pesos estão zerados.")
             story.append("\n🎯 IMPACTO (LLMs e LGPD):")
             story.append("A topologia é simples demais para validar a quebra de isomorfismo estatisticamente. Recomendamos rodar em um DDL mais complexo.")
        elif correlation > 0.95 and p_value < 0.05:
            story.append(f"O teste analisou {num_tables} tabelas e encontrou uma correlação de Pearson quase perfeita (r = {correlation:.4f}). O valor-p de {p_value:.2e} indica significância estatística. A topologia do banco de dados permaneceu intacta após o mascaramento.")
            story.append("\n🎯 IMPACTO (LLMs e LGPD):")
            story.append("✅ Viabilidade Comprovada: A 'assinatura geométrica' foi preservada. Você pode injetar o DDL mascarado em LLMs com total segurança LGPD. O LLM tomará decisões matemáticas baseadas nas exatas mesmas tabelas 'hotspots' do banco real.")
        else:
            story.append(f"O teste em {num_tables} tabelas retornou uma correlação (r = {correlation:.4f}). A ofuscação alterou a estrutura fundamental do esquema, quebrando dependências cruciais.")
            story.append("\n🎯 IMPACTO (LLMs e LGPD):")
            story.append("❌ Risco Arquitetural: Enviar este DDL para um LLM resultará em alucinações. O mascarador precisa ser ajustado.")
        
        return "\n".join(story)