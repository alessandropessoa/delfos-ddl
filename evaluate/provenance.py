import json
import getpass
import platform
from datetime import datetime
from pathlib import Path

class ProvenanceTracker:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def record(self, orig_file, mask_file, map_file, correlation, p_value, weights):
        timestamp = datetime.now()
        
        data = {
            "experiment_date": timestamp.isoformat(),
            "user": getpass.getuser(),
            "system": {
                "os": platform.system(),
                "node": platform.node(),
                "python_version": platform.python_version()
            },
            "inputs": {
                "original_schema": str(orig_file),
                "masked_schema": str(mask_file),
                "mapping_file": str(map_file)
            },
            "sre_weights": weights,
            "results": {
                "pearson_correlation": round(correlation, 4),
                "p_value": p_value,
                "isomorphism_preserved": bool(correlation > 0.95 and p_value < 0.05)
            }
        }

        # Formatador de tempo para nome do arquivo
        time_str = timestamp.strftime('%Y%m%d_%H%M%S')

        # Salva JSON
        json_path = self.output_dir / f"provenance_{time_str}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        # Salva Markdown
        md_path = self.output_dir / f"provenance_{time_str}.md"
        self._write_markdown(md_path, data)
        
        return json_path, md_path

    def _write_markdown(self, path: Path, data: dict):
        # 1. Extraindo as variáveis antes para evitar problemas de parsing no f-string
        exp_date = data['experiment_date']
        user = data['user']
        node = data['system']['node']
        os_sys = data['system']['os']
        
        orig_schema = data['inputs']['original_schema']
        mask_schema = data['inputs']['masked_schema']
        map_file = data['inputs']['mapping_file']
        
        weights_json = json.dumps(data['sre_weights'], indent=2)
        
        corr = data['results']['pearson_correlation']
        pval = f"{data['results']['p_value']:.4e}"
        
        iso_preserved = "✅ SIM" if data['results']['isomorphism_preserved'] else "❌ NÃO"
        
        # 2. Montando o Markdown de forma linear e segura
        md_content = (
            f"# 🛡️ Relatório de Proveniência do Experimento\n\n"
            f"**Data/Hora:** {exp_date}\n"
            f"**Pesquisador/Usuário:** `{user}`\n"
            f"**Máquina:** `{node}` (OS: {os_sys})\n\n"
            f"## 📂 Artefatos Analisados\n"
            f"* **Original:** `{orig_schema}`\n"
            f"* **Mascarado:** `{mask_schema}`\n"
            f"* **Mapeamento:** `{map_file}`\n\n"
            f"## ⚖️ Pesos Utilizados (SRE)\n"
            f"```json\n{weights_json}\n```\n\n"
            f"## 📈 Resultados da Hipótese\n"
            f"* **Correlação de Pearson (r):** `{corr}`\n"
            f"* **P-Value:** `{pval}`\n"
            f"* **Isomorfismo Preservado:** `{iso_preserved}`\n"
        )
        
        # 3. Escrevendo no arquivo
        path.write_text(md_content, encoding='utf-8')