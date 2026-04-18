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

#### `ANEXO_RELATORIO`

- **PK:** `ID` (`anexo_relatorio_pkey`)

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

#### `AUTH_GROUP`

- **PK:** `ID` (`auth_group_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `NAME` | `varchar(150)` | NO |  |  |  |

#### `AUTH_GROUP_PERMISSIONS`

- **PK:** `ID` (`auth_group_permissions_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `int` | NO |  |  |  |
| `PERMISSION_ID` | `int` | NO |  |  |  |

#### `AUTH_PERMISSION`

- **PK:** `ID` (`auth_permission_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `NAME` | `varchar(255)` | NO |  |  |  |
| `CONTENT_TYPE_ID` | `int` | NO |  |  |  |
| `CODENAME` | `varchar(100)` | NO |  |  |  |

#### `AVALIACAO_ITEM`

- **PK:** `ID` (`avaliacao_item_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `NOTA` | `numeric(5, 2)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |
| `AVALIACAO_ID` | `int` | NO |  |  |  |
| `ITEM_AVALIACAO_ID` | `int` | NO |  |  |  |

#### `AVALIACOES`

- **PK:** `ID` (`avaliacoes_pkey`)

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

#### `AVALIACOES_AVALIACAOEVENT`

- **PK:** `PGH_ID` (`avaliacoes_avaliacaoevent_pkey`)

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

#### `AVALIACOES_ITEMAVALIACAOEVENT`

- **PK:** `PGH_ID` (`avaliacoes_itemavaliacaoevent_pkey`)

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

#### `CATEGORIA_ITEM`

- **PK:** `ID` (`categoria_item_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `CONTRATOS`

- **PK:** `ID` (`contratos_pkey`)

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

#### `CONTRATOS_CONTRATOEVENT`

- **PK:** `PGH_ID` (`contratos_contratoevent_pkey`)

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

#### `CONTRATOS_FUNCIONARIOCONTRATOEVENT`

- **PK:** `PGH_ID` (`contratos_funcionariocontratoevent_pkey`)

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

#### `CONTRATOS_FUNCIONARIOMOVIMENTOEVENT`

- **PK:** `PGH_ID` (`contratos_funcionariomovimentoevent_pkey`)

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

#### `CONTRATOS_STATUSEVENT`

- **PK:** `PGH_ID` (`contratos_statusevent_pkey`)

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

#### `CONTRATO_ITEM_ALOCADO`

- **PK:** `ID` (`contrato_item_alocado_pkey`)

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

#### `DJANGO_ADMIN_LOG`

- **PK:** `ID` (`django_admin_log_pkey`)

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

#### `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE`

- **PK:** `ID` (`django_celery_beat_clockedschedule_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `CLOCKED_TIME` | `timestamp` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_CRONTABSCHEDULE`

- **PK:** `ID` (`django_celery_beat_crontabschedule_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `MINUTE` | `varchar(240)` | NO |  |  |  |
| `HOUR` | `varchar(96)` | NO |  |  |  |
| `DAY_OF_WEEK` | `varchar(64)` | NO |  |  |  |
| `DAY_OF_MONTH` | `varchar(124)` | NO |  |  |  |
| `MONTH_OF_YEAR` | `varchar(64)` | NO |  |  |  |
| `TIMEZONE` | `varchar(63)` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_INTERVALSCHEDULE`

- **PK:** `ID` (`django_celery_beat_intervalschedule_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `EVERY` | `int` | NO |  |  |  |
| `PERIOD` | `varchar(24)` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_PERIODICTASK`

- **PK:** `ID` (`django_celery_beat_periodictask_pkey`)

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

#### `DJANGO_CELERY_BEAT_PERIODICTASKS`

- **PK:** `IDENT` (`django_celery_beat_periodictasks_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `IDENT` | `int` | NO | ✅ |  |  |
| `LAST_UPDATE` | `timestamp` | NO |  |  |  |

#### `DJANGO_CELERY_BEAT_SOLARSCHEDULE`

- **PK:** `ID` (`django_celery_beat_solarschedule_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `EVENT` | `varchar(24)` | NO |  |  |  |
| `LATITUDE` | `numeric(9, 6)` | NO |  |  |  |
| `LONGITUDE` | `numeric(9, 6)` | NO |  |  |  |

#### `DJANGO_CELERY_RESULTS_CHORDCOUNTER`

- **PK:** `ID` (`django_celery_results_chordcounter_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `varchar(255)` | NO |  |  |  |
| `SUB_TASKS` | `text` | NO |  |  |  |
| `COUNT` | `int` | NO |  |  |  |

#### `DJANGO_CELERY_RESULTS_GROUPRESULT`

- **PK:** `ID` (`django_celery_results_groupresult_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `GROUP_ID` | `varchar(255)` | NO |  |  |  |
| `DATE_CREATED` | `timestamp` | NO |  |  |  |
| `DATE_DONE` | `timestamp` | NO |  |  |  |
| `CONTENT_TYPE` | `varchar(128)` | NO |  |  |  |
| `CONTENT_ENCODING` | `varchar(64)` | NO |  |  |  |
| `RESULT` | `text` | YES |  |  |  |

#### `DJANGO_CELERY_RESULTS_TASKRESULT`

- **PK:** `ID` (`django_celery_results_taskresult_pkey`)

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

#### `DJANGO_CONTENT_TYPE`

- **PK:** `ID` (`django_content_type_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `APP_LABEL` | `varchar(100)` | NO |  |  |  |
| `MODEL` | `varchar(100)` | NO |  |  |  |

#### `DJANGO_MIGRATIONS`

- **PK:** `ID` (`django_migrations_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `APP` | `varchar(255)` | NO |  |  |  |
| `NAME` | `varchar(255)` | NO |  |  |  |
| `APPLIED` | `timestamp` | NO |  |  |  |

#### `DJANGO_SESSION`

- **PK:** `SESSION_KEY` (`django_session_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `SESSION_KEY` | `varchar(40)` | NO | ✅ |  |  |
| `SESSION_DATA` | `text` | NO |  |  |  |
| `EXPIRE_DATE` | `timestamp` | NO |  |  |  |

#### `DOCUMENTOS`

- **PK:** `ID` (`documentos_pkey`)

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

#### `DOCUMENTOS_DOCUMENTOEVENT`

- **PK:** `PGH_ID` (`documentos_documentoevent_pkey`)

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

#### `DOCUMENTOS_ROTULOEVENT`

- **PK:** `PGH_ID` (`documentos_rotuloevent_pkey`)

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

#### `DOCUMENTOS_TIPODOCUMENTOEVENT`

- **PK:** `PGH_ID` (`documentos_tipodocumentoevent_pkey`)

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

#### `DOCUMENTO_ROTULO`

- **PK:** `ID` (`documento_rotulo_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DOCUMENTO_ID` | `int` | NO |  |  |  |
| `ROTULO_ID` | `int` | NO |  |  |  |

#### `EMPRESAS`

- **PK:** `ID` (`empresas_pkey`)

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

#### `EMPRESAS_EMPRESAEVENT`

- **PK:** `PGH_ID` (`empresas_empresaevent_pkey`)

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

#### `EMPRESAS_ENDERECOEVENT`

- **PK:** `PGH_ID` (`empresas_enderecoevent_pkey`)

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

#### `EMPRESAS_SOCIOADMINISTRADOREVENT`

- **PK:** `PGH_ID` (`empresas_socioadministradorevent_pkey`)

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

#### `EMPRESA_SOCIOS`

- **PK:** `ID` (`empresa_socios_pkey`)

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

#### `ENDERECOS`

- **PK:** `ID` (`enderecos_pkey`)

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

#### `EQUIPAMENTOS`

- **PK:** `ID` (`equipamentos_pkey`)

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

#### `ESTOQUE_CATEGORIAITEMEVENT`

- **PK:** `PGH_ID` (`estoque_categoriaitemevent_pkey`)

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

#### `ESTOQUE_EQUIPAMENTOEVENT`

- **PK:** `PGH_ID` (`estoque_equipamentoevent_pkey`)

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

#### `ESTOQUE_FERRAMENTAEVENT`

- **PK:** `PGH_ID` (`estoque_ferramentaevent_pkey`)

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

#### `ESTOQUE_MATERIALEVENT`

- **PK:** `PGH_ID` (`estoque_materialevent_pkey`)

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

#### `ESTOQUE_UNIDADEMEDIDAEVENT`

- **PK:** `PGH_ID` (`estoque_unidademedidaevent_pkey`)

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

#### `ESTOQUE_VEICULOEVENT`

- **PK:** `PGH_ID` (`estoque_veiculoevent_pkey`)

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

#### `FERRAMENTAS`

- **PK:** `ID` (`ferramentas_pkey`)

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

#### `FINANCEIRO_TRANSACAOCONTRATOEVENT`

- **PK:** `PGH_ID` (`financeiro_transacaocontratoevent_pkey`)

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

#### `FUNCIONARIOS`

- **PK:** `ID` (`funcionarios_pkey`)

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

#### `FUNCIONARIO_CONTRATO`

- **PK:** `ID` (`funcionario_contrato_pkey`)

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

#### `FUNCIONARIO_MOVIMENTO`

- **PK:** `ID` (`funcionario_movimento_pkey`)

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

#### `FUNCIONARIO_PERMISSAO`

- **PK:** `ID` (`funcionario_permissao_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `CONCEDIDO_POR_ID` | `int` | YES |  |  |  |
| `FUNCIONARIO_ID` | `int` | NO |  |  |  |
| `PERMISSAO_ID` | `int` | NO |  |  |  |

#### `GRUPO_PERMISSOES`

- **PK:** `ID` (`grupo_permissoes_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |

#### `GRUPO_PERMISSOES_PERMISSOES`

- **PK:** `ID` (`grupo_permissoes_permissoes_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `GRUPOPERMISSAO_ID` | `int` | NO |  |  |  |
| `PERMISSAO_ID` | `int` | NO |  |  |  |

#### `ITEM_AVALIACAO`

- **PK:** `ID` (`item_avaliacao_pkey`)

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

#### `ITEM_ROTULO`

- **PK:** `ID` (`item_rotulo_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `ITEM_TIPO` | `varchar(20)` | NO |  |  |  |
| `ITEM_ID` | `int` | NO |  |  |  |
| `ROTULO_ID` | `int` | NO |  |  |  |

#### `KANBAN_ATIVIDADE_CONCLUIDA`

- **PK:** `ID` (`kanban_atividade_concluida_pkey`)

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

#### `KANBAN_CARD`

- **PK:** `ID` (`kanban_card_pkey`)

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

#### `KANBAN_CARD_RESPONSAVEIS`

- **PK:** `ID` (`kanban_card_responsaveis_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `KANBANCARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `KANBAN_KANBANATIVIDADECONCLUIDAEVENT`

- **PK:** `PGH_ID` (`kanban_kanbanatividadeconcluidaevent_pkey`)

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

#### `KANBAN_KANBANCARDEVENT`

- **PK:** `PGH_ID` (`kanban_kanbancardevent_pkey`)

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

#### `KANBAN_KANBANOBSERVACAOEVENT`

- **PK:** `PGH_ID` (`kanban_kanbanobservacaoevent_pkey`)

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

#### `KANBAN_KANBANQUADROEVENT`

- **PK:** `PGH_ID` (`kanban_kanbanquadroevent_pkey`)

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

#### `KANBAN_MOVIMENTO`

- **PK:** `ID` (`kanban_movimento_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DE_COLUNA` | `varchar(50)` | NO |  |  |  |
| `PARA_COLUNA` | `varchar(50)` | NO |  |  |  |
| `DATA_MOVIMENTO` | `timestamp` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `KANBAN_OBSERVACAO`

- **PK:** `ID` (`kanban_observacao_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `TEXTO` | `text` | NO |  |  |  |
| `CARD_ID` | `int` | NO |  |  |  |
| `USUARIO_ID` | `int` | NO |  |  |  |

#### `KANBAN_QUADRO`

- **PK:** `ID` (`kanban_quadro_pkey`)

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

#### `MATERIAIS`

- **PK:** `ID` (`materiais_pkey`)

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

#### `MOVIMENTACAO_ESTOQUE`

- **PK:** `ID` (`movimentacao_estoque_pkey`)

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

#### `MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT`

- **PK:** `PGH_ID` (`movimentacoes_movimentacaoestoqueevent_pkey`)

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

#### `MOVIMENTACOES_TIPOMOVIMENTACAOEVENT`

- **PK:** `PGH_ID` (`movimentacoes_tipomovimentacaoevent_pkey`)

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

#### `NOTIFICACOES`

- **PK:** `ID` (`notificacoes_pkey`)

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

#### `NOTIFICACOES_GRUPOPERMISSAOEVENT`

- **PK:** `PGH_ID` (`notificacoes_grupopermissaoevent_pkey`)

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

#### `NOTIFICACOES_NOTIFICACAOEVENT`

- **PK:** `PGH_ID` (`notificacoes_notificacaoevent_pkey`)

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

#### `NOTIFICACOES_PERMISSAOEVENT`

- **PK:** `PGH_ID` (`notificacoes_permissaoevent_pkey`)

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

#### `PERMISSOES`

- **PK:** `ID` (`permissoes_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `RECURSO` | `varchar(100)` | NO |  |  |  |
| `ACAO` | `varchar(50)` | NO |  |  |  |

#### `PESSOAS`

- **PK:** `ID` (`pessoas_pkey`)

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

#### `PESSOAS_FUNCIONARIOEVENT`

- **PK:** `PGH_ID` (`pessoas_funcionarioevent_pkey`)

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

#### `PESSOAS_PESSOAEVENT`

- **PK:** `PGH_ID` (`pessoas_pessoaevent_pkey`)

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

#### `PGHISTORY_CONTEXT`

- **PK:** `ID` (`pghistory_context_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |

#### `RELATORIOS_RELATORIOVISITAEVENT`

- **PK:** `PGH_ID` (`relatorios_relatoriovisitaevent_pkey`)

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

#### `RELATORIOS_TIPORELATORIOEVENT`

- **PK:** `PGH_ID` (`relatorios_tiporelatorioevent_pkey`)

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

#### `RELATORIO_VISITA`

- **PK:** `ID` (`relatorio_visita_pkey`)

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

#### `ROTULOS`

- **PK:** `ID` (`rotulos_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `STATUS`

- **PK:** `ID` (`status_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `STATUS` | `varchar(50)` | NO |  |  |  |
| `OBSERVACAO` | `text` | NO |  |  |  |

#### `TIPO_DOCUMENTO`

- **PK:** `ID` (`tipo_documento_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SLUG` | `varchar(50)` | NO |  |  |  |

#### `TIPO_MOVIMENTACAO`

- **PK:** `ID` (`tipo_movimentacao_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(100)` | NO |  |  |  |
| `NATUREZA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `text` | NO |  |  |  |

#### `TIPO_RELATORIO`

- **PK:** `ID` (`tipo_relatorio_pkey`)

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

#### `TOKEN_BLACKLIST_BLACKLISTEDTOKEN`

- **PK:** `ID` (`token_blacklist_blacklistedtoken_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `BLACKLISTED_AT` | `timestamp` | NO |  |  |  |
| `TOKEN_ID` | `int` | NO |  |  |  |

#### `TOKEN_BLACKLIST_OUTSTANDINGTOKEN`

- **PK:** `ID` (`token_blacklist_outstandingtoken_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `TOKEN` | `text` | NO |  |  |  |
| `CREATED_AT` | `timestamp` | YES |  |  |  |
| `EXPIRES_AT` | `timestamp` | NO |  |  |  |
| `USER_ID` | `int` | YES |  |  |  |
| `JTI` | `varchar(255)` | NO |  |  |  |

#### `TRANSACAO_CONTRATO`

- **PK:** `ID` (`transacao_contrato_pkey`)

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

#### `UNIDADE_MEDIDA`

- **PK:** `ID` (`unidade_medida_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `DELETED_AT` | `timestamp` | YES |  |  |  |
| `CREATED_AT` | `timestamp` | NO |  |  |  |
| `UPDATED_AT` | `timestamp` | NO |  |  |  |
| `NOME` | `varchar(50)` | NO |  |  |  |
| `SIGLA` | `varchar(10)` | NO |  |  |  |
| `DESCRICAO` | `varchar(200)` | NO |  |  |  |

#### `USUARIOS`

- **PK:** `ID` (`usuarios_pkey`)

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

#### `USUARIOS_GROUPS`

- **PK:** `ID` (`usuarios_groups_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `GROUP_ID` | `int` | NO |  |  |  |

#### `USUARIOS_USER_PERMISSIONS`

- **PK:** `ID` (`usuarios_user_permissions_pkey`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `ID` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `USUARIO_ID` | `int` | NO |  |  |  |
| `PERMISSION_ID` | `int` | NO |  |  |  |

#### `USUARIOS_USUARIOEVENT`

- **PK:** `PGH_ID` (`usuarios_usuarioevent_pkey`)

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

#### `VEICULOS`

- **PK:** `ID` (`veiculos_pkey`)

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

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `ANEXO_RELATORIO` | `anexo_relatorio_pkey` | `ID` |
| `AUTH_GROUP` | `auth_group_pkey` | `ID` |
| `AUTH_GROUP_PERMISSIONS` | `auth_group_permissions_pkey` | `ID` |
| `AUTH_PERMISSION` | `auth_permission_pkey` | `ID` |
| `AVALIACAO_ITEM` | `avaliacao_item_pkey` | `ID` |
| `AVALIACOES` | `avaliacoes_pkey` | `ID` |
| `AVALIACOES_AVALIACAOEVENT` | `avaliacoes_avaliacaoevent_pkey` | `PGH_ID` |
| `AVALIACOES_ITEMAVALIACAOEVENT` | `avaliacoes_itemavaliacaoevent_pkey` | `PGH_ID` |
| `CATEGORIA_ITEM` | `categoria_item_pkey` | `ID` |
| `CONTRATOS` | `contratos_pkey` | `ID` |
| `CONTRATOS_CONTRATOEVENT` | `contratos_contratoevent_pkey` | `PGH_ID` |
| `CONTRATOS_FUNCIONARIOCONTRATOEVENT` | `contratos_funcionariocontratoevent_pkey` | `PGH_ID` |
| `CONTRATOS_FUNCIONARIOMOVIMENTOEVENT` | `contratos_funcionariomovimentoevent_pkey` | `PGH_ID` |
| `CONTRATOS_STATUSEVENT` | `contratos_statusevent_pkey` | `PGH_ID` |
| `CONTRATO_ITEM_ALOCADO` | `contrato_item_alocado_pkey` | `ID` |
| `DJANGO_ADMIN_LOG` | `django_admin_log_pkey` | `ID` |
| `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE` | `django_celery_beat_clockedschedule_pkey` | `ID` |
| `DJANGO_CELERY_BEAT_CRONTABSCHEDULE` | `django_celery_beat_crontabschedule_pkey` | `ID` |
| `DJANGO_CELERY_BEAT_INTERVALSCHEDULE` | `django_celery_beat_intervalschedule_pkey` | `ID` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `django_celery_beat_periodictask_pkey` | `ID` |
| `DJANGO_CELERY_BEAT_PERIODICTASKS` | `django_celery_beat_periodictasks_pkey` | `IDENT` |
| `DJANGO_CELERY_BEAT_SOLARSCHEDULE` | `django_celery_beat_solarschedule_pkey` | `ID` |
| `DJANGO_CELERY_RESULTS_CHORDCOUNTER` | `django_celery_results_chordcounter_pkey` | `ID` |
| `DJANGO_CELERY_RESULTS_GROUPRESULT` | `django_celery_results_groupresult_pkey` | `ID` |
| `DJANGO_CELERY_RESULTS_TASKRESULT` | `django_celery_results_taskresult_pkey` | `ID` |
| `DJANGO_CONTENT_TYPE` | `django_content_type_pkey` | `ID` |
| `DJANGO_MIGRATIONS` | `django_migrations_pkey` | `ID` |
| `DJANGO_SESSION` | `django_session_pkey` | `SESSION_KEY` |
| `DOCUMENTOS` | `documentos_pkey` | `ID` |
| `DOCUMENTOS_DOCUMENTOEVENT` | `documentos_documentoevent_pkey` | `PGH_ID` |
| `DOCUMENTOS_ROTULOEVENT` | `documentos_rotuloevent_pkey` | `PGH_ID` |
| `DOCUMENTOS_TIPODOCUMENTOEVENT` | `documentos_tipodocumentoevent_pkey` | `PGH_ID` |
| `DOCUMENTO_ROTULO` | `documento_rotulo_pkey` | `ID` |
| `EMPRESAS` | `empresas_pkey` | `ID` |
| `EMPRESAS_EMPRESAEVENT` | `empresas_empresaevent_pkey` | `PGH_ID` |
| `EMPRESAS_ENDERECOEVENT` | `empresas_enderecoevent_pkey` | `PGH_ID` |
| `EMPRESAS_SOCIOADMINISTRADOREVENT` | `empresas_socioadministradorevent_pkey` | `PGH_ID` |
| `EMPRESA_SOCIOS` | `empresa_socios_pkey` | `ID` |
| `ENDERECOS` | `enderecos_pkey` | `ID` |
| `EQUIPAMENTOS` | `equipamentos_pkey` | `ID` |
| `ESTOQUE_CATEGORIAITEMEVENT` | `estoque_categoriaitemevent_pkey` | `PGH_ID` |
| `ESTOQUE_EQUIPAMENTOEVENT` | `estoque_equipamentoevent_pkey` | `PGH_ID` |
| `ESTOQUE_FERRAMENTAEVENT` | `estoque_ferramentaevent_pkey` | `PGH_ID` |
| `ESTOQUE_MATERIALEVENT` | `estoque_materialevent_pkey` | `PGH_ID` |
| `ESTOQUE_UNIDADEMEDIDAEVENT` | `estoque_unidademedidaevent_pkey` | `PGH_ID` |
| `ESTOQUE_VEICULOEVENT` | `estoque_veiculoevent_pkey` | `PGH_ID` |
| `FERRAMENTAS` | `ferramentas_pkey` | `ID` |
| `FINANCEIRO_TRANSACAOCONTRATOEVENT` | `financeiro_transacaocontratoevent_pkey` | `PGH_ID` |
| `FUNCIONARIOS` | `funcionarios_pkey` | `ID` |
| `FUNCIONARIO_CONTRATO` | `funcionario_contrato_pkey` | `ID` |
| `FUNCIONARIO_MOVIMENTO` | `funcionario_movimento_pkey` | `ID` |
| `FUNCIONARIO_PERMISSAO` | `funcionario_permissao_pkey` | `ID` |
| `GRUPO_PERMISSOES` | `grupo_permissoes_pkey` | `ID` |
| `GRUPO_PERMISSOES_PERMISSOES` | `grupo_permissoes_permissoes_pkey` | `ID` |
| `ITEM_AVALIACAO` | `item_avaliacao_pkey` | `ID` |
| `ITEM_ROTULO` | `item_rotulo_pkey` | `ID` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `kanban_atividade_concluida_pkey` | `ID` |
| `KANBAN_CARD` | `kanban_card_pkey` | `ID` |
| `KANBAN_CARD_RESPONSAVEIS` | `kanban_card_responsaveis_pkey` | `ID` |
| `KANBAN_KANBANATIVIDADECONCLUIDAEVENT` | `kanban_kanbanatividadeconcluidaevent_pkey` | `PGH_ID` |
| `KANBAN_KANBANCARDEVENT` | `kanban_kanbancardevent_pkey` | `PGH_ID` |
| `KANBAN_KANBANOBSERVACAOEVENT` | `kanban_kanbanobservacaoevent_pkey` | `PGH_ID` |
| `KANBAN_KANBANQUADROEVENT` | `kanban_kanbanquadroevent_pkey` | `PGH_ID` |
| `KANBAN_MOVIMENTO` | `kanban_movimento_pkey` | `ID` |
| `KANBAN_OBSERVACAO` | `kanban_observacao_pkey` | `ID` |
| `KANBAN_QUADRO` | `kanban_quadro_pkey` | `ID` |
| `MATERIAIS` | `materiais_pkey` | `ID` |
| `MOVIMENTACAO_ESTOQUE` | `movimentacao_estoque_pkey` | `ID` |
| `MOVIMENTACOES_MOVIMENTACAOESTOQUEEVENT` | `movimentacoes_movimentacaoestoqueevent_pkey` | `PGH_ID` |
| `MOVIMENTACOES_TIPOMOVIMENTACAOEVENT` | `movimentacoes_tipomovimentacaoevent_pkey` | `PGH_ID` |
| `NOTIFICACOES` | `notificacoes_pkey` | `ID` |
| `NOTIFICACOES_GRUPOPERMISSAOEVENT` | `notificacoes_grupopermissaoevent_pkey` | `PGH_ID` |
| `NOTIFICACOES_NOTIFICACAOEVENT` | `notificacoes_notificacaoevent_pkey` | `PGH_ID` |
| `NOTIFICACOES_PERMISSAOEVENT` | `notificacoes_permissaoevent_pkey` | `PGH_ID` |
| `PERMISSOES` | `permissoes_pkey` | `ID` |
| `PESSOAS` | `pessoas_pkey` | `ID` |
| `PESSOAS_FUNCIONARIOEVENT` | `pessoas_funcionarioevent_pkey` | `PGH_ID` |
| `PESSOAS_PESSOAEVENT` | `pessoas_pessoaevent_pkey` | `PGH_ID` |
| `PGHISTORY_CONTEXT` | `pghistory_context_pkey` | `ID` |
| `RELATORIOS_RELATORIOVISITAEVENT` | `relatorios_relatoriovisitaevent_pkey` | `PGH_ID` |
| `RELATORIOS_TIPORELATORIOEVENT` | `relatorios_tiporelatorioevent_pkey` | `PGH_ID` |
| `RELATORIO_VISITA` | `relatorio_visita_pkey` | `ID` |
| `ROTULOS` | `rotulos_pkey` | `ID` |
| `STATUS` | `status_pkey` | `ID` |
| `TIPO_DOCUMENTO` | `tipo_documento_pkey` | `ID` |
| `TIPO_MOVIMENTACAO` | `tipo_movimentacao_pkey` | `ID` |
| `TIPO_RELATORIO` | `tipo_relatorio_pkey` | `ID` |
| `TOKEN_BLACKLIST_BLACKLISTEDTOKEN` | `token_blacklist_blacklistedtoken_pkey` | `ID` |
| `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `token_blacklist_outstandingtoken_pkey` | `ID` |
| `TRANSACAO_CONTRATO` | `transacao_contrato_pkey` | `ID` |
| `UNIDADE_MEDIDA` | `unidade_medida_pkey` | `ID` |
| `USUARIOS` | `usuarios_pkey` | `ID` |
| `USUARIOS_GROUPS` | `usuarios_groups_pkey` | `ID` |
| `USUARIOS_USER_PERMISSIONS` | `usuarios_user_permissions_pkey` | `ID` |
| `USUARIOS_USUARIOEVENT` | `usuarios_usuarioevent_pkey` | `PGH_ID` |
| `VEICULOS` | `veiculos_pkey` | `ID` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `ANEXO_RELATORIO` | `ENVIADO_POR_ID` | `FUNCIONARIOS` | `ID` | `anexo_relatorio_enviado_por_id_ba0a79c0_fk_funcionarios_id` |
| `ANEXO_RELATORIO` | `RELATORIO_ID` | `RELATORIO_VISITA` | `ID` | `anexo_relatorio_relatorio_id_41de4f28_fk_relatorio_visita_id` |
| `AUTH_GROUP_PERMISSIONS` | `PERMISSION_ID` | `AUTH_PERMISSION` | `ID` | `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` |
| `AUTH_GROUP_PERMISSIONS` | `GROUP_ID` | `AUTH_GROUP` | `ID` | `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` |
| `AUTH_PERMISSION` | `CONTENT_TYPE_ID` | `DJANGO_CONTENT_TYPE` | `ID` | `auth_permission_content_type_id_2f476e4b_fk_django_co` |
| `AVALIACAO_ITEM` | `AVALIACAO_ID` | `AVALIACOES` | `ID` | `avaliacao_item_avaliacao_id_cd3264f4_fk_avaliacoes_id` |
| `AVALIACAO_ITEM` | `ITEM_AVALIACAO_ID` | `ITEM_AVALIACAO` | `ID` | `avaliacao_item_item_avaliacao_id_6ea3b81b_fk_item_avaliacao_id` |
| `AVALIACOES` | `AVALIADOR_ID` | `PESSOAS` | `ID` | `avaliacoes_avaliador_id_45cc8a45_fk_pessoas_id` |
| `AVALIACOES` | `RATIFICADOR_ID` | `PESSOAS` | `ID` | `avaliacoes_ratificador_id_f050c022_fk_pessoas_id` |
| `CONTRATOS` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `contratos_empresa_id_7a23f8cb_fk_empresas_id` |
| `CONTRATOS` | `GESTOR_RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `contratos_gestor_responsavel_id_f34999a6_fk_funcionarios_id` |
| `CONTRATOS` | `LOCAL_EXECUCAO_ID` | `ENDERECOS` | `ID` | `contratos_local_execucao_id_51882e4d_fk_enderecos_id` |
| `CONTRATOS` | `STATUS_ID` | `STATUS` | `ID` | `contratos_status_id_fb9ba518_fk_status_id` |
| `CONTRATO_ITEM_ALOCADO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `contrato_item_alocado_contrato_id_c66d331b_fk_contratos_id` |
| `DJANGO_ADMIN_LOG` | `CONTENT_TYPE_ID` | `DJANGO_CONTENT_TYPE` | `ID` | `django_admin_log_content_type_id_c4bce8eb_fk_django_co` |
| `DJANGO_ADMIN_LOG` | `USER_ID` | `USUARIOS` | `ID` | `django_admin_log_user_id_c564eba6_fk_usuarios_id` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `CLOCKED_ID` | `DJANGO_CELERY_BEAT_CLOCKEDSCHEDULE` | `ID` | `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `CRONTAB_ID` | `DJANGO_CELERY_BEAT_CRONTABSCHEDULE` | `ID` | `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `INTERVAL_ID` | `DJANGO_CELERY_BEAT_INTERVALSCHEDULE` | `ID` | `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` |
| `DJANGO_CELERY_BEAT_PERIODICTASK` | `SOLAR_ID` | `DJANGO_CELERY_BEAT_SOLARSCHEDULE` | `ID` | `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` |
| `DOCUMENTOS` | `CREATED_BY_ID` | `FUNCIONARIOS` | `ID` | `documentos_created_by_id_6ce1c352_fk_funcionarios_id` |
| `DOCUMENTOS` | `TIPO_DOCUMENTO_ID` | `TIPO_DOCUMENTO` | `ID` | `documentos_tipo_documento_id_bb661ba3_fk_tipo_documento_id` |
| `DOCUMENTO_ROTULO` | `DOCUMENTO_ID` | `DOCUMENTOS` | `ID` | `documento_rotulo_documento_id_b68c8743_fk_documentos_id` |
| `DOCUMENTO_ROTULO` | `ROTULO_ID` | `ROTULOS` | `ID` | `documento_rotulo_rotulo_id_b428c401_fk_rotulos_id` |
| `EMPRESAS` | `ENDERECO_ID` | `ENDERECOS` | `ID` | `empresas_endereco_id_ce47b5ff_fk_enderecos_id` |
| `EMPRESA_SOCIOS` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `empresa_socios_empresa_id_53a6d4ed_fk_empresas_id` |
| `EMPRESA_SOCIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `empresa_socios_pessoa_id_a513d917_fk_pessoas_id` |
| `EQUIPAMENTOS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `equipamentos_categoria_id_a9274919_fk_categoria_item_id` |
| `EQUIPAMENTOS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `equipamentos_unidade_medida_id_fa020088_fk_unidade_medida_id` |
| `FERRAMENTAS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `ferramentas_categoria_id_3b419683_fk_categoria_item_id` |
| `FERRAMENTAS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `ferramentas_unidade_medida_id_5a83d675_fk_unidade_medida_id` |
| `FUNCIONARIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `funcionarios_pessoa_id_1e1211c6_fk_pessoas_id` |
| `FUNCIONARIO_CONTRATO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `funcionario_contrato_contrato_id_5bdcdb13_fk_contratos_id` |
| `FUNCIONARIO_CONTRATO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `funcionario_contrato_funcionario_id_7e02e8d4_fk_funcionarios_id` |
| `FUNCIONARIO_MOVIMENTO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `funcionario_moviment_funcionario_id_1fc836e7_fk_funcionar` |
| `FUNCIONARIO_MOVIMENTO` | `CREATED_BY_ID` | `FUNCIONARIOS` | `ID` | `funcionario_movimento_created_by_id_367a195c_fk_funcionarios_id` |
| `FUNCIONARIO_MOVIMENTO` | `DE_CONTRATO_ID` | `CONTRATOS` | `ID` | `funcionario_movimento_de_contrato_id_af9d8bf9_fk_contratos_id` |
| `FUNCIONARIO_MOVIMENTO` | `PARA_CONTRATO_ID` | `CONTRATOS` | `ID` | `funcionario_movimento_para_contrato_id_10426c41_fk_contratos_id` |
| `FUNCIONARIO_PERMISSAO` | `CONCEDIDO_POR_ID` | `FUNCIONARIOS` | `ID` | `funcionario_permissa_concedido_por_id_ea8b4963_fk_funcionar` |
| `FUNCIONARIO_PERMISSAO` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `funcionario_permissa_funcionario_id_dc9f3230_fk_funcionar` |
| `FUNCIONARIO_PERMISSAO` | `PERMISSAO_ID` | `PERMISSOES` | `ID` | `funcionario_permissao_permissao_id_87336c7b_fk_permissoes_id` |
| `GRUPO_PERMISSOES_PERMISSOES` | `GRUPOPERMISSAO_ID` | `GRUPO_PERMISSOES` | `ID` | `grupo_permissoes_per_grupopermissao_id_b6817939_fk_grupo_per` |
| `GRUPO_PERMISSOES_PERMISSOES` | `PERMISSAO_ID` | `PERMISSOES` | `ID` | `grupo_permissoes_per_permissao_id_6418902f_fk_permissoe` |
| `ITEM_ROTULO` | `ROTULO_ID` | `ROTULOS` | `ID` | `item_rotulo_rotulo_id_da37d665_fk_rotulos_id` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `CARD_ID` | `KANBAN_CARD` | `ID` | `kanban_atividade_concluida_card_id_bee61dc1_fk_kanban_card_id` |
| `KANBAN_ATIVIDADE_CONCLUIDA` | `USUARIO_ID` | `USUARIOS` | `ID` | `kanban_atividade_concluida_usuario_id_d83278c2_fk_usuarios_id` |
| `KANBAN_CARD` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `kanban_card_contrato_id_458a161b_fk_contratos_id` |
| `KANBAN_CARD` | `CRIADO_POR_ID` | `USUARIOS` | `ID` | `kanban_card_criado_por_id_291ae5e7_fk_usuarios_id` |
| `KANBAN_CARD` | `FUNCIONARIO_ID` | `FUNCIONARIOS` | `ID` | `kanban_card_funcionario_id_295df478_fk_funcionarios_id` |
| `KANBAN_CARD` | `QUADRO_ID` | `KANBAN_QUADRO` | `ID` | `kanban_card_quadro_id_a101eeb3_fk_kanban_quadro_id` |
| `KANBAN_CARD_RESPONSAVEIS` | `KANBANCARD_ID` | `KANBAN_CARD` | `ID` | `kanban_card_responsa_kanbancard_id_1f8f2100_fk_kanban_ca` |
| `KANBAN_CARD_RESPONSAVEIS` | `USUARIO_ID` | `USUARIOS` | `ID` | `kanban_card_responsaveis_usuario_id_6c144e62_fk_usuarios_id` |
| `KANBAN_MOVIMENTO` | `CARD_ID` | `KANBAN_CARD` | `ID` | `kanban_movimento_card_id_823bbf8d_fk_kanban_card_id` |
| `KANBAN_MOVIMENTO` | `USUARIO_ID` | `USUARIOS` | `ID` | `kanban_movimento_usuario_id_81ca9982_fk_usuarios_id` |
| `KANBAN_OBSERVACAO` | `CARD_ID` | `KANBAN_CARD` | `ID` | `kanban_observacao_card_id_b09a0c7a_fk_kanban_card_id` |
| `KANBAN_OBSERVACAO` | `USUARIO_ID` | `USUARIOS` | `ID` | `kanban_observacao_usuario_id_caf6ec6c_fk_usuarios_id` |
| `KANBAN_QUADRO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `kanban_quadro_contrato_id_26dc9a1c_fk_contratos_id` |
| `KANBAN_QUADRO` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `kanban_quadro_empresa_id_256b898d_fk_empresas_id` |
| `MATERIAIS` | `CATEGORIA_ID` | `CATEGORIA_ITEM` | `ID` | `materiais_categoria_id_ee883d56_fk_categoria_item_id` |
| `MATERIAIS` | `UNIDADE_MEDIDA_ID` | `UNIDADE_MEDIDA` | `ID` | `materiais_unidade_medida_id_a54a9d6b_fk_unidade_medida_id` |
| `MOVIMENTACAO_ESTOQUE` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `movimentacao_estoque_contrato_id_b8368648_fk_contratos_id` |
| `MOVIMENTACAO_ESTOQUE` | `RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `movimentacao_estoque_responsavel_id_0b964e29_fk_funcionarios_id` |
| `MOVIMENTACAO_ESTOQUE` | `TIPO_MOVIMENTACAO_ID` | `TIPO_MOVIMENTACAO` | `ID` | `movimentacao_estoque_tipo_movimentacao_id_95bd7650_fk_tipo_movi` |
| `NOTIFICACOES` | `DESTINATARIO_ID` | `FUNCIONARIOS` | `ID` | `notificacoes_destinatario_id_91f2a446_fk_funcionarios_id` |
| `PESSOAS` | `ENDERECO_ID` | `ENDERECOS` | `ID` | `pessoas_endereco_id_758f075e_fk_enderecos_id` |
| `RELATORIO_VISITA` | `EMPRESA_ID` | `EMPRESAS` | `ID` | `relatorio_visita_empresa_id_01129847_fk_empresas_id` |
| `RELATORIO_VISITA` | `RESPONSAVEL_ID` | `FUNCIONARIOS` | `ID` | `relatorio_visita_responsavel_id_ee034725_fk_funcionarios_id` |
| `RELATORIO_VISITA` | `TIPO_RELATORIO_ID` | `TIPO_RELATORIO` | `ID` | `relatorio_visita_tipo_relatorio_id_54a6d546_fk_tipo_rela` |
| `TOKEN_BLACKLIST_BLACKLISTEDTOKEN` | `TOKEN_ID` | `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `ID` | `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` |
| `TOKEN_BLACKLIST_OUTSTANDINGTOKEN` | `USER_ID` | `USUARIOS` | `ID` | `token_blacklist_outs_user_id_83bc629a_fk_usuarios_` |
| `TRANSACAO_CONTRATO` | `CONTRATO_ID` | `CONTRATOS` | `ID` | `transacao_contrato_contrato_id_ceaf0fff_fk_contratos_id` |
| `USUARIOS` | `PESSOA_ID` | `PESSOAS` | `ID` | `usuarios_pessoa_id_0331f0f2_fk_pessoas_id` |
| `USUARIOS_GROUPS` | `GROUP_ID` | `AUTH_GROUP` | `ID` | `usuarios_groups_group_id_18c61092_fk_auth_group_id` |
| `USUARIOS_GROUPS` | `USUARIO_ID` | `USUARIOS` | `ID` | `usuarios_groups_usuario_id_1132ca50_fk_usuarios_id` |
| `USUARIOS_USER_PERMISSIONS` | `PERMISSION_ID` | `AUTH_PERMISSION` | `ID` | `usuarios_user_permis_permission_id_af615ca1_fk_auth_perm` |
| `USUARIOS_USER_PERMISSIONS` | `USUARIO_ID` | `USUARIOS` | `ID` | `usuarios_user_permissions_usuario_id_232fd58d_fk_usuarios_id` |
| `VEICULOS` | `STATUS_ID` | `STATUS` | `ID` | `veiculos_status_id_5f131383_fk_status_id` |
