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

#### `EMPRESA`

- **PK:** `ID_EMPRESA` (`pk_empresa`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `CNPJ` | `VARCHAR(14)` | NO |  |  |  |
| `RAZAO_SOCIAL` | `VARCHAR(100)` | NO |  |  |  |
| `DATA_CADASTRO` | `TIMESTAMP` | YES |  |  |  |

#### `MEDICAO_FISICA`

- **PK:** `ID_MEDICAO` (`pk_medicao`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID_OBRA` | `INT` | NO |  |  |  |
| `ANO_REFERENCIA` | `INT` | NO |  | 🔍 |  |
| `MES_REFERENCIA` | `INT` | NO |  | 🔍 |  |
| `VALOR_EXECUTADO` | `NUMERIC(15,2)` | NO |  |  |  |
| `DATA_APROVACAO` | `TIMESTAMP` | YES |  |  |  |

#### `OBRA`

- **PK:** `ID_OBRA` (`pk_obra`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID_EMPRESA` | `INT` | NO |  |  |  |
| `NOME_OBRA` | `VARCHAR(150)` | NO |  |  |  |
| `ORCAMENTO_TOTAL` | `NUMERIC(15,2)` | YES |  |  |  |
| `STATUS` | `VARCHAR(20)` | YES |  | 🔍 |  |

## 📇 ÍNDICES EXPLÍCITOS

#### `MEDICAO_FISICA`

| Nome do Índice | Colunas | Único? |
|----------------|---------|--------|
| `idx_medicao_tempo` | `ANO_REFERENCIA`, `MES_REFERENCIA` |  |

#### `OBRA`

| Nome do Índice | Colunas | Único? |
|----------------|---------|--------|
| `idx_obra_status` | `STATUS` |  |

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `EMPRESA` | `pk_empresa` | `ID_EMPRESA` |
| `MEDICAO_FISICA` | `pk_medicao` | `ID_MEDICAO` |
| `OBRA` | `pk_obra` | `ID_OBRA` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `MEDICAO_FISICA` | `ID_OBRA` | `OBRA` | `ID_OBRA` | `fk_medicao_obra` |
| `OBRA` | `ID_EMPRESA` | `EMPRESA` | `ID_EMPRESA` | `fk_obra_empresa` |
