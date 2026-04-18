# 🔬 Relatório de Validação Completa – DELFOS

**Diretório analisado:** `output-exp-adservice`  
**Data/Hora:** 2026-04-18 13:50:32  
**Versão do Avaliador:** 2.0.0  

---

## 📊 Sumário Executivo

| Experimento              | Resultado | Métricas Principais |
|--------------------------|-----------|---------------------|
| **Isomorfismo**          | ✅ PASSOU | r = 1.0000, p = 0.00e+00 |
| **Eficácia da Máscara**  | ❌ FALHOU | Subst. = 100.0%, Entropia = -0.07 bits |
| **Cardinalidade**        | ✅ PASSOU | Todas idênticas |
| **Desempenho**           | ✅ PASSOU | Tempo = 64.7 ms, Memória = 1.1 MB |
| **Risco de Reidentif.**  | ✅ PASSOU | k mínimo = 96 (limiar 5) |

**Veredito Final:** ⚠️ **REPROVADO (parcial ou total)**

---

## 🔍 Detalhamento por Experimento

### 1. Isomorfismo Topológico (`isomorphism`)

- **Correlação de Pearson:** 1.0000  
- **p‑valor:** 0.00e+00  
- **Tabelas avaliadas:** 96  
- **Critério:** r > 0.95 **E** p < 0.05  
- **Status:** ✅ **PASSOU**  

### 2. Eficácia da Máscara (`masking_efficacy`)

- **Taxa de substituição:** 100.00%  
- **Ganho de entropia:** -0.07 bits  
- **Razão de unicidade (original):** 0.30  
- **Razão de unicidade (mascarado):** 0.30  
- **Critério:** Substituição = 100% **E** ganho > 0.0  
- **Status:** ❌ **FALHOU**  

### 3. Integridade de Cardinalidade (`cardinality`)

| Objeto      | Original | Mascarado | Status |
|-------------|----------|-----------|--------|
| tables      |       96 |        96 | ✅      |
| columns     |      964 |       964 | ✅      |
| primary_keys |       96 |        96 | ✅      |
| foreign_keys |       77 |        77 | ✅      |
| indexes     |        0 |         0 | ✅      |
| views       |        0 |         0 | ✅      |

- **Critério:** Todas as linhas com ✅  
- **Status:** ✅ **PASSOU**  

### 4. Desempenho (`performance`)
- **Tempo médio de parsing:** 64.7 ms (desvio: 14.5 ms)  
- **Pico de memória:** 1.1 MB  
- **Critério:** Tempo < 1000 ms **E** memória < 100 MB  
- **Status:** ✅ **PASSOU**  

### 5. Risco de Reidentificação (`reidentification_risk`)

| Quasi‑identificador     | k mínimo | Limiar | Status      |
|-------------------------|----------|--------|-------------|
| table_name_length       |       96 |      5 | ✅ OK        |
| column_name_length      |      964 |      5 | ✅ OK        |
| prefix_pattern          |      101 |      5 | ✅ OK        |

- **Critério:** k ≥ 5 para todos os QIs  
- **Status:** ✅ **PASSOU**  

---

## 📌 Recomendações

⚠️ Foram detectadas não conformidades. Recomenda-se:

- **Eficácia:** Aumentar comprimento do hash (`--length 12`) ou usar `--mode scoped` para maior entropia.

---

**Arquivos de proveniência detalhada disponíveis em:**  
`output-exp-adservice/provenance_*.json`  
`output-exp-adservice/provenance_*.md`