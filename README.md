Aqui está a versão revisada do `README.md`, agora incluindo a referência ao arquivo de interpretação do relatório de validação completa e pequenos ajustes para alinhamento com o playbook estendido e a flag `--full-validation`.

---

```markdown
# 🛡️ DELFOS: Analisador, Anonimizador e Validador Científico de DDL

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LGPD Compliance](https://img.shields.io/badge/Compliance-LGPD-green.svg)](#)
[![Methodology: DSR](https://img.shields.io/badge/Methodology-DSR-orange.svg)](#)

O **DELFOS** é uma ferramenta avançada de engenharia de dados projetada para permitir a análise de arquiteturas de bancos de dados legados por Large Language Models (LLMs) sem comprometer a segurança ou violar a LGPD. Através de um pipeline de anonimização estrutural, o DELFOS transforma DDLs complexos em representações matemáticas isomórficas (hashes), garantindo que a inteligência da topologia permaneça intacta enquanto os dados sensíveis são protegidos.

---

## 🎯 Objetivo do Projeto

Garantir a reprodutibilidade e conformidade no uso de IA para arquitetura de software, permitindo:
1. **Anonimização Radical:** Substituição de identificadores por hashes preservando a lógica relacional.
2. **Validação Científica:** Testes estatísticos (Pearson) para provar que o modelo mascarado é funcionalmente idêntico ao original.
3. **Análise Segura via LLM:** Uso de prompts estratégicos sobre o DDL ofuscado com tradução reversa de insights.

---

## 🏗️ Fluxo de Trabalho (Pipeline)

```mermaid
graph LR
    A[DDL Original] --> B[delfos.py pipeline]
    B --> C[Artefatos Mascarados]
    C --> D[evaluate.py --all]
    D --> E{Validação Multi-experimento}
    E --> F[Proveniência Científica]
    F --> G[Prompt LLM Seguro]
    G --> H[delfos.py unmask]
    H --> I[Insights de Negócio Reais]
```

---

## 🚀 Como Executar

### 1. Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/analisador-delfos.git
cd analisador-delfos

# Instale as dependências
pip install -r requirements.txt
pip install sqlglot scipy numpy pyyaml
```

### 2. Executando a Anonimização
O comando abaixo gera o DDL mascarado e o "Cofre de Reversão" (Mapping):
```bash
python delfos.py pipeline seu_schema.sql --output-dir ./output-experimento --mode hash
```

### 3. Validação de Isomorfismo e Efetividade

#### Validação Rápida (um único experimento)
```bash
python evaluate.py --dir ./output-experimento
```

#### Validação Completa (todos os critérios de uma só vez) 🆕
Execute uma bateria completa de testes e obtenha um relatório consolidado em Markdown com veredito final:
```bash
python evaluate.py --dir ./output-experimento --full-validation
```
O relatório será salvo como `full_validation_report_YYYYMMDD_HHMMSS.md` dentro do diretório do experimento.

#### Execução em Lote (múltiplos experimentos)
```bash
python evaluate.py --all
```

> 💡 **Dica:** Para entender como interpretar o relatório gerado pelo `--full-validation`, consulte o arquivo de exemplo:  
> [`output-exp-adservice/interpretacao-do-relatorio-full-validation-ll.md`](https://github.com/alessandropessoa/delfos-ddl/blob/main/output-exp-adservice/interpretacao-do-relatorio-full-validation-ll.md)  
> Ele explica, passo a passo, o significado de cada métrica e as ações corretivas recomendadas.

---

## 🧪 Validação Científica (Módulo Evaluate)

O DELFOS utiliza o **Score de Relevância Estática (SRE)** para quantificar a importância de cada tabela na topologia. O avaliador suporta cinco tipos de experimento, definidos no arquivo `evaluate/config.yaml`:

| Tipo de Experimento | Objetivo | Métrica Principal |
|:--- |:--- |:--- |
| **Isomorfismo** | Preservação da topologia relacional | Correlação de Pearson ($r > 0.95$) |
| **Masking Efficacy** | Efetividade da ofuscação | Ganho de Entropia e Taxa de Substituição |
| **Cardinalidade** | Integridade da contagem de objetos | Comparação exata de entidades |
| **Performance** | Overhead computacional | Tempo de parsing e uso de memória |
| **Re-identification Risk** | Risco de reversão/ataque | k-anonymity score |

Para detalhes completos sobre cada experimento, pesos ajustáveis e interpretação de resultados, consulte o **Playbook de Execução Completo** (fornecido separadamente).

---

## 🤖 Integração com LLMs (Engenharia de Prompt)

Após a validação, utilize o arquivo `01_masked.sql` para extrair insights arquiteturais. 

**Exemplo de Prompt:**
> *"Atue como um Arquiteto de Dados. Analise o seguinte schema DDL ofuscado. Identifique os 5 principais hotspots baseando-se na densidade de relacionamentos e chaves estrangeiras."*

Para traduzir os nomes mascarados da resposta de volta para o original:
```bash
python delfos.py unmask resposta_llm.md ./output/02_mapping.json --output analise_real.md
```

---

## 📂 Estrutura de Artefatos Gerados

- `01_masked.sql`: DDL pronto para envio ao LLM.
- `02_mapping.json`: Chave privada para desmascaramento (NUNCA compartilhe).
- `03_structure_masked.json`: Metadados da topologia ofuscada.
- `05_structure_original.json`: Metadados da topologia original (ground truth).
- `full_validation_report_*.md`: Relatório consolidado de validação (quando usando `--full-validation`).
- `provenance_*.md` / `provenance_*.json`: Relatórios de proveniência para auditoria científica.

---

## ⚖️ Metodologia e Conformidade

Este projeto segue os princípios da **Design Science Research (DSR)**, focando na criação de artefatos que resolvem problemas práticos (segurança de dados) com rigor acadêmico. 

- **LGPD:** Garante que metadados que possam identificar processos de negócio sejam removidos.
- **Isomorfismo:** Mantém a assinatura geométrica do grafo de tabelas.

---

## 📚 Documentação Adicional

- [Playbook de Execução Completo (PDF/Markdown)](./docs/playbook.md) – Guia detalhado com todas as fases do pipeline e configurações avançadas.
- [Interpretação de Relatório Full-Validation (exemplo)](./output-exp-adservice/interpretacao-do-relatorio-full-validation-ll.md) – Explicação prática de como analisar os resultados da validação completa.

---

**Versão do README:** 2.1  
**Última Atualização:** Abril de 2026
```

