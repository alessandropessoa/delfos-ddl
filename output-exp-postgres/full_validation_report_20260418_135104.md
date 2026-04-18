# 🔬 Relatório de Validação Completa – DELFOS

**Diretório analisado:** `output-exp-postgres`  
**Data/Hora:** 2026-04-18 13:51:04  
**Versão do Avaliador:** 2.0.0  

---

## 📊 Sumário Executivo

| Experimento              | Resultado | Métricas Principais |
|--------------------------|-----------|---------------------|
| **Isomorfismo**          | ✅ PASSOU | r = 1.0000, p = 0.00e+00 |
| **Eficácia da Máscara**  | ❌ FALHOU | Subst. = 100.0%, Entropia = -0.20 bits |
| **Cardinalidade**        | ✅ PASSOU | Todas idênticas |
| **Desempenho**           | ✅ PASSOU | Tempo = 1.6 ms, Memória = 0.0 MB |
| **Risco de Reidentif.**  | ⚠️ FALHOU | k mínimo = 3 (limiar 5) |

**Veredito Final:** ⚠️ **REPROVADO (parcial ou total)**

---

## 🔍 Detalhamento por Experimento

### 1. Isomorfismo Topológico (`isomorphism`)

- **Correlação de Pearson:** 1.0000  
- **p‑valor:** 0.00e+00  
- **Tabelas avaliadas:** 3  
- **Critério:** r > 0.95 **E** p < 0.05  
- **Status:** ✅ **PASSOU**  

### 2. Eficácia da Máscara (`masking_efficacy`)

- **Taxa de substituição:** 100.00%  
- **Ganho de entropia:** -0.20 bits  
- **Razão de unicidade (original):** 1.00  
- **Razão de unicidade (mascarado):** 1.00  
- **Critério:** Substituição = 100% **E** ganho > 0.0  
- **Status:** ❌ **FALHOU**  

### 3. Integridade de Cardinalidade (`cardinality`)

| Objeto      | Original | Mascarado | Status |
|-------------|----------|-----------|--------|
| tables      |        3 |         3 | ✅      |
| columns     |       12 |        12 | ✅      |
| primary_keys |        3 |         3 | ✅      |
| foreign_keys |        2 |         2 | ✅      |
| indexes     |        2 |         2 | ✅      |
| views       |        0 |         0 | ✅      |

- **Critério:** Todas as linhas com ✅  
- **Status:** ✅ **PASSOU**  

### 4. Desempenho (`performance`)
- **Tempo médio de parsing:** 1.6 ms (desvio: 0.9 ms)  
- **Pico de memória:** 0.0 MB  
- **Critério:** Tempo < 1000 ms **E** memória < 100 MB  
- **Status:** ✅ **PASSOU**  

### 5. Risco de Reidentificação (`reidentification_risk`)

| Quasi‑identificador     | k mínimo | Limiar | Status      |
|-------------------------|----------|--------|-------------|
| table_name_length       |        3 |      5 | ❌ Abaixo    |
| column_name_length      |       12 |      5 | ✅ OK        |
| prefix_pattern          |        3 |      5 | ❌ Abaixo    |

- **Critério:** k ≥ 5 para todos os QIs  
- **Status:** ⚠️ **FALHOU**  

---

## 📌 Recomendações

⚠️ Foram detectadas não conformidades. Recomenda-se:

- **Eficácia:** Aumentar comprimento do hash (`--length 12`) ou usar `--mode scoped` para maior entropia.
- **Risco de reidentificação:** Usar `--mode scoped` ou aumentar `--length` para homogeneizar tamanhos.

---

**Arquivos de proveniência detalhada disponíveis em:**  
`output-exp-postgres/provenance_*.json`  
`output-exp-postgres/provenance_*.md`