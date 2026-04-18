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

#### `MEDICAO_FISICA`

- **PK:** `ID_MEDICAO` (`PK_MEDICAO`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID_OBRA` | `INT` | NO |  |  |  |
| `ANO_REFERENCIA` | `INT` | NO |  | 🔍 |  |
| `MES_REFERENCIA` | `INT` | NO |  | 🔍 |  |
| `VALOR_EXECUTADO` | `NUMERIC(15,2)` | NO |  |  |  |
| `DATA_APROVACAO` | `TIMESTAMP` | YES |  |  |  |

#### `EMPRESA`

- **PK:** `ID_EMPRESA` (`PK_EMPRESA`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `CNPJ` | `VARCHAR(14)` | NO |  |  |  |
| `RAZAO_SOCIAL` | `VARCHAR(100)` | NO |  |  |  |
| `DATA_CADASTRO` | `TIMESTAMP` | YES |  |  |  |

#### `OBRA`

- **PK:** `ID_OBRA` (`PK_OBRA`)

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
| `IDX_MEDICAO_TEMPO` | `ANO_REFERENCIA`, `MES_REFERENCIA` |  |

#### `OBRA`

| Nome do Índice | Colunas | Único? |
|----------------|---------|--------|
| `IDX_OBRA_STATUS` | `STATUS` |  |

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `MEDICAO_FISICA` | `PK_MEDICAO` | `ID_MEDICAO` |
| `EMPRESA` | `PK_EMPRESA` | `ID_EMPRESA` |
| `OBRA` | `PK_OBRA` | `ID_OBRA` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `MEDICAO_FISICA` | `ID_OBRA` | `OBRA` | `ID_OBRA` | `FK_MEDICAO_OBRA` |
| `OBRA` | `ID_EMPRESA` | `EMPRESA` | `ID_EMPRESA` | `FK_OBRA_EMPRESA` |
