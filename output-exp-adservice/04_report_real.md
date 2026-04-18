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
| Tabelas físicas | 96 |
| Materialized Views | 0 |
| Views | 0 |
| Índices explícitos | 0 |
| Chaves primárias | 96 |
| Chaves estrangeiras (FK) | 77 |
| Comentários de tabela | 0 |
| Comentários de coluna | 0 |
| Arestas de join (SQL) | 0 |

## 🗃️ TABELAS — DETALHAMENTO DE COLUNAS

### 📌 Tabelas (96)

#### `KANBAN_MOVIMENTO`

- **PK:** `ID` (`KANBAN_MOVIMENTO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DE_COLUNA` | `varchar(50)` | NO |  |  |  |
| `PARA_COLUNA` | `varchar(50)` | NO |  |  |  |
| `DATA_MOVIMENTO` | `timestamp` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `DJANGO_MIGRATIONS`

- **PK:** `ID` (`DJANGO_MIGRATIONS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `APP` | `varchar(255)` | NO |  |  |  |
| `NAME` | `varchar(255)` | NO |  |  |  |
| `APPLIED` | `timestamp` | NO |  |  |  |

#### `NOTIFICACOES_GRUPOPERMISSAOEVENT`

- **PK:** `PGH_ID` (`NOTIFICACOES_GRUPOPERMISSAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `KANBAN_KANBANOBSERVACAOEVENT`

- **PK:** `PGH_ID` (`KANBAN_KANBANOBSERVACAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TEXTO` | `text` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `USUARIOS_USUARIOEVENT`

- **PK:** `PGH_ID` (`USUARIOS_USUARIOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `PASSWORD` | `varchar(128)` | NO |  |  |  |
| `LAST_LOGIN` | `timestamp` | YES |  |  |  |
| `USERNAME` | `varchar(150)` | NO |  |  |  |
| `FIRST_NAME` | `varchar(150)` | NO |  |  |  |
| `LAST_NAME` | `varchar(150)` | NO |  |  |  |
| `EMAIL` | `varchar(254)` | NO |  |  |  |
| `DATE_JOINED` | `timestamp` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `PESSOA_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `CONTRATOS`

- **PK:** `ID` (`CONTRATOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `VALOR_TOTAL` | `numeric(12, 2)` | NO |  |  |  |
| `DATA_INICIO` | `date` | NO |  |  |  |
| `DATA_FIM` | `date` | NO |  |  |  |
| `DATA_RENOVACAO` | `date` | YES |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `GESTOR_RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `LOCAL_EXECUCAO_ID` | `int` | YES |  |  |  |
| `STATUS_ID` | `int` | NO |  |  |  |

#### `NOTIFICACOES`

- **PK:** `ID` (`NOTIFICACOES_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(200)` | NO |  |  |  |
| `MENSAGEM` | `text` | NO |  |  |  |
| `LINK` | `varchar(200)` | NO |  |  |  |
| `DESTINATARIO_ID` | `int` | NO |  |  |  |

#### `DOCUMENTOS_DOCUMENTOEVENT`

- **PK:** `PGH_ID` (`DOCUMENTOS_DOCUMENTOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_ORIGINAL` | `varchar(255)` | NO |  |  |  |
| `ARQUIVO` | `varchar(100)` | NO |  |  |  |
| `FUNCAO_DOCUMENTO` | `varchar(50)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `DATA_VALIDADE` | `date` | YES |  |  |  |
| `CREATED_BY_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `TIPO_DOCUMENTO_ID` | `int` | NO |  |  |  |

#### `MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT`

- **PK:** `PGH_ID` (`MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `ITEM_TIPO` | `varchar(20)` | NO |  |  |  |
| `ITEM_ID` | `int` | NO |  |  |  |
| `QUANTIDADE` | `numeric(12, 4)` | NO |  |  |  |
| `DATA_MOVIMENTO` | `timestamp` | NO |  |  |  |
| `ORIGEM` | `varchar(255)` | NO |  |  |  |
| `DESTINO` | `varchar(255)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `TIPO_MOVIMENTACAO_ID` | `int` | NO |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |

#### `TIPO_RELATORIO`

- **PK:** `ID` (`TIPO_RELATORIO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `TEMPLATE_HTML` | `text` | NO |  |  |  |

#### `ENDERECOS`

- **PK:** `ID` (`ENDERECOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `LOGRADOURO` | `varchar(255)` | NO |  |  |  |
| `NUMERO` | `varchar(20)` | NO |  |  |  |
| `COMPLEMENTO` | `varchar(100)` | YES |  |  |  |
| `BAIRRO` | `varchar(100)` | NO |  |  |  |
| `CIDADE` | `varchar(100)` | NO |  |  |  |
| `ESTADO` | `varchar(2)` | NO |  |  |  |
| `CEP` | `varchar(10)` | YES |  |  |  |
| `PAIS` | `varchar(50)` | NO |  |  |  |

#### `KANBAN_ATIVIDADE_CONCLUIDA`

- **PK:** `ID` (`KANBAN_ATIVIDADE_CONCLUIDA_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_CONCLUSAO` | `timestamp` | NO |  |  |  |
| `TEMPO_TOTAL_HORAS` | `numeric(8, 2)` | YES |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |

#### `UNIDADE_MEDIDA`

- **PK:** `ID` (`UNIDADE_MEDIDA_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SIGLA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `varchar(200)` | NO |  |  |  |

#### `AUTH_GROUP`

- **PK:** `ID` (`AUTH_GROUP_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `NAME` | `varchar(150)` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_INTERVALSCHEDULE`

- **PK:** `ID` (`DJANGO_CELERY_BEAT_INTERVALSCHEDULE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `EVERY` | `int` | NO |  |  |  |
| `PERIOD` | `varchar(24)` | NO |  |  |  |

#### `PGHISTORY_CONTEXT`

- **PK:** `ID` (`PGHISTORY_CONTEXT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |

#### `DJANGO_ADMIN_LOG`

- **PK:** `ID` (`DJANGO_ADMIN_LOG_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `ACTION_TIME` | `timestamp` | NO |  |  |  |
| `OBJECT_ID` | `text` | YES |  |  |  |
| `OBJECT_REPR` | `varchar(200)` | NO |  |  |  |
| `ACTION_FLAG` | `int` | NO |  |  |  |
| `CHANGE_MESSAGE` | `text` | NO |  |  |  |
| `CONTENT_TYPE_ID` | `int` | YES |  |  |  |
| `USER_ID` | `int` | NO |  |  |  |

#### `USUARIOS`

- **PK:** `ID` (`USUARIOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `PASSWORD` | `varchar(128)` | NO |  |  |  |
| `LAST_LOGIN` | `timestamp` | YES |  |  |  |
| `USERNAME` | `varchar(150)` | NO |  |  |  |
| `FIRST_NAME` | `varchar(150)` | NO |  |  |  |
| `LAST_NAME` | `varchar(150)` | NO |  |  |  |
| `EMAIL` | `varchar(254)` | NO |  |  |  |
| `DATE_JOINED` | `timestamp` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `PESSOA_ID` | `int` | YES |  |  |  |

#### `ESTOQUE_UNIDADEMEDIDAEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_UNIDADEMEDIDAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SIGLA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `varchar(200)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `AVALIACOES_AVALIACAOEVENT`

- **PK:** `PGH_ID` (`AVALIACOES_AVALIACAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_AVALIACAO` | `date` | NO |  |  |  |
| `ENTIDADE_TIPO` | `varchar(20)` | NO |  |  |  |
| `ENTIDADE_ID` | `int` | NO |  |  |  |
| `NOTA_FINAL` | `numeric(5, 2)` | YES |  |  |  |
| `AVALIADOR_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `RATIFICADOR_ID` | `int` | YES |  |  |  |

#### `PERMISSOES`

- **PK:** `ID` (`PERMISSOES_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `RECURSO` | `varchar(100)` | NO |  |  |  |
| `ACAO` | `varchar(50)` | NO |  |  |  |

#### `MATERIAIS`

- **PK:** `ID` (`MATERIAIS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `DATA_VALIDADE` | `date` | YES |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `DJANGO_SESSION`

- **PK:** `SESSION_KEY` (`DJANGO_SESSION_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `SESSION_KEY` | `varchar(40)` | NO | ✅ |  |  |
| `SESSION_DATA` | `text` | NO |  |  |  |
| `EXPIRE_DATE` | `timestamp` | NO |  |  |  |

#### `FERRAMENTAS`

- **PK:** `ID` (`FERRAMENTAS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `NUMERO_SERIE` | `varchar(100)` | YES |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `KANBAN_KANBANCARDEVENT`

- **PK:** `PGH_ID` (`KANBAN_KANBANCARDEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(300)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `COLUNA` | `varchar(50)` | NO |  |  |  |
| `ORDEM` | `int` | NO |  |  |  |
| `DATA_LIMITE` | `date` | YES |  |  |  |
| `DATA_INICIO` | `date` | YES |  |  |  |
| `DATA_CONCLUSAO` | `date` | YES |  |  |  |
| `PRIORIDADE` | `varchar(20)` | NO |  |  |  |
| `ESTIMATIVA_HORAS` | `numeric(6, 2)` | YES |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |
| `CRIADO_POR_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `QUADRO_ID` | `int` | NO |  |  |  |

#### `ROTULOS`

- **PK:** `ID` (`ROTULOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `DJANGO_CONTENT_TYPE`

- **PK:** `ID` (`DJANGO_CONTENT_TYPE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `APP_LABEL` | `varchar(100)` | NO |  |  |  |
| `MODEL` | `varchar(100)` | NO |  |  |  |

#### `ITEM_ROTULO`

- **PK:** `ID` (`ITEM_ROTULO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `ITEM_TIPO` | `varchar(20)` | NO |  |  |  |
| `ITEM_ID` | `int` | NO |  |  |  |
| `ROTULO_ID` | `int` | NO |  |  |  |

#### `TIPO_DOCUMENTO`

- **PK:** `ID` (`TIPO_DOCUMENTO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |

#### `PESSOAS_FUNCIONARIOEVENT`

- **PK:** `PGH_ID` (`PESSOAS_FUNCIONARIOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `MATRICULA` | `varchar(50)` | NO |  |  |  |
| `DATA_ADMISSAO` | `date` | NO |  |  |  |
| `DATA_DEMISSAO` | `date` | YES |  |  |  |
| `TIPO_CONTRATACAO` | `varchar(20)` | NO |  |  |  |
| `CARGA_HORARIA_CONTRATUAL_MENSAL` | `numeric(6, 2)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `PESSOA_ID` | `int` | NO |  |  |  |

#### `EMPRESAS_SOCIOADMINISTRADOREVENT`

- **PK:** `PGH_ID` (`EMPRESAS_SOCIOADMINISTRADOREVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TIPO` | `varchar(20)` | NO |  |  |  |
| `PERCENTUAL` | `numeric(5, 2)` | YES |  |  |  |
| `DATA_INICIO` | `date` | NO |  |  |  |
| `DATA_FIM` | `date` | YES |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `PESSOA_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `EMPRESAS_EMPRESAEVENT`

- **PK:** `PGH_ID` (`EMPRESAS_EMPRESAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_FANTASIA` | `varchar(200)` | NO |  |  |  |
| `RAZAO_SOCIAL` | `varchar(200)` | NO |  |  |  |
| `CNPJ` | `varchar(18)` | NO |  |  |  |
| `EMAIL` | `varchar(255)` | NO |  |  |  |
| `TELEFONE` | `varchar(20)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `ENDERECO_ID` | `int` | YES |  |  |  |

#### `TRANSACAO_CONTRATO`

- **PK:** `ID` (`TRANSACAO_CONTRATO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `VALOR_CUSTO` | `numeric(12, 2)` | NO |  |  |  |
| `VALOR_RECEITA` | `numeric(12, 2)` | NO |  |  |  |
| `VALOR_LUCRO_PREJUIZO` | `numeric(12, 2)` | NO |  |  |  |
| `DATA_TRANSACAO` | `date` | NO |  |  |  |
| `CONTRATO_ID` | `int` | NO |  |  |  |

#### `CONTRATOS_CONTRATOEVENT`

- **PK:** `PGH_ID` (`CONTRATOS_CONTRATOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `VALOR_TOTAL` | `numeric(12, 2)` | NO |  |  |  |
| `DATA_INICIO` | `date` | NO |  |  |  |
| `DATA_FIM` | `date` | NO |  |  |  |
| `DATA_RENOVACAO` | `date` | YES |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `GESTOR_RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `LOCAL_EXECUCAO_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `STATUS_ID` | `int` | NO |  |  |  |

#### `CONTRATOS_FUNCIONARIOMOVIMENTOEVENT`

- **PK:** `PGH_ID` (`CONTRATOS_FUNCIONARIOMOVIMENTOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_MOVIMENTO` | `date` | NO |  |  |  |
| `MOTIVO` | `text` | NO |  |  |  |
| `CREATED_BY_ID` | `int` | YES |  |  |  |
| `DE_CONTRATO_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |
| `PARA_CONTRATO_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `ITEM_AVALIACAO`

- **PK:** `ID` (`ITEM_AVALIACAO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `PESO` | `numeric(5, 2)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_BASE` | `numeric(10, 2)` | YES |  |  |  |

#### `AVALIACOES`

- **PK:** `ID` (`AVALIACOES_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_AVALIACAO` | `date` | NO |  |  |  |
| `ENTIDADE_TIPO` | `varchar(20)` | NO |  |  |  |
| `ENTIDADE_ID` | `int` | NO |  |  |  |
| `NOTA_FINAL` | `numeric(5, 2)` | YES |  |  |  |
| `AVALIADOR_ID` | `int` | NO |  |  |  |
| `RATIFICADOR_ID` | `int` | YES |  |  |  |

#### `ANEXO_RELATORIO`

- **PK:** `ID` (`ANEXO_RELATORIO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `ARQUIVO` | `varchar(100)` | NO |  |  |  |
| `NOME` | `varchar(255)` | NO |  |  |  |
| `DESCRICAO` | `varchar(300)` | NO |  |  |  |
| `TIPO_MIME` | `varchar(50)` | NO |  |  |  |
| `ENVIADO_POR_ID` | `int` | YES |  |  |  |
| `RELATORIO_ID` | `int` | NO |  |  |  |

#### `ESTOQUE_EQUIPAMENTOEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_EQUIPAMENTOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `NUMERO_SERIE` | `varchar(100)` | NO |  |  |  |
| `DATA_AQUISICAO` | `date` | NO |  |  |  |
| `GARANTIA_FIM` | `date` | NO |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `DJANGO_CELERY_RESULTS_GROUPRESULT`

- **PK:** `ID` (`DJANGO_CELERY_RESULTS_GROUPRESULT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `varchar(255)` | NO |  |  |  |
| `DATE_CREATED` | `timestamp` | NO |  |  |  |
| `DATE_DONE` | `timestamp` | NO |  |  |  |
| `CONTENT_TYPE` | `varchar(128)` | NO |  |  |  |
| `CONTENT_ENCODING` | `varchar(64)` | NO |  |  |  |
| `RESULT` | `text` | YES |  |  |  |

#### `PESSOAS_PESSOAEVENT`

- **PK:** `PGH_ID` (`PESSOAS_PESSOAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_COMPLETO` | `varchar(200)` | NO |  |  |  |
| `CPF_CNPJ` | `varchar(18)` | YES |  |  |  |
| `EMAIL` | `varchar(254)` | YES |  |  |  |
| `TELEFONE` | `varchar(20)` | YES |  |  |  |
| `FOTO` | `varchar(100)` | YES |  |  |  |
| `ENDERECO_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `AUTH_PERMISSION`

- **PK:** `ID` (`AUTH_PERMISSION_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `NAME` | `varchar(255)` | NO |  |  |  |
| `CONTENT_TYPE_ID` | `int` | NO |  |  |  |
| `CODENAME` | `varchar(100)` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE`

- **PK:** `ID` (`DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `CLOCKED_TIME` | `timestamp` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_PERIODICTASKS`

- **PK:** `IDENT` (`DJANGO_CELERY_BEAT_PERIODICTASKS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `IDENT` | `int` | NO | ✅ |  |  |
| `LAST_UPDATE` | `timestamp` | NO |  |  |  |

#### `KANBAN_KANBANATIVIDADECONCLUIDAEVENT`

- **PK:** `PGH_ID` (`KANBAN_KANBANATIVIDADECONCLUIDAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_CONCLUSAO` | `timestamp` | NO |  |  |  |
| `TEMPO_TOTAL_HORAS` | `numeric(8, 2)` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |

#### `ESTOQUE_FERRAMENTAEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_FERRAMENTAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `NUMERO_SERIE` | `varchar(100)` | YES |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `FUNCIONARIO_PERMISSAO`

- **PK:** `ID` (`FUNCIONARIO_PERMISSAO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `CONCEDIDO_POR_ID` | `int` | YES |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |
| `PERMISSAO_ID` | `int` | NO |  |  |  |

#### `VEICULOS`

- **PK:** `ID` (`VEICULOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `PLACA` | `varchar(10)` | NO |  |  |  |
| `RENAVAM` | `varchar(20)` | NO |  |  |  |
| `MARCA` | `varchar(50)` | NO |  |  |  |
| `MODELO` | `varchar(50)` | NO |  |  |  |
| `ANO_FABRICACAO` | `int` | NO |  |  |  |
| `DATA_LICENCIAMENTO` | `date` | NO |  |  |  |
| `PROPRIETARIO_TIPO` | `varchar(20)` | NO |  |  |  |
| `PROPRIETARIO_ID` | `int` | NO |  |  |  |
| `VALOR_AQUISICAO` | `numeric(12, 2)` | NO |  |  |  |
| `STATUS_ID` | `int` | NO |  |  |  |

#### `FINANCEIRO_TRANSACAOCONTRATOEVENT`

- **PK:** `PGH_ID` (`FINANCEIRO_TRANSACAOCONTRATOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `VALOR_CUSTO` | `numeric(12, 2)` | NO |  |  |  |
| `VALOR_RECEITA` | `numeric(12, 2)` | NO |  |  |  |
| `VALOR_LUCRO_PREJUIZO` | `numeric(12, 2)` | NO |  |  |  |
| `DATA_TRANSACAO` | `date` | NO |  |  |  |
| `CONTRATO_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `CONTRATOS_FUNCIONARIOCONTRATOEVENT`

- **PK:** `PGH_ID` (`CONTRATOS_FUNCIONARIOCONTRATOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_INICIO_VINCULO` | `date` | NO |  |  |  |
| `DATA_FIM_VINCULO` | `date` | YES |  |  |  |
| `TIPO_ALOCACAO` | `varchar(20)` | NO |  |  |  |
| `HORAS_CONTRATADAS_PERIODO` | `numeric(8, 2)` | NO |  |  |  |
| `HORAS_TRABALHADAS_PERIODO` | `numeric(8, 2)` | NO |  |  |  |
| `CONTRATO_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `KANBAN_OBSERVACAO`

- **PK:** `ID` (`KANBAN_OBSERVACAO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TEXTO` | `text` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `PESSOAS`

- **PK:** `ID` (`PESSOAS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_COMPLETO` | `varchar(200)` | NO |  |  |  |
| `CPF_CNPJ` | `varchar(18)` | YES |  |  |  |
| `EMAIL` | `varchar(254)` | YES |  |  |  |
| `TELEFONE` | `varchar(20)` | YES |  |  |  |
| `FOTO` | `varchar(100)` | YES |  |  |  |
| `ENDERECO_ID` | `int` | YES |  |  |  |

#### `ESTOQUE_CATEGORIAITEMEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_CATEGORIAITEMEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `STATUS`

- **PK:** `ID` (`STATUS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `STATUS` | `varchar(50)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |

#### `DOCUMENTO_ROTULO`

- **PK:** `ID` (`DOCUMENTO_ROTULO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DOCUMENTO_ID` | `int` | NO |  |  |  |
| `ROTULO_ID` | `int` | NO |  |  |  |

#### `DOCUMENTOS_ROTULOEVENT`

- **PK:** `PGH_ID` (`DOCUMENTOS_ROTULOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `AUTH_GROUP_PERMISSIONS`

- **PK:** `ID` (`AUTH_GROUP_PERMISSIONS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `int` | NO |  |  |  |
| `PERMISSION_ID` | `int` | NO |  |  |  |

#### `AVALIACAO_ITEM`

- **PK:** `ID` (`AVALIACAO_ITEM_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `NOTA` | `numeric(5, 2)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `AVALIACAO_ID` | `int` | NO |  |  |  |
| `ITEM_AVALIACAO_ID` | `int` | NO |  |  |  |

#### `CONTRATOS_STATUSEVENT`

- **PK:** `PGH_ID` (`CONTRATOS_STATUSEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `STATUS` | `varchar(50)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `FUNCIONARIO_CONTRATO`

- **PK:** `ID` (`FUNCIONARIO_CONTRATO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_INICIO_VINCULO` | `date` | NO |  |  |  |
| `DATA_FIM_VINCULO` | `date` | YES |  |  |  |
| `TIPO_ALOCACAO` | `varchar(20)` | NO |  |  |  |
| `HORAS_CONTRATADAS_PERIODO` | `numeric(8, 2)` | NO |  |  |  |
| `HORAS_TRABALHADAS_PERIODO` | `numeric(8, 2)` | NO |  |  |  |
| `CONTRATO_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |

#### `AVALIACOES_ITEMAVALIACAOEVENT`

- **PK:** `PGH_ID` (`AVALIACOES_ITEMAVALIACAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `PESO` | `numeric(5, 2)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_BASE` | `numeric(10, 2)` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_SOLARSCHEDULE`

- **PK:** `ID` (`DJANGO_CELERY_BEAT_SOLARSCHEDULE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `EVENT` | `varchar(24)` | NO |  |  |  |
| `LATITUDE` | `numeric(9, 6)` | NO |  |  |  |
| `LONGITUDE` | `numeric(9, 6)` | NO |  |  |  |

#### `GRUPO_PERMISSOES`

- **PK:** `ID` (`GRUPO_PERMISSOES_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |

#### `DOCUMENTOS`

- **PK:** `ID` (`DOCUMENTOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_ORIGINAL` | `varchar(255)` | NO |  |  |  |
| `ARQUIVO` | `varchar(100)` | NO |  |  |  |
| `FUNCAO_DOCUMENTO` | `varchar(50)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `DATA_VALIDADE` | `date` | YES |  |  |  |
| `CREATED_BY_ID` | `int` | YES |  |  |  |
| `TIPO_DOCUMENTO_ID` | `int` | NO |  |  |  |

#### `EMPRESAS_ENDERECOEVENT`

- **PK:** `PGH_ID` (`EMPRESAS_ENDERECOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `LOGRADOURO` | `varchar(255)` | NO |  |  |  |
| `NUMERO` | `varchar(20)` | NO |  |  |  |
| `COMPLEMENTO` | `varchar(100)` | YES |  |  |  |
| `BAIRRO` | `varchar(100)` | NO |  |  |  |
| `CIDADE` | `varchar(100)` | NO |  |  |  |
| `ESTADO` | `varchar(2)` | NO |  |  |  |
| `CEP` | `varchar(10)` | YES |  |  |  |
| `PAIS` | `varchar(50)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `NOTIFICACOES_NOTIFICACAOEVENT`

- **PK:** `PGH_ID` (`NOTIFICACOES_NOTIFICACAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(200)` | NO |  |  |  |
| `MENSAGEM` | `text` | NO |  |  |  |
| `LINK` | `varchar(200)` | NO |  |  |  |
| `DESTINATARIO_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `FUNCIONARIOS`

- **PK:** `ID` (`FUNCIONARIOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `MATRICULA` | `varchar(50)` | NO |  |  |  |
| `DATA_ADMISSAO` | `date` | NO |  |  |  |
| `DATA_DEMISSAO` | `date` | YES |  |  |  |
| `TIPO_CONTRATACAO` | `varchar(20)` | NO |  |  |  |
| `CARGA_HORARIA_CONTRATUAL_MENSAL` | `numeric(6, 2)` | NO |  |  |  |
| `PESSOA_ID` | `int` | NO |  |  |  |

#### `EMPRESAS`

- **PK:** `ID` (`EMPRESAS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME_FANTASIA` | `varchar(200)` | NO |  |  |  |
| `RAZAO_SOCIAL` | `varchar(200)` | NO |  |  |  |
| `CNPJ` | `varchar(18)` | NO |  |  |  |
| `EMAIL` | `varchar(255)` | NO |  |  |  |
| `TELEFONE` | `varchar(20)` | NO |  |  |  |
| `ENDERECO_ID` | `int` | YES |  |  |  |

#### `DJANGO_CELERY_BEAT_PERIODICTASK`

- **PK:** `ID` (`DJANGO_CELERY_BEAT_PERIODICTASK_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `NAME` | `varchar(200)` | NO |  |  |  |
| `TASK` | `varchar(200)` | NO |  |  |  |
| `ARGS` | `text` | NO |  |  |  |
| `KWARGS` | `text` | NO |  |  |  |
| `QUEUE` | `varchar(200)` | YES |  |  |  |
| `EXCHANGE` | `varchar(200)` | YES |  |  |  |
| `ROUTING_KEY` | `varchar(200)` | YES |  |  |  |
| `EXPIRES` | `timestamp` | YES |  |  |  |
| `LAST_RUN_AT` | `timestamp` | YES |  |  |  |
| `TOTAL_RUN_COUNT` | `int` | NO |  |  |  |
| `DATE_CHANGED` | `timestamp` | NO |  |  |  |
| `DESCRIPTION` | `text` | NO |  |  |  |
| `CRONTAB_ID` | `int` | YES |  |  |  |
| `INTERVAL_ID` | `int` | YES |  |  |  |
| `SOLAR_ID` | `int` | YES |  |  |  |
| `START_TIME` | `timestamp` | YES |  |  |  |
| `PRIORITY` | `int` | YES |  |  |  |
| `HEADERS` | `text` | NO |  |  |  |
| `CLOCKED_ID` | `int` | YES |  |  |  |
| `EXPIRE_SECONDS` | `int` | YES |  |  |  |

#### `USUARIOS_USER_PERMISSIONS`

- **PK:** `ID` (`USUARIOS_USER_PERMISSIONS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `PERMISSION_ID` | `int` | NO |  |  |  |

#### `RELATORIOS_RELATORIOVISITAEVENT`

- **PK:** `PGH_ID` (`RELATORIOS_RELATORIOVISITAEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(300)` | NO |  |  |  |
| `DATA_EMISSAO` | `date` | NO |  |  |  |
| `STATUS` | `varchar(20)` | NO |  |  |  |
| `OBSERVACOES_GERAIS` | `text` | NO |  |  |  |
| `DATA_VISITA` | `date` | NO |  |  |  |
| `LOCAL_ESPECIFICO` | `varchar(255)` | NO |  |  |  |
| `EQUIPE` | `text` | NO |  |  |  |
| `OBJETIVO` | `text` | NO |  |  |  |
| `TAREFAS` | `text` | NO |  |  |  |
| `PENDENCIAS` | `text` | NO |  |  |  |
| `PROXIMAS_ACOES` | `text` | NO |  |  |  |
| `AVALIACAO_CLIENTE` | `int` | YES |  |  |  |
| `ASSINATURA_CLIENTE` | `varchar(200)` | NO |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `TIPO_RELATORIO_ID` | `int` | NO |  |  |  |

#### `ESTOQUE_VEICULOEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_VEICULOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `PLACA` | `varchar(10)` | NO |  |  |  |
| `RENAVAM` | `varchar(20)` | NO |  |  |  |
| `MARCA` | `varchar(50)` | NO |  |  |  |
| `MODELO` | `varchar(50)` | NO |  |  |  |
| `ANO_FABRICACAO` | `int` | NO |  |  |  |
| `DATA_LICENCIAMENTO` | `date` | NO |  |  |  |
| `PROPRIETARIO_TIPO` | `varchar(20)` | NO |  |  |  |
| `PROPRIETARIO_ID` | `int` | NO |  |  |  |
| `VALOR_AQUISICAO` | `numeric(12, 2)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `STATUS_ID` | `int` | NO |  |  |  |

#### `ESTOQUE_MATERIALEVENT`

- **PK:** `PGH_ID` (`ESTOQUE_MATERIALEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `DATA_VALIDADE` | `date` | YES |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `TOKEN_BLACKLIST_OUTSTANDINGTOKEN`

- **PK:** `ID` (`TOKEN_BLACKLIST_OUTSTANDINGTOKEN_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `TOKEN` | `text` | NO |  |  |  |
| `CREATED_AT` | `timestamp` | YES |  |  |  |
| `EXPIRES_AT` | `timestamp` | NO |  |  |  |
| `USER_ID` | `int` | YES |  |  |  |
| `JTI` | `varchar(255)` | NO |  |  |  |

#### `DJANGO_CELERY_RESULTS_TASKRESULT`

- **PK:** `ID` (`DJANGO_CELERY_RESULTS_TASKRESULT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `TASK_ID` | `varchar(255)` | NO |  |  |  |
| `STATUS` | `varchar(50)` | NO |  |  |  |
| `CONTENT_TYPE` | `varchar(128)` | NO |  |  |  |
| `CONTENT_ENCODING` | `varchar(64)` | NO |  |  |  |
| `RESULT` | `text` | YES |  |  |  |
| `DATE_DONE` | `timestamp` | NO |  |  |  |
| `TRACEBACK` | `text` | YES |  |  |  |
| `META` | `text` | YES |  |  |  |
| `TASK_ARGS` | `text` | YES |  |  |  |
| `TASK_KWARGS` | `text` | YES |  |  |  |
| `TASK_NAME` | `varchar(255)` | YES |  |  |  |
| `WORKER` | `varchar(100)` | YES |  |  |  |
| `DATE_CREATED` | `timestamp` | NO |  |  |  |
| `PERIODIC_TASK_NAME` | `varchar(255)` | YES |  |  |  |
| `DATE_STARTED` | `timestamp` | YES |  |  |  |

#### `FUNCIONARIO_MOVIMENTO`

- **PK:** `ID` (`FUNCIONARIO_MOVIMENTO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `DATA_MOVIMENTO` | `date` | NO |  |  |  |
| `MOTIVO` | `text` | NO |  |  |  |
| `CREATED_BY_ID` | `int` | YES |  |  |  |
| `DE_CONTRATO_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |
| `PARA_CONTRATO_ID` | `int` | NO |  |  |  |

#### `EQUIPAMENTOS`

- **PK:** `ID` (`EQUIPAMENTOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `CODIGO_PRODUTO` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | YES |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `VALOR_ATUAL` | `numeric(12, 2)` | YES |  |  |  |
| `QUANTIDADE_ESTOQUE` | `numeric(12, 4)` | NO |  |  |  |
| `NUMERO_SERIE` | `varchar(100)` | NO |  |  |  |
| `DATA_AQUISICAO` | `date` | NO |  |  |  |
| `GARANTIA_FIM` | `date` | NO |  |  |  |
| `CATEGORIA_ID` | `int` | NO |  |  |  |
| `UNIDADE_MEDIDA_ID` | `int` | NO |  |  |  |

#### `DOCUMENTOS_TIPODOCUMENTOEVENT`

- **PK:** `PGH_ID` (`DOCUMENTOS_TIPODOCUMENTOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `KANBAN_KANBANQUADROEVENT`

- **PK:** `PGH_ID` (`KANBAN_KANBANQUADROEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `ANO` | `int` | NO |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |
| `EMPRESA_ID` | `int` | YES |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `CONTRATO_ITEM_ALOCADO`

- **PK:** `ID` (`CONTRATO_ITEM_ALOCADO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `ITEM_TIPO` | `varchar(20)` | NO |  |  |  |
| `ITEM_ID` | `int` | NO |  |  |  |
| `QUANTIDADE_ALOCADA` | `numeric(12, 4)` | NO |  |  |  |
| `QUANTIDADE_DEVOLVIDA` | `numeric(12, 4)` | NO |  |  |  |
| `DATA_ALOCACAO` | `timestamp` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `CONTRATO_ID` | `int` | NO |  |  |  |

#### `MOVIMENTACAO_ESTOQUE`

- **PK:** `ID` (`MOVIMENTACAO_ESTOQUE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `ITEM_TIPO` | `varchar(20)` | NO |  |  |  |
| `ITEM_ID` | `int` | NO |  |  |  |
| `QUANTIDADE` | `numeric(12, 4)` | NO |  |  |  |
| `DATA_MOVIMENTO` | `timestamp` | NO |  |  |  |
| `ORIGEM` | `varchar(255)` | NO |  |  |  |
| `DESTINO` | `varchar(255)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `TIPO_MOVIMENTACAO_ID` | `int` | NO |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |

#### `MOVIMENTACOES_TIPOMOVIMENTACAOEVENT`

- **PK:** `PGH_ID` (`MOVIMENTACOES_TIPOMOVIMENTACAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `NATUREZA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `CATEGORIA_ITEM`

- **PK:** `ID` (`CATEGORIA_ITEM_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `GRUPO_PERMISSOES_PERMISSOES`

- **PK:** `ID` (`GRUPO_PERMISSOES_PERMISSOES_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `GRUPOPERMISSAO_ID` | `int` | NO |  |  |  |
| `PERMISSAO_ID` | `int` | NO |  |  |  |

#### `TOKEN_BLACKLIST_BLACKLISTEDTOKEN`

- **PK:** `ID` (`TOKEN_BLACKLIST_BLACKLISTEDTOKEN_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `BLACKLISTED_AT` | `timestamp` | NO |  |  |  |
| `TOKEN_ID` | `int` | NO |  |  |  |

#### `DJANGO_CELERY_RESULTS_CHORDCOUNTER`

- **PK:** `ID` (`DJANGO_CELERY_RESULTS_CHORDCOUNTER_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `varchar(255)` | NO |  |  |  |
| `SUB_TASKS` | `text` | NO |  |  |  |
| `COUNT` | `int` | NO |  |  |  |

#### `RELATORIOS_TIPORELATORIOEVENT`

- **PK:** `PGH_ID` (`RELATORIOS_TIPORELATORIOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `TEMPLATE_HTML` | `text` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `KANBAN_QUADRO`

- **PK:** `ID` (`KANBAN_QUADRO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(200)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `ANO` | `int` | NO |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |
| `EMPRESA_ID` | `int` | YES |  |  |  |

#### `DJANGO_CELERY_BEAT_CRONTABSCHEDULE`

- **PK:** `ID` (`DJANGO_CELERY_BEAT_CRONTABSCHEDULE_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `MINUTE` | `varchar(240)` | NO |  |  |  |
| `HOUR` | `varchar(96)` | NO |  |  |  |
| `DAY_OF_WEEK` | `varchar(64)` | NO |  |  |  |
| `DAY_OF_MONTH` | `varchar(124)` | NO |  |  |  |
| `MONTH_OF_YEAR` | `varchar(64)` | NO |  |  |  |
| `TIMEZONE` | `varchar(63)` | NO |  |  |  |

#### `KANBAN_CARD_RESPONSAVEIS`

- **PK:** `ID` (`KANBAN_CARD_RESPONSAVEIS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `KANBANCARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `NOTIFICACOES_PERMISSAOEVENT`

- **PK:** `PGH_ID` (`NOTIFICACOES_PERMISSAOEVENT_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `PGH_ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `PGH_CREATED_AT` | `timestamp` | NO |  |  |  |
| `PGH_LABEL` | `text` | NO |  |  |  |
| `ID` | `int` | NO |  |  |  |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `RECURSO` | `varchar(100)` | NO |  |  |  |
| `ACAO` | `varchar(50)` | NO |  |  |  |
| `PGH_OBJ_ID` | `int` | NO |  |  |  |

#### `EMPRESA_SOCIOS`

- **PK:** `ID` (`EMPRESA_SOCIOS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TIPO` | `varchar(20)` | NO |  |  |  |
| `PERCENTUAL` | `numeric(5, 2)` | YES |  |  |  |
| `DATA_INICIO` | `date` | NO |  |  |  |
| `DATA_FIM` | `date` | YES |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `PESSOA_ID` | `int` | NO |  |  |  |

#### `USUARIOS_GROUPS`

- **PK:** `ID` (`USUARIOS_GROUPS_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `GROUP_ID` | `int` | NO |  |  |  |

#### `KANBAN_CARD`

- **PK:** `ID` (`KANBAN_CARD_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(300)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |
| `COLUNA` | `varchar(50)` | NO |  |  |  |
| `ORDEM` | `int` | NO |  |  |  |
| `DATA_LIMITE` | `date` | YES |  |  |  |
| `DATA_INICIO` | `date` | YES |  |  |  |
| `DATA_CONCLUSAO` | `date` | YES |  |  |  |
| `PRIORIDADE` | `varchar(20)` | NO |  |  |  |
| `ESTIMATIVA_HORAS` | `numeric(6, 2)` | YES |  |  |  |
| `CONTRATO_ID` | `int` | YES |  |  |  |
| `CRIADO_POR_ID` | `int` | NO |  |  |  |
| `FUNCIONARIO_ID` | `int` | YES |  |  |  |
| `QUADRO_ID` | `int` | NO |  |  |  |

#### `TIPO_MOVIMENTACAO`

- **PK:** `ID` (`TIPO_MOVIMENTACAO_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `NATUREZA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `RELATORIO_VISITA`

- **PK:** `ID` (`RELATORIO_VISITA_PKEY`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TITULO` | `varchar(300)` | NO |  |  |  |
| `DATA_EMISSAO` | `date` | NO |  |  |  |
| `STATUS` | `varchar(20)` | NO |  |  |  |
| `OBSERVACOES_GERAIS` | `text` | NO |  |  |  |
| `DATA_VISITA` | `date` | NO |  |  |  |
| `LOCAL_ESPECIFICO` | `varchar(255)` | NO |  |  |  |
| `EQUIPE` | `text` | NO |  |  |  |
| `OBJETIVO` | `text` | NO |  |  |  |
| `TAREFAS` | `text` | NO |  |  |  |
| `PENDENCIAS` | `text` | NO |  |  |  |
| `PROXIMAS_ACOES` | `text` | NO |  |  |  |
| `AVALIACAO_CLIENTE` | `int` | YES |  |  |  |
| `ASSINATURA_CLIENTE` | `varchar(200)` | NO |  |  |  |
| `EMPRESA_ID` | `int` | NO |  |  |  |
| `RESPONSAVEL_ID` | `int` | NO |  |  |  |
| `TIPO_RELATORIO_ID` | `int` | NO |  |  |  |

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `KANBAN_MOVIMENTO` | `KANBAN_MOVIMENTO_PKEY` | `ID` |
| `DJANGO_MIGRATIONS` | `DJANGO_MIGRATIONS_PKEY` | `ID` |
| `NOTIFICACOES_GRUPOPERMISSAOEVENT` | `NOTIFICACOES_GRUPOPERMISSAOEVENT_PKEY` | `PGH_ID` |
| `KANBAN_KANBANOBSERVACAOEVENT` | `KANBAN_KANBANOBSERVACAOEVENT_PKEY` | `PGH_ID` |
| `USUARIOS_USUARIOEVENT` | `USUARIOS_USUARIOEVENT_PKEY` | `PGH_ID` |
| `CONTRATOS` | `CONTRATOS_PKEY` | `ID` |
| `NOTIFICACOES` | `NOTIFICACOES_PKEY` | `ID` |
| `DOCUMENTOS_DOCUMENTOEVENT` | `DOCUMENTOS_DOCUMENTOEVENT_PKEY` | `PGH_ID` |
| `MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT` | `MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT_PKEY` | `PGH_ID` |
| `TIPO_RELATORIO` | `TIPO_RELATORIO_PKEY` | `ID` |
| `ENDERECOS` | `ENDERECOS_PKEY` | `ID` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `KANBAN_ATIVIDADE_CONCLUIDA_PKEY` | `ID` |
| `UNIDADE_MEDIDA` | `UNIDADE_MEDIDA_PKEY` | `ID` |
| `AUTH_GROUP` | `AUTH_GROUP_PKEY` | `ID` |
| `DJANGO_CELERY_BEAT_INTERVALSCHEDULE` | `DJANGO_CELERY_BEAT_INTERVALSCHEDULE_PKEY` | `ID` |
| `PGHISTORY_CONTEXT` | `PGHISTORY_CONTEXT_PKEY` | `ID` |
| `DJANGO_ADMIN_LOG` | `DJANGO_ADMIN_LOG_PKEY` | `ID` |
| `USUARIOS` | `USUARIOS_PKEY` | `ID` |
| `ESTOQUE_UNIDADEMEDIDAEVENT` | `ESTOQUE_UNIDADEMEDIDAEVENT_PKEY` | `PGH_ID` |
| `AVALIACOES_AVALIACAOEVENT` | `AVALIACOES_AVALIACAOEVENT_PKEY` | `PGH_ID` |
| `PERMISSOES` | `PERMISSOES_PKEY` | `ID` |
| `MATERIAIS` | `MATERIAIS_PKEY` | `ID` |
| `DJANGO_SESSION` | `DJANGO_SESSION_PKEY` | `SESSION_KEY` |
| `FERRAMENTAS` | `FERRAMENTAS_PKEY` | `ID` |
| `KANBAN_KANBANCARDEVENT` | `KANBAN_KANBANCARDEVENT_PKEY` | `PGH_ID` |
| `ROTULOS` | `ROTULOS_PKEY` | `ID` |
| `DJANGO_CONTENT_TYPE` | `DJANGO_CONTENT_TYPE_PKEY` | `ID` |
| `ITEM_ROTULO` | `ITEM_ROTULO_PKEY` | `ID` |
| `TIPO_DOCUMENTO` | `TIPO_DOCUMENTO_PKEY` | `ID` |
| `PESSOAS_FUNCIONARIOEVENT` | `PESSOAS_FUNCIONARIOEVENT_PKEY` | `PGH_ID` |
| `EMPRESAS_SOCIOADMINISTRADOREVENT` | `EMPRESAS_SOCIOADMINISTRADOREVENT_PKEY` | `PGH_ID` |
| `EMPRESAS_EMPRESAEVENT` | `EMPRESAS_EMPRESAEVENT_PKEY` | `PGH_ID` |
| `TRANSACAO_CONTRATO` | `TRANSACAO_CONTRATO_PKEY` | `ID` |
| `CONTRATOS_CONTRATOEVENT` | `CONTRATOS_CONTRATOEVENT_PKEY` | `PGH_ID` |
| `CONTRATOS_FUNCIONARIOMOVIMENTOEVENT` | `CONTRATOS_FUNCIONARIOMOVIMENTOEVENT_PKEY` | `PGH_ID` |
| `ITEM_AVALIACAO` | `ITEM_AVALIACAO_PKEY` | `ID` |
| `AVALIACOES` | `AVALIACOES_PKEY` | `ID` |
| `ANEXO_RELATORIO` | `ANEXO_RELATORIO_PKEY` | `ID` |
| `ESTOQUE_EQUIPAMENTOEVENT` | `ESTOQUE_EQUIPAMENTOEVENT_PKEY` | `PGH_ID` |
| `DJANGO_CELERY_RESULTS_GROUPRESULT` | `DJANGO_CELERY_RESULTS_GROUPRESULT_PKEY` | `ID` |
| `PESSOAS_PESSOAEVENT` | `PESSOAS_PESSOAEVENT_PKEY` | `PGH_ID` |
| `AUTH_PERMISSION` | `AUTH_PERMISSION_PKEY` | `ID` |
| `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE` | `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE_PKEY` | `ID` |
| `DJANGO_CELERY_BEAT_PERIODICTASKS` | `DJANGO_CELERY_BEAT_PERIODICTASKS_PKEY` | `IDENT` |
| `KANBAN_KANBANATIVIDADECONCLUIDAEVENT` | `KANBAN_KANBANATIVIDADECONCLUIDAEVENT_PKEY` | `PGH_ID` |
| `ESTOQUE_FERRAMENTAEVENT` | `ESTOQUE_FERRAMENTAEVENT_PKEY` | `PGH_ID` |
| `FUNCIONARIO_PERMISSAO` | `FUNCIONARIO_PERMISSAO_PKEY` | `ID` |
| `VEICULOS` | `VEICULOS_PKEY` | `ID` |
| `FINANCEIRO_TRANSACAOCONTRATOEVENT` | `FINANCEIRO_TRANSACAOCONTRATOEVENT_PKEY` | `PGH_ID` |
| `CONTRATOS_FUNCIONARIOCONTRATOEVENT` | `CONTRATOS_FUNCIONARIOCONTRATOEVENT_PKEY` | `PGH_ID` |
| `KANBAN_OBSERVACAO` | `KANBAN_OBSERVACAO_PKEY` | `ID` |
| `PESSOAS` | `PESSOAS_PKEY` | `ID` |
| `ESTOQUE_CATEGORIAITEMEVENT` | `ESTOQUE_CATEGORIAITEMEVENT_PKEY` | `PGH_ID` |
| `STATUS` | `STATUS_PKEY` | `ID` |
| `DOCUMENTO_ROTULO` | `DOCUMENTO_ROTULO_PKEY` | `ID` |
| `DOCUMENTOS_ROTULOEVENT` | `DOCUMENTOS_ROTULOEVENT_PKEY` | `PGH_ID` |
| `AUTH_GROUP_PERMISSIONS` | `AUTH_GROUP_PERMISSIONS_PKEY` | `ID` |
| `AVALIACAO_ITEM` | `AVALIACAO_ITEM_PKEY` | `ID` |
| `CONTRATOS_STATUSEVENT` | `CONTRATOS_STATUSEVENT_PKEY` | `PGH_ID` |
| `FUNCIONARIO_CONTRATO` | `FUNCIONARIO_CONTRATO_PKEY` | `ID` |
| `AVALIACOES_ITEMAVALIACAOEVENT` | `AVALIACOES_ITEMAVALIACAOEVENT_PKEY` | `PGH_ID` |
| `DJANGO_CELERY_BEAT_SOLARSCHEDULE` | `DJANGO_CELERY_BEAT_SOLARSCHEDULE_PKEY` | `ID` |
| `GRUPO_PERMISSOES` | `GRUPO_PERMISSOES_PKEY` | `ID` |
| `DOCUMENTOS` | `DOCUMENTOS_PKEY` | `ID` |
| `EMPRESAS_ENDERECOEVENT` | `EMPRESAS_ENDERECOEVENT_PKEY` | `PGH_ID` |
| `NOTIFICACOES_NOTIFICACAOEVENT` | `NOTIFICACOES_NOTIFICACAOEVENT_PKEY` | `PGH_ID` |
| `FUNCIONARIOS` | `FUNCIONARIOS_PKEY` | `ID` |
| `EMPRESAS` | `EMPRESAS_PKEY` | `ID` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `DJANGO_CELERY_BEAT_PERIODICTASK_PKEY` | `ID` |
| `USUARIOS_USER_PERMISSIONS` | `USUARIOS_USER_PERMISSIONS_PKEY` | `ID` |
| `RELATORIOS_RELATORIOVISITAEVENT` | `RELATORIOS_RELATORIOVISITAEVENT_PKEY` | `PGH_ID` |
| `ESTOQUE_VEICULOEVENT` | `ESTOQUE_VEICULOEVENT_PKEY` | `PGH_ID` |
| `ESTOQUE_MATERIALEVENT` | `ESTOQUE_MATERIALEVENT_PKEY` | `PGH_ID` |
| `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `TOKEN_BLACKLIST_OUTSTANDINGTOKEN_PKEY` | `ID` |
| `DJANGO_CELERY_RESULTS_TASKRESULT` | `DJANGO_CELERY_RESULTS_TASKRESULT_PKEY` | `ID` |
| `FUNCIONARIO_MOVIMENTO` | `FUNCIONARIO_MOVIMENTO_PKEY` | `ID` |
| `EQUIPAMENTOS` | `EQUIPAMENTOS_PKEY` | `ID` |
| `DOCUMENTOS_TIPODOCUMENTOEVENT` | `DOCUMENTOS_TIPODOCUMENTOEVENT_PKEY` | `PGH_ID` |
| `KANBAN_KANBANQUADROEVENT` | `KANBAN_KANBANQUADROEVENT_PKEY` | `PGH_ID` |
| `CONTRATO_ITEM_ALOCADO` | `CONTRATO_ITEM_ALOCADO_PKEY` | `ID` |
| `MOVIMENTACAO_ESTOQUE` | `MOVIMENTACAO_ESTOQUE_PKEY` | `ID` |
| `MOVIMENTACOES_TIPOMOVIMENTACAOEVENT` | `MOVIMENTACOES_TIPOMOVIMENTACAOEVENT_PKEY` | `PGH_ID` |
| `CATEGORIA_ITEM` | `CATEGORIA_ITEM_PKEY` | `ID` |
| `GRUPO_PERMISSOES_PERMISSOES` | `GRUPO_PERMISSOES_PERMISSOES_PKEY` | `ID` |
| `TOKEN_BLACKLIST_BLACKLISTEDTOKEN` | `TOKEN_BLACKLIST_BLACKLISTEDTOKEN_PKEY` | `ID` |
| `DJANGO_CELERY_RESULTS_CHORDCOUNTER` | `DJANGO_CELERY_RESULTS_CHORDCOUNTER_PKEY` | `ID` |
| `RELATORIOS_TIPORELATORIOEVENT` | `RELATORIOS_TIPORELATORIOEVENT_PKEY` | `PGH_ID` |
| `KANBAN_QUADRO` | `KANBAN_QUADRO_PKEY` | `ID` |
| `DJANGO_CELERY_BEAT_CRONTABSCHEDULE` | `DJANGO_CELERY_BEAT_CRONTABSCHEDULE_PKEY` | `ID` |
| `KANBAN_CARD_RESPONSAVEIS` | `KANBAN_CARD_RESPONSAVEIS_PKEY` | `ID` |
| `NOTIFICACOES_PERMISSAOEVENT` | `NOTIFICACOES_PERMISSAOEVENT_PKEY` | `PGH_ID` |
| `EMPRESA_SOCIOS` | `EMPRESA_SOCIOS_PKEY` | `ID` |
| `USUARIOS_GROUPS` | `USUARIOS_GROUPS_PKEY` | `ID` |
| `KANBAN_CARD` | `KANBAN_CARD_PKEY` | `ID` |
| `TIPO_MOVIMENTACAO` | `TIPO_MOVIMENTACAO_PKEY` | `ID` |
| `RELATORIO_VISITA` | `RELATORIO_VISITA_PKEY` | `ID` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `KANBAN_MOVIMENTO` | `CARD_ID` | `KANBAN_CARD` | `ID` | `KANBAN_MOVIMENTO_CARD_ID_823BBF8D_FK_KANBAN_CARD_ID` |
| `KANBAN_MOVIMENTO` | `USUARIO_ID` | `USUARIOS` | `ID` | `KANBAN_MOVIMENTO_USUARIO_ID_81CA9982_FK_USUARIOS_ID` |
| `CONTRATOS` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `CONTRATOS_EMPRESA_ID_7A23F8CB_FK_EMPRESAS_ID` |
| `CONTRATOS` | `GESTOR_RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `CONTRATOS_GESTOR_RESPONSAVEL_ID_F34999A6_FK_FUNCIONARIOS_ID` |
| `CONTRATOS` | `LOCAL_EXECUCAO_ID` | `ENDERECOS` | `ID` | `CONTRATOS_LOCAL_EXECUCAO_ID_51882E4D_FK_ENDERECOS_ID` |
| `CONTRATOS` | `STATUS_ID` | `STATUS` | `ID` | `CONTRATOS_STATUS_ID_FB9BA518_FK_STATUS_ID` |
| `NOTIFICACOES` | `DESTINATARIO_ID` | `FUNCIONARIOS` | `ID` | `NOTIFICACOES_DESTINATARIO_ID_91F2A446_FK_FUNCIONARIOS_ID` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `CARD_ID` | `KANBAN_CARD` | `ID` | `KANBAN_ATIVIDADE_CONCLUIDA_CARD_ID_BEE61DC1_FK_KANBAN_CARD_ID` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `USUARIO_ID` | `USUARIOS` | `ID` | `KANBAN_ATIVIDADE_CONCLUIDA_USUARIO_ID_D83278C2_FK_USUARIOS_ID` |
| `DJANGO_ADMIN_LOG` | `CONTENT_TYPE_ID` | `DJANGO_CONTENT_TYPE` | `ID` | `DJANGO_ADMIN_LOG_CONTENT_TYPE_ID_C4BCE8EB_FK_DJANGO_CO` |
| `DJANGO_ADMIN_LOG` | `USER_ID` | `USUARIOS` | `ID` | `DJANGO_ADMIN_LOG_USER_ID_C564EBA6_FK_USUARIOS_ID` |
| `USUARIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `USUARIOS_PESSOA_ID_0331F0F2_FK_PESSOAS_ID` |
| `MATERIAIS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `MATERIAIS_CATEGORIA_ID_EE883D56_FK_CATEGORIA_ITEM_ID` |
| `MATERIAIS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `MATERIAIS_UNIDADE_MEDIDA_ID_A54A9D6B_FK_UNIDADE_MEDIDA_ID` |
| `FERRAMENTAS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `FERRAMENTAS_CATEGORIA_ID_3B419683_FK_CATEGORIA_ITEM_ID` |
| `FERRAMENTAS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `FERRAMENTAS_UNIDADE_MEDIDA_ID_5A83D675_FK_UNIDADE_MEDIDA_ID` |
| `ITEM_ROTULO` | `ROTULO_ID` | `ROTULOS` | `ID` | `ITEM_ROTULO_ROTULO_ID_DA37D665_FK_ROTULOS_ID` |
| `TRANSACAO_CONTRATO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `TRANSACAO_CONTRATO_CONTRATO_ID_CEAF0FFF_FK_CONTRATOS_ID` |
| `AVALIACOES` | `AVALIADOR_ID` | `PESSOAS` | `ID` | `AVALIACOES_AVALIADOR_ID_45CC8A45_FK_PESSOAS_ID` |
| `AVALIACOES` | `RATIFICADOR_ID` | `PESSOAS` | `ID` | `AVALIACOES_RATIFICADOR_ID_F050C022_FK_PESSOAS_ID` |
| `ANEXO_RELATORIO` | `ENVIADO_POR_ID` | `FUNCIONARIOS` | `ID` | `ANEXO_RELATORIO_ENVIADO_POR_ID_BA0A79C0_FK_FUNCIONARIOS_ID` |
| `ANEXO_RELATORIO` | `RELATORIO_ID` | `RELATORIO_VISITA` | `ID` | `ANEXO_RELATORIO_RELATORIO_ID_41DE4F28_FK_RELATORIO_VISITA_ID` |
| `AUTH_PERMISSION` | `CONTENT_TYPE_ID` | `DJANGO_CONTENT_TYPE` | `ID` | `AUTH_PERMISSION_CONTENT_TYPE_ID_2F476E4B_FK_DJANGO_CO` |
| `FUNCIONARIO_PERMISSAO` | `CONCEDIDO_POR_ID` | `FUNCIONARIOS` | `ID` | `FUNCIONARIO_PERMISSA_CONCEDIDO_POR_ID_EA8B4963_FK_FUNCIONAR` |
| `FUNCIONARIO_PERMISSAO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `FUNCIONARIO_PERMISSA_FUNCIONARIO_ID_DC9F3230_FK_FUNCIONAR` |
| `FUNCIONARIO_PERMISSAO` | `PERMISSAO_ID` | `PERMISSOES` | `ID` | `FUNCIONARIO_PERMISSAO_PERMISSAO_ID_87336C7B_FK_PERMISSOES_ID` |
| `VEICULOS` | `STATUS_ID` | `STATUS` | `ID` | `VEICULOS_STATUS_ID_5F131383_FK_STATUS_ID` |
| `KANBAN_OBSERVACAO` | `CARD_ID` | `KANBAN_CARD` | `ID` | `KANBAN_OBSERVACAO_CARD_ID_B09A0C7A_FK_KANBAN_CARD_ID` |
| `KANBAN_OBSERVACAO` | `USUARIO_ID` | `USUARIOS` | `ID` | `KANBAN_OBSERVACAO_USUARIO_ID_CAF6EC6C_FK_USUARIOS_ID` |
| `PESSOAS` | `ENDERECO_ID` | `ENDERECOS` | `ID` | `PESSOAS_ENDERECO_ID_758F075E_FK_ENDERECOS_ID` |
| `DOCUMENTO_ROTULO` | `DOCUMENTO_ID` | `DOCUMENTOS` | `ID` | `DOCUMENTO_ROTULO_DOCUMENTO_ID_B68C8743_FK_DOCUMENTOS_ID` |
| `DOCUMENTO_ROTULO` | `ROTULO_ID` | `ROTULOS` | `ID` | `DOCUMENTO_ROTULO_ROTULO_ID_B428C401_FK_ROTULOS_ID` |
| `AUTH_GROUP_PERMISSIONS` | `PERMISSION_ID` | `AUTH_PERMISSION` | `ID` | `AUTH_GROUP_PERMISSIO_PERMISSION_ID_84C5C92E_FK_AUTH_PERM` |
| `AUTH_GROUP_PERMISSIONS` | `GROUP_ID` | `AUTH_GROUP` | `ID` | `AUTH_GROUP_PERMISSIONS_GROUP_ID_B120CBF9_FK_AUTH_GROUP_ID` |
| `AVALIACAO_ITEM` | `AVALIACAO_ID` | `AVALIACOES` | `ID` | `AVALIACAO_ITEM_AVALIACAO_ID_CD3264F4_FK_AVALIACOES_ID` |
| `AVALIACAO_ITEM` | `ITEM_AVALIACAO_ID` | `ITEM_AVALIACAO` | `ID` | `AVALIACAO_ITEM_ITEM_AVALIACAO_ID_6EA3B81B_FK_ITEM_AVALIACAO_ID` |
| `FUNCIONARIO_CONTRATO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `FUNCIONARIO_CONTRATO_CONTRATO_ID_5BDCDB13_FK_CONTRATOS_ID` |
| `FUNCIONARIO_CONTRATO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `FUNCIONARIO_CONTRATO_FUNCIONARIO_ID_7E02E8D4_FK_FUNCIONARIOS_ID` |
| `DOCUMENTOS` | `CREATED_BY_ID` | `FUNCIONARIOS` | `ID` | `DOCUMENTOS_CREATED_BY_ID_6CE1C352_FK_FUNCIONARIOS_ID` |
| `DOCUMENTOS` | `TIPO_DOCUMENTO_ID` | `TIPO_DOCUMENTO` | `ID` | `DOCUMENTOS_TIPO_DOCUMENTO_ID_BB661BA3_FK_TIPO_DOCUMENTO_ID` |
| `FUNCIONARIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `FUNCIONARIOS_PESSOA_ID_1E1211C6_FK_PESSOAS_ID` |
| `EMPRESAS` | `ENDERECO_ID` | `ENDERECOS` | `ID` | `EMPRESAS_ENDERECO_ID_CE47B5FF_FK_ENDERECOS_ID` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `CLOCKED_ID` | `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE` | `ID` | `DJANGO_CELERY_BEAT_P_CLOCKED_ID_47A69F82_FK_DJANGO_CE` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `CRONTAB_ID` | `DJANGO_CELERY_BEAT_CRONTABSCHEDULE` | `ID` | `DJANGO_CELERY_BEAT_P_CRONTAB_ID_D3CBA168_FK_DJANGO_CE` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `INTERVAL_ID` | `DJANGO_CELERY_BEAT_INTERVALSCHEDULE` | `ID` | `DJANGO_CELERY_BEAT_P_INTERVAL_ID_A8CA27DA_FK_DJANGO_CE` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `SOLAR_ID` | `DJANGO_CELERY_BEAT_SOLARSCHEDULE` | `ID` | `DJANGO_CELERY_BEAT_P_SOLAR_ID_A87CE72C_FK_DJANGO_CE` |
| `USUARIOS_USER_PERMISSIONS` | `PERMISSION_ID` | `AUTH_PERMISSION` | `ID` | `USUARIOS_USER_PERMIS_PERMISSION_ID_AF615CA1_FK_AUTH_PERM` |
| `USUARIOS_USER_PERMISSIONS` | `USUARIO_ID` | `USUARIOS` | `ID` | `USUARIOS_USER_PERMISSIONS_USUARIO_ID_232FD58D_FK_USUARIOS_ID` |
| `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `USER_ID` | `USUARIOS` | `ID` | `TOKEN_BLACKLIST_OUTS_USER_ID_83BC629A_FK_USUARIOS_` |
| `FUNCIONARIO_MOVIMENTO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `FUNCIONARIO_MOVIMENT_FUNCIONARIO_ID_1FC836E7_FK_FUNCIONAR` |
| `FUNCIONARIO_MOVIMENTO` | `CREATED_BY_ID` | `FUNCIONARIOS` | `ID` | `FUNCIONARIO_MOVIMENTO_CREATED_BY_ID_367A195C_FK_FUNCIONARIOS_ID` |
| `FUNCIONARIO_MOVIMENTO` | `DE_CONTRATO_ID` | `CONTRATOS` | `ID` | `FUNCIONARIO_MOVIMENTO_DE_CONTRATO_ID_AF9D8BF9_FK_CONTRATOS_ID` |
| `FUNCIONARIO_MOVIMENTO` | `PARA_CONTRATO_ID` | `CONTRATOS` | `ID` | `FUNCIONARIO_MOVIMENTO_PARA_CONTRATO_ID_10426C41_FK_CONTRATOS_ID` |
| `EQUIPAMENTOS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `EQUIPAMENTOS_CATEGORIA_ID_A9274919_FK_CATEGORIA_ITEM_ID` |
| `EQUIPAMENTOS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `EQUIPAMENTOS_UNIDADE_MEDIDA_ID_FA020088_FK_UNIDADE_MEDIDA_ID` |
| `CONTRATO_ITEM_ALOCADO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `CONTRATO_ITEM_ALOCADO_CONTRATO_ID_C66D331B_FK_CONTRATOS_ID` |
| `MOVIMENTACAO_ESTOQUE` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `MOVIMENTACAO_ESTOQUE_CONTRATO_ID_B8368648_FK_CONTRATOS_ID` |
| `MOVIMENTACAO_ESTOQUE` | `RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `MOVIMENTACAO_ESTOQUE_RESPONSAVEL_ID_0B964E29_FK_FUNCIONARIOS_ID` |
| `MOVIMENTACAO_ESTOQUE` | `TIPO_MOVIMENTACAO_ID` | `TIPO_MOVIMENTACAO` | `ID` | `MOVIMENTACAO_ESTOQUE_TIPO_MOVIMENTACAO_ID_95BD7650_FK_TIPO_MOVI` |
| `GRUPO_PERMISSOES_PERMISSOES` | `GRUPOPERMISSAO_ID` | `GRUPO_PERMISSOES` | `ID` | `GRUPO_PERMISSOES_PER_GRUPOPERMISSAO_ID_B6817939_FK_GRUPO_PER` |
| `GRUPO_PERMISSOES_PERMISSOES` | `PERMISSAO_ID` | `PERMISSOES` | `ID` | `GRUPO_PERMISSOES_PER_PERMISSAO_ID_6418902F_FK_PERMISSOE` |
| `TOKEN_BLACKLIST_BLACKLISTEDTOKEN` | `TOKEN_ID` | `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `ID` | `TOKEN_BLACKLIST_BLACKLISTEDTOKEN_TOKEN_ID_3CC7FE56_FK` |
| `KANBAN_QUADRO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `KANBAN_QUADRO_CONTRATO_ID_26DC9A1C_FK_CONTRATOS_ID` |
| `KANBAN_QUADRO` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `KANBAN_QUADRO_EMPRESA_ID_256B898D_FK_EMPRESAS_ID` |
| `KANBAN_CARD_RESPONSAVEIS` | `KANBANCARD_ID` | `KANBAN_CARD` | `ID` | `KANBAN_CARD_RESPONSA_KANBANCARD_ID_1F8F2100_FK_KANBAN_CA` |
| `KANBAN_CARD_RESPONSAVEIS` | `USUARIO_ID` | `USUARIOS` | `ID` | `KANBAN_CARD_RESPONSAVEIS_USUARIO_ID_6C144E62_FK_USUARIOS_ID` |
| `EMPRESA_SOCIOS` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `EMPRESA_SOCIOS_EMPRESA_ID_53A6D4ED_FK_EMPRESAS_ID` |
| `EMPRESA_SOCIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `EMPRESA_SOCIOS_PESSOA_ID_A513D917_FK_PESSOAS_ID` |
| `USUARIOS_GROUPS` | `GROUP_ID` | `AUTH_GROUP` | `ID` | `USUARIOS_GROUPS_GROUP_ID_18C61092_FK_AUTH_GROUP_ID` |
| `USUARIOS_GROUPS` | `USUARIO_ID` | `USUARIOS` | `ID` | `USUARIOS_GROUPS_USUARIO_ID_1132CA50_FK_USUARIOS_ID` |
| `KANBAN_CARD` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `KANBAN_CARD_CONTRATO_ID_458A161B_FK_CONTRATOS_ID` |
| `KANBAN_CARD` | `CRIADO_POR_ID` | `USUARIOS` | `ID` | `KANBAN_CARD_CRIADO_POR_ID_291AE5E7_FK_USUARIOS_ID` |
| `KANBAN_CARD` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `KANBAN_CARD_FUNCIONARIO_ID_295DF478_FK_FUNCIONARIOS_ID` |
| `KANBAN_CARD` | `QUADRO_ID` | `KANBAN_QUADRO` | `ID` | `KANBAN_CARD_QUADRO_ID_A101EEB3_FK_KANBAN_QUADRO_ID` |
| `RELATORIO_VISITA` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `RELATORIO_VISITA_EMPRESA_ID_01129847_FK_EMPRESAS_ID` |
| `RELATORIO_VISITA` | `RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `RELATORIO_VISITA_RESPONSAVEL_ID_EE034725_FK_FUNCIONARIOS_ID` |
| `RELATORIO_VISITA` | `TIPO_RELATORIO_ID` | `TIPO_RELATORIO` | `ID` | `RELATORIO_VISITA_TIPO_RELATORIO_ID_54A6D546_FK_TIPO_RELA` |
