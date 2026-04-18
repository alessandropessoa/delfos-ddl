# 🛡️ DELFOS v2: Analisador, Anonimizador e Validador Científico de DDL

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LGPD Compliance](https://img.shields.io/badge/Compliance-LGPD-green.svg)](#)
[![Methodology: DSR](https://img.shields.io/badge/Methodology-DSR-orange.svg)](#)

O **DELFOS v2** é uma ferramenta avançada de engenharia de dados projetada para permitir a análise de arquiteturas de bancos de dados legados por Large Language Models (LLMs) sem comprometer a segurança ou violar a LGPD. Através de um pipeline de anonimização estrutural, o DELFOS transforma DDLs complexos em representações matemáticas isomórficas (hashes), garantindo que a inteligência da topologia permaneça intacta enquanto os dados sensíveis são protegidos.

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