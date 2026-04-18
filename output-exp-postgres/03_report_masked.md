> ⚠️ **DISCLAIMER — ANÁLISE ESTÁTICA DE DDL**
> 
> Esta análise é puramente ESTRUTURAL, baseada no DDL (schema estático).
> Sem acesso ao banco populado, NÃO é possível inferir:
> 
> 1. **Consistência das regras de negócio**
> 2. **Normalização real das colunas**
> 3. **Candidatos reais a índice B‑tree**
> 
> ➜ Use estatísticas reais do banco para validação.

## 📊 SUMÁRIO GERAL

| Métrica | Valor |
|---------|-------|
| Tabelas físicas | 3 |
| Materialized Views | 0 |
| Views | 0 |
| Índices explícitos | 2 |
| Chaves primárias | 3 |
| Chaves estrangeiras (FK) | 2 |
| Comentários de tabela | 0 |
| Comentários de coluna | 0 |
| Arestas de join (SQL) | 0 |

## 🗃️ TABELAS — DETALHAMENTO DE COLUNAS

### 📌 Tabelas (3)

#### `T_7EE4E828`

- **PK:** `ID_MEDICAO` (`K_a05e7e3d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_CF4A6E1B` | `INT` | NO |  |  |  |
| `C_74507A61` | `INT` | NO |  | 🔍 |  |
| `C_3E546EDB` | `INT` | NO |  | 🔍 |  |
| `C_F02308D1` | `NUMERIC(15,2)` | NO |  |  |  |
| `C_3129D9AD` | `TIMESTAMP` | YES |  |  |  |

#### `T_A75D07F8`

- **PK:** `C_835190E8` (`K_e5a6eda7`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_9D10D4E4` | `VARCHAR(14)` | NO |  |  |  |
| `C_291B360B` | `VARCHAR(100)` | NO |  |  |  |
| `C_6D1312E8` | `TIMESTAMP` | YES |  |  |  |

#### `T_E2098DBF`

- **PK:** `C_CF4A6E1B` (`K_060c120c`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_835190E8` | `INT` | NO |  |  |  |
| `C_4F8B69BF` | `VARCHAR(150)` | NO |  |  |  |
| `C_3C1A4C64` | `NUMERIC(15,2)` | YES |  |  |  |
| `C_8C2E4A03` | `VARCHAR(20)` | YES |  | 🔍 |  |

## 📇 ÍNDICES EXPLÍCITOS

#### `T_7EE4E828`

| Nome do Índice | Colunas | Único? |
|----------------|---------|--------|
| `I_f40c92fe` | `C_74507A61`, `C_3E546EDB` |  |

#### `T_E2098DBF`

| Nome do Índice | Colunas | Único? |
|----------------|---------|--------|
| `I_ea0675ce` | `C_8C2E4A03` |  |

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `T_7EE4E828` | `K_a05e7e3d` | `ID_MEDICAO` |
| `T_A75D07F8` | `K_e5a6eda7` | `C_835190E8` |
| `T_E2098DBF` | `K_060c120c` | `C_CF4A6E1B` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `T_7EE4E828` | `C_CF4A6E1B` | `T_E2098DBF` | `C_CF4A6E1B` | `K_013e5099` |
| `T_E2098DBF` | `C_835190E8` | `T_A75D07F8` | `C_835190E8` | `K_604f6592` |
