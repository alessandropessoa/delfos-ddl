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

#### `T_008B72D0`

- **PK:** `C_3843971D` (`K_48587f50`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_348DE53B` | `varchar(50)` | NO |  |  |  |
| `C_B671C40D` | `varchar(50)` | NO |  |  |  |
| `C_7D9B19F2` | `timestamp` | NO |  |  |  |
| `C_BF7FC51B` | `int` | NO |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |

#### `T_042FAD8B`

- **PK:** `C_3843971D` (`K_ecde6bf7`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_B7179FE7` | `varchar(255)` | NO |  |  |  |
| `C_EAA58932` | `varchar(255)` | NO |  |  |  |
| `C_79DFD370` | `timestamp` | NO |  |  |  |

#### `T_04EA3513`

- **PK:** `C_7DB37878` (`K_2bf410a8`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_08331B35`

- **PK:** `C_7DB37878` (`K_4223385c`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_1154AEDB` | `text` | NO |  |  |  |
| `C_BF7FC51B` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |

#### `T_0F02E5AB`

- **PK:** `C_7DB37878` (`K_6f071b23`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_0BE64AE8` | `varchar(128)` | NO |  |  |  |
| `C_E8820A9C` | `timestamp` | YES |  |  |  |
| `C_2BC362D1` | `varchar(150)` | NO |  |  |  |
| `C_2D87207D` | `varchar(150)` | NO |  |  |  |
| `C_6AD00525` | `varchar(150)` | NO |  |  |  |
| `C_72D90AF3` | `varchar(254)` | NO |  |  |  |
| `C_AE1ED986` | `timestamp` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_06B58CC4` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_110854C7`

- **PK:** `C_3843971D` (`K_eece3af5`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_BB7543F1` | `numeric(12, 2)` | NO |  |  |  |
| `C_E5F33DE1` | `date` | NO |  |  |  |
| `C_9A01ED69` | `date` | NO |  |  |  |
| `C_09FB9E4B` | `date` | YES |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_B7E9CDAB` | `int` | NO |  |  |  |
| `C_7EC8E5BB` | `int` | YES |  |  |  |
| `C_CEC71448` | `int` | NO |  |  |  |

#### `T_189FFA19`

- **PK:** `C_3843971D` (`K_71f6b911`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(200)` | NO |  |  |  |
| `C_9F84DB4F` | `text` | NO |  |  |  |
| `C_E26EF190` | `varchar(200)` | NO |  |  |  |
| `C_76E51CA4` | `int` | NO |  |  |  |

#### `T_195AE791`

- **PK:** `C_7DB37878` (`K_72bccbae`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_6F6C7E96` | `varchar(255)` | NO |  |  |  |
| `C_04C36512` | `varchar(100)` | NO |  |  |  |
| `C_047ECB51` | `varchar(50)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_BD0159B6` | `date` | YES |  |  |  |
| `C_E20FBEE5` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_5CE17026` | `int` | NO |  |  |  |

#### `T_1AB0BF01`

- **PK:** `C_7DB37878` (`K_4d9200ab`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A08D2777` | `varchar(20)` | NO |  |  |  |
| `C_D4E5C147` | `int` | NO |  |  |  |
| `C_2F2C1C01` | `numeric(12, 4)` | NO |  |  |  |
| `C_7D9B19F2` | `timestamp` | NO |  |  |  |
| `C_899F5890` | `varchar(255)` | NO |  |  |  |
| `C_2ADAB83F` | `varchar(255)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_97E46024` | `int` | NO |  |  |  |
| `C_035B8E23` | `int` | NO |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |

#### `T_1D285733`

- **PK:** `C_3843971D` (`K_b02aa7a6`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_7124DEA5` | `text` | NO |  |  |  |

#### `T_1DC445F1`

- **PK:** `C_3843971D` (`K_804b056a`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_02318D48` | `varchar(255)` | NO |  |  |  |
| `C_8BB9E366` | `varchar(20)` | NO |  |  |  |
| `C_E48ECE77` | `varchar(100)` | YES |  |  |  |
| `C_889529CA` | `varchar(100)` | NO |  |  |  |
| `C_2AE3E40A` | `varchar(100)` | NO |  |  |  |
| `C_F16FE7D4` | `varchar(2)` | NO |  |  |  |
| `C_D686368B` | `varchar(10)` | YES |  |  |  |
| `C_B74B28B5` | `varchar(50)` | NO |  |  |  |

#### `T_217033D7`

- **PK:** `C_3843971D` (`K_b5774642`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A43DB406` | `timestamp` | NO |  |  |  |
| `C_0C23F601` | `numeric(8, 2)` | YES |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |
| `C_BF7FC51B` | `int` | NO |  |  |  |

#### `T_2D92DC9D`

- **PK:** `C_3843971D` (`K_3b092f2a`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(50)` | NO |  |  |  |
| `C_901F61B2` | `varchar(10)` | NO |  |  |  |
| `C_D0B4D949` | `varchar(200)` | NO |  |  |  |

#### `T_2E5AC9DD`

- **PK:** `C_3843971D` (`K_6b4fde5b`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_EAA58932` | `varchar(150)` | NO |  |  |  |

#### `T_322CEC05`

- **PK:** `C_3843971D` (`K_235ff9cd`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_D3B6D19D` | `int` | NO |  |  |  |
| `C_2C05C5B9` | `varchar(24)` | NO |  |  |  |

#### `T_3452E3CE`

- **PK:** `C_3843971D` (`K_e540e302`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |

#### `T_361ECADA`

- **PK:** `C_3843971D` (`K_9162f6ec`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_5A4BA6AF` | `timestamp` | NO |  |  |  |
| `C_52FA508A` | `text` | YES |  |  |  |
| `C_FE9F0530` | `varchar(200)` | NO |  |  |  |
| `C_8C5185AA` | `int` | NO |  |  |  |
| `C_B9208E8B` | `text` | NO |  |  |  |
| `C_2CB7E946` | `int` | YES |  |  |  |
| `C_E5BB97D1` | `int` | NO |  |  |  |

#### `T_36D9977C`

- **PK:** `C_3843971D` (`K_d050bcaf`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_0BE64AE8` | `varchar(128)` | NO |  |  |  |
| `C_E8820A9C` | `timestamp` | YES |  |  |  |
| `C_2BC362D1` | `varchar(150)` | NO |  |  |  |
| `C_2D87207D` | `varchar(150)` | NO |  |  |  |
| `C_6AD00525` | `varchar(150)` | NO |  |  |  |
| `C_72D90AF3` | `varchar(254)` | NO |  |  |  |
| `C_AE1ED986` | `timestamp` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_06B58CC4` | `int` | YES |  |  |  |

#### `T_3C0F4574`

- **PK:** `C_7DB37878` (`K_51b912e2`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(50)` | NO |  |  |  |
| `C_901F61B2` | `varchar(10)` | NO |  |  |  |
| `C_D0B4D949` | `varchar(200)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_40D8A68B`

- **PK:** `C_7DB37878` (`K_94bd57e2`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_902C0FA2` | `date` | NO |  |  |  |
| `C_42B26E87` | `varchar(20)` | NO |  |  |  |
| `C_AE109891` | `int` | NO |  |  |  |
| `C_9EAE8E0D` | `numeric(5, 2)` | YES |  |  |  |
| `C_52007D21` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_FB759242` | `int` | YES |  |  |  |

#### `T_415214E3`

- **PK:** `C_3843971D` (`K_3d56e7c0`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_A0773D8D` | `varchar(100)` | NO |  |  |  |
| `C_4F844C00` | `varchar(50)` | NO |  |  |  |

#### `T_417C313C`

- **PK:** `C_3843971D` (`K_b35606ba`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_BD0159B6` | `date` | YES |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_41B9A0B9`

- **PK:** `C_96548987` (`K_40d2ab0e`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_96548987` | `varchar(40)` | NO | ✅ |  |  |
| `C_7E777A6F` | `text` | NO |  |  |  |
| `C_23885834` | `timestamp` | NO |  |  |  |

#### `T_429E6B85`

- **PK:** `C_3843971D` (`K_bab6ed82`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_71357FA2` | `varchar(100)` | YES |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_43C86CA7`

- **PK:** `C_7DB37878` (`K_9cd41fda`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(300)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_792E36F5` | `varchar(50)` | NO |  |  |  |
| `C_1B9EF054` | `int` | NO |  |  |  |
| `C_67F48386` | `date` | YES |  |  |  |
| `C_E5F33DE1` | `date` | YES |  |  |  |
| `C_A43DB406` | `date` | YES |  |  |  |
| `C_48286F17` | `varchar(20)` | NO |  |  |  |
| `C_4EBF96D0` | `numeric(6, 2)` | YES |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |
| `C_E95014A5` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_FC92A130` | `int` | NO |  |  |  |

#### `T_46761816`

- **PK:** `C_3843971D` (`K_9a8262f6`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |

#### `T_4FF564D3`

- **PK:** `C_3843971D` (`K_99e9fd34`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_35EEFC58` | `varchar(100)` | NO |  |  |  |
| `C_C8B6C094` | `varchar(100)` | NO |  |  |  |

#### `T_50CDAAFF`

- **PK:** `C_3843971D` (`K_1c58fc74`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_A08D2777` | `varchar(20)` | NO |  |  |  |
| `C_D4E5C147` | `int` | NO |  |  |  |
| `C_94BF01BE` | `int` | NO |  |  |  |

#### `T_51F27CE2`

- **PK:** `C_3843971D` (`K_635cffb6`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(50)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |

#### `T_57755815`

- **PK:** `C_7DB37878` (`K_9eb0557c`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_999EC7C5` | `varchar(50)` | NO |  |  |  |
| `C_D5E72980` | `date` | NO |  |  |  |
| `C_93928056` | `date` | YES |  |  |  |
| `C_6600003A` | `varchar(20)` | NO |  |  |  |
| `C_AFB4D893` | `numeric(6, 2)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_06B58CC4` | `int` | NO |  |  |  |

#### `T_5802694A`

- **PK:** `C_7DB37878` (`K_883b7676`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_CD4C8ECF` | `varchar(20)` | NO |  |  |  |
| `C_4F627600` | `numeric(5, 2)` | YES |  |  |  |
| `C_E5F33DE1` | `date` | NO |  |  |  |
| `C_9A01ED69` | `date` | YES |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_06B58CC4` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_58324603`

- **PK:** `C_7DB37878` (`K_fd1fbf4e`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_BB30FD48` | `varchar(200)` | NO |  |  |  |
| `C_291B360B` | `varchar(200)` | NO |  |  |  |
| `C_9D10D4E4` | `varchar(18)` | NO |  |  |  |
| `C_72D90AF3` | `varchar(255)` | NO |  |  |  |
| `C_8C7D47EE` | `varchar(20)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_6105EC46` | `int` | YES |  |  |  |

#### `T_5DA267DD`

- **PK:** `C_3843971D` (`K_8710a1db`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2FEAD22C` | `numeric(12, 2)` | NO |  |  |  |
| `C_7BC20718` | `numeric(12, 2)` | NO |  |  |  |
| `C_909F326B` | `numeric(12, 2)` | NO |  |  |  |
| `C_49658A0C` | `date` | NO |  |  |  |
| `C_24B44209` | `int` | NO |  |  |  |

#### `T_5FB11F7A`

- **PK:** `C_7DB37878` (`K_8b1f1a1f`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_BB7543F1` | `numeric(12, 2)` | NO |  |  |  |
| `C_E5F33DE1` | `date` | NO |  |  |  |
| `C_9A01ED69` | `date` | NO |  |  |  |
| `C_09FB9E4B` | `date` | YES |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_B7E9CDAB` | `int` | NO |  |  |  |
| `C_7EC8E5BB` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_CEC71448` | `int` | NO |  |  |  |

#### `T_6105DF1C`

- **PK:** `C_7DB37878` (`K_197491f5`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_7D9B19F2` | `date` | NO |  |  |  |
| `C_D4C800A6` | `text` | NO |  |  |  |
| `C_E20FBEE5` | `int` | YES |  |  |  |
| `C_52968FC9` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | NO |  |  |  |
| `C_A13D6A9F` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_6772EFBF`

- **PK:** `C_3843971D` (`K_b2a0a512`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_3C569425` | `numeric(5, 2)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_C5415C65` | `numeric(10, 2)` | YES |  |  |  |

#### `T_6C45B3AB`

- **PK:** `C_3843971D` (`K_8aea1854`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_902C0FA2` | `date` | NO |  |  |  |
| `C_42B26E87` | `varchar(20)` | NO |  |  |  |
| `C_AE109891` | `int` | NO |  |  |  |
| `C_9EAE8E0D` | `numeric(5, 2)` | YES |  |  |  |
| `C_52007D21` | `int` | NO |  |  |  |
| `C_FB759242` | `int` | YES |  |  |  |

#### `T_6C95C894`

- **PK:** `C_3843971D` (`K_cad02d75`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_04C36512` | `varchar(100)` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(255)` | NO |  |  |  |
| `C_D0B4D949` | `varchar(300)` | NO |  |  |  |
| `C_96C099BD` | `varchar(50)` | NO |  |  |  |
| `C_C8126FA8` | `int` | YES |  |  |  |
| `C_252EE3C7` | `int` | NO |  |  |  |

#### `T_6F5C08ED`

- **PK:** `C_7DB37878` (`K_42d26c34`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_71357FA2` | `varchar(100)` | NO |  |  |  |
| `C_D9E44109` | `date` | NO |  |  |  |
| `C_97D80A63` | `date` | NO |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_6F76DECF`

- **PK:** `C_3843971D` (`K_75eafc27`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_61F43369` | `varchar(255)` | NO |  |  |  |
| `C_2C193205` | `timestamp` | NO |  |  |  |
| `C_AC27CD50` | `timestamp` | NO |  |  |  |
| `C_4D3593A9` | `varchar(128)` | NO |  |  |  |
| `C_40F2D7AF` | `varchar(64)` | NO |  |  |  |
| `C_A67D2A6C` | `text` | YES |  |  |  |

#### `T_6FE1FD64`

- **PK:** `C_7DB37878` (`K_2a278db1`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_F8538A08` | `varchar(200)` | NO |  |  |  |
| `C_86C0034A` | `varchar(18)` | YES |  |  |  |
| `C_72D90AF3` | `varchar(254)` | YES |  |  |  |
| `C_8C7D47EE` | `varchar(20)` | YES |  |  |  |
| `C_9F34EBF7` | `varchar(100)` | YES |  |  |  |
| `C_6105EC46` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_7246DB20`

- **PK:** `C_3843971D` (`K_a0a1b4a6`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_EAA58932` | `varchar(255)` | NO |  |  |  |
| `C_2CB7E946` | `int` | NO |  |  |  |
| `C_2DC56C0C` | `varchar(100)` | NO |  |  |  |

#### `T_75198600`

- **PK:** `C_3843971D` (`K_8ed3bb1f`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_717E081B` | `timestamp` | NO |  |  |  |

#### `T_767E14CD`

- **PK:** `C_89F8A056` (`K_753f6d87`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_89F8A056` | `int` | NO | ✅ |  |  |
| `C_30AFEB5C` | `timestamp` | NO |  |  |  |

#### `T_7779E836`

- **PK:** `C_7DB37878` (`K_2cb85e5e`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A43DB406` | `timestamp` | NO |  |  |  |
| `C_0C23F601` | `numeric(8, 2)` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |
| `C_BF7FC51B` | `int` | NO |  |  |  |

#### `T_79317E82`

- **PK:** `C_7DB37878` (`K_6763e947`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_71357FA2` | `varchar(100)` | YES |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_7F849C39`

- **PK:** `C_3843971D` (`K_70ff6f5a`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_238B70A3` | `int` | YES |  |  |  |
| `C_B84F8A29` | `int` | NO |  |  |  |
| `C_B4EFE3DB` | `int` | NO |  |  |  |

#### `T_806C737C`

- **PK:** `C_3843971D` (`K_e791ba61`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_D147CBF5` | `varchar(10)` | NO |  |  |  |
| `C_A5E2302F` | `varchar(20)` | NO |  |  |  |
| `C_84DAAC7C` | `varchar(50)` | NO |  |  |  |
| `C_A80919F1` | `varchar(50)` | NO |  |  |  |
| `C_345D6439` | `int` | NO |  |  |  |
| `C_BA30D708` | `date` | NO |  |  |  |
| `C_49FD508C` | `varchar(20)` | NO |  |  |  |
| `C_437CD0C8` | `int` | NO |  |  |  |
| `C_1C5CEE2B` | `numeric(12, 2)` | NO |  |  |  |
| `C_CEC71448` | `int` | NO |  |  |  |

#### `T_829B25D9`

- **PK:** `C_7DB37878` (`K_40284068`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2FEAD22C` | `numeric(12, 2)` | NO |  |  |  |
| `C_7BC20718` | `numeric(12, 2)` | NO |  |  |  |
| `C_909F326B` | `numeric(12, 2)` | NO |  |  |  |
| `C_49658A0C` | `date` | NO |  |  |  |
| `C_24B44209` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_84B7D0DC`

- **PK:** `C_7DB37878` (`K_936df83d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_DC8F4938` | `date` | NO |  |  |  |
| `C_69035D89` | `date` | YES |  |  |  |
| `C_2071730B` | `varchar(20)` | NO |  |  |  |
| `C_A1088848` | `numeric(8, 2)` | NO |  |  |  |
| `C_C4AEDC5A` | `numeric(8, 2)` | NO |  |  |  |
| `C_24B44209` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_85194794`

- **PK:** `C_3843971D` (`K_1dcc0120`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_1154AEDB` | `text` | NO |  |  |  |
| `C_BF7FC51B` | `int` | NO |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |

#### `T_86B0D73F`

- **PK:** `C_3843971D` (`K_659c8472`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_F8538A08` | `varchar(200)` | NO |  |  |  |
| `C_86C0034A` | `varchar(18)` | YES |  |  |  |
| `C_72D90AF3` | `varchar(254)` | YES |  |  |  |
| `C_8C7D47EE` | `varchar(20)` | YES |  |  |  |
| `C_9F34EBF7` | `varchar(100)` | YES |  |  |  |
| `C_6105EC46` | `int` | YES |  |  |  |

#### `T_872E94DF`

- **PK:** `C_7DB37878` (`K_bc217c4b`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_8C2E4A03`

- **PK:** `C_3843971D` (`K_9a2cf01d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `T_8C2E4A03` | `varchar(50)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |

#### `T_9634BF2F`

- **PK:** `C_3843971D` (`K_1f2b04f6`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_8C7FDCD2` | `int` | NO |  |  |  |
| `C_94BF01BE` | `int` | NO |  |  |  |

#### `T_98A73B6C`

- **PK:** `C_7DB37878` (`K_a9d4b58f`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_9AFBDDA9`

- **PK:** `C_3843971D` (`K_da01ebe9`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_61F43369` | `int` | NO |  |  |  |
| `C_F2A8BEB4` | `int` | NO |  |  |  |

#### `T_9B4B4111`

- **PK:** `C_3843971D` (`K_92286dc3`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_E8E2C42C` | `numeric(5, 2)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_4D784B7A` | `int` | NO |  |  |  |
| `C_522843BA` | `int` | NO |  |  |  |

#### `T_A3873C8D`

- **PK:** `C_7DB37878` (`K_dfb284f0`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `T_8C2E4A03` | `varchar(50)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_A3BA632F`

- **PK:** `C_3843971D` (`K_b98315c7`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_DC8F4938` | `date` | NO |  |  |  |
| `C_69035D89` | `date` | YES |  |  |  |
| `C_2071730B` | `varchar(20)` | NO |  |  |  |
| `C_A1088848` | `numeric(8, 2)` | NO |  |  |  |
| `C_C4AEDC5A` | `numeric(8, 2)` | NO |  |  |  |
| `C_24B44209` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | NO |  |  |  |

#### `T_A44ED7F9`

- **PK:** `C_7DB37878` (`K_7ef110e4`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_3C569425` | `numeric(5, 2)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_C5415C65` | `numeric(10, 2)` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_A93B273A`

- **PK:** `C_3843971D` (`K_455fa8c9`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_B3C5C916` | `varchar(24)` | NO |  |  |  |
| `C_BCEF849A` | `numeric(9, 6)` | NO |  |  |  |
| `C_F708F5CE` | `numeric(9, 6)` | NO |  |  |  |

#### `T_AED32ABC`

- **PK:** `C_3843971D` (`K_b852801b`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |

#### `T_AF95AC82`

- **PK:** `C_3843971D` (`K_99c4cecb`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_6F6C7E96` | `varchar(255)` | NO |  |  |  |
| `C_04C36512` | `varchar(100)` | NO |  |  |  |
| `C_047ECB51` | `varchar(50)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_BD0159B6` | `date` | YES |  |  |  |
| `C_E20FBEE5` | `int` | YES |  |  |  |
| `C_5CE17026` | `int` | NO |  |  |  |

#### `T_B2749B4E`

- **PK:** `C_7DB37878` (`K_6ab72bc1`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_02318D48` | `varchar(255)` | NO |  |  |  |
| `C_8BB9E366` | `varchar(20)` | NO |  |  |  |
| `C_E48ECE77` | `varchar(100)` | YES |  |  |  |
| `C_889529CA` | `varchar(100)` | NO |  |  |  |
| `C_2AE3E40A` | `varchar(100)` | NO |  |  |  |
| `C_F16FE7D4` | `varchar(2)` | NO |  |  |  |
| `C_D686368B` | `varchar(10)` | YES |  |  |  |
| `C_B74B28B5` | `varchar(50)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_B6A4FC8C`

- **PK:** `C_7DB37878` (`K_ec80d1eb`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(200)` | NO |  |  |  |
| `C_9F84DB4F` | `text` | NO |  |  |  |
| `C_E26EF190` | `varchar(200)` | NO |  |  |  |
| `C_76E51CA4` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_BC0C970B`

- **PK:** `C_3843971D` (`K_e07288a3`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_999EC7C5` | `varchar(50)` | NO |  |  |  |
| `C_D5E72980` | `date` | NO |  |  |  |
| `C_93928056` | `date` | YES |  |  |  |
| `C_6600003A` | `varchar(20)` | NO |  |  |  |
| `C_AFB4D893` | `numeric(6, 2)` | NO |  |  |  |
| `C_06B58CC4` | `int` | NO |  |  |  |

#### `T_BE8FBFEA`

- **PK:** `C_3843971D` (`K_11bb07c8`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_BB30FD48` | `varchar(200)` | NO |  |  |  |
| `C_291B360B` | `varchar(200)` | NO |  |  |  |
| `C_9D10D4E4` | `varchar(18)` | NO |  |  |  |
| `C_72D90AF3` | `varchar(255)` | NO |  |  |  |
| `C_8C7D47EE` | `varchar(20)` | NO |  |  |  |
| `C_6105EC46` | `int` | YES |  |  |  |

#### `T_BF4B991C`

- **PK:** `C_3843971D` (`K_1c08ab81`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_EAA58932` | `varchar(200)` | NO |  |  |  |
| `C_E3091486` | `varchar(200)` | NO |  |  |  |
| `C_11AC420B` | `text` | NO |  |  |  |
| `C_63122D01` | `text` | NO |  |  |  |
| `C_F4A35C7B` | `varchar(200)` | YES |  |  |  |
| `C_CCA6B109` | `varchar(200)` | YES |  |  |  |
| `C_8E2FB3D1` | `varchar(200)` | YES |  |  |  |
| `C_ECE45D0A` | `timestamp` | YES |  |  |  |
| `C_C77D23D0` | `timestamp` | YES |  |  |  |
| `C_B0985AC3` | `int` | NO |  |  |  |
| `C_3DB4E75A` | `timestamp` | NO |  |  |  |
| `C_9CC35840` | `text` | NO |  |  |  |
| `C_58DA583E` | `int` | YES |  |  |  |
| `C_3D99CE42` | `int` | YES |  |  |  |
| `C_006FE370` | `int` | YES |  |  |  |
| `C_FC3ECFD9` | `timestamp` | YES |  |  |  |
| `C_6836EC5D` | `int` | YES |  |  |  |
| `C_B08C868A` | `text` | NO |  |  |  |
| `C_4E43E1E9` | `int` | YES |  |  |  |
| `C_29385855` | `int` | YES |  |  |  |

#### `T_BFC85B87`

- **PK:** `C_3843971D` (`K_3c9cd54d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_F3890CE9` | `int` | NO |  |  |  |
| `C_F2A8BEB4` | `int` | NO |  |  |  |

#### `T_C004F0F1`

- **PK:** `C_7DB37878` (`K_d9847efd`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(300)` | NO |  |  |  |
| `C_596FDD6A` | `date` | NO |  |  |  |
| `T_8C2E4A03` | `varchar(20)` | NO |  |  |  |
| `C_616CFC6F` | `text` | NO |  |  |  |
| `C_AC4B2BBE` | `date` | NO |  |  |  |
| `C_70509AA4` | `varchar(255)` | NO |  |  |  |
| `C_35A580E8` | `text` | NO |  |  |  |
| `C_87139025` | `text` | NO |  |  |  |
| `C_4B6AA0E6` | `text` | NO |  |  |  |
| `C_3BA5BC28` | `text` | NO |  |  |  |
| `C_0B233812` | `text` | NO |  |  |  |
| `C_8692B17E` | `int` | YES |  |  |  |
| `C_C205C1F9` | `varchar(200)` | NO |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_97E46024` | `int` | NO |  |  |  |
| `C_BABC244C` | `int` | NO |  |  |  |

#### `T_C0D68196`

- **PK:** `C_7DB37878` (`K_c9b02899`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_D147CBF5` | `varchar(10)` | NO |  |  |  |
| `C_A5E2302F` | `varchar(20)` | NO |  |  |  |
| `C_84DAAC7C` | `varchar(50)` | NO |  |  |  |
| `C_A80919F1` | `varchar(50)` | NO |  |  |  |
| `C_345D6439` | `int` | NO |  |  |  |
| `C_BA30D708` | `date` | NO |  |  |  |
| `C_49FD508C` | `varchar(20)` | NO |  |  |  |
| `C_437CD0C8` | `int` | NO |  |  |  |
| `C_1C5CEE2B` | `numeric(12, 2)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_CEC71448` | `int` | NO |  |  |  |

#### `T_C7D24495`

- **PK:** `C_7DB37878` (`K_c3a99a69`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_BD0159B6` | `date` | YES |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_C8A9BFFE`

- **PK:** `C_3843971D` (`K_3b227846`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_F98103E9` | `text` | NO |  |  |  |
| `C_80323571` | `timestamp` | YES |  |  |  |
| `C_946B160F` | `timestamp` | NO |  |  |  |
| `C_E5BB97D1` | `int` | YES |  |  |  |
| `C_C78283A3` | `varchar(255)` | NO |  |  |  |

#### `T_C931CB03`

- **PK:** `C_3843971D` (`K_b5a329aa`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_9CEE831C` | `varchar(255)` | NO |  |  |  |
| `T_8C2E4A03` | `varchar(50)` | NO |  |  |  |
| `C_4D3593A9` | `varchar(128)` | NO |  |  |  |
| `C_40F2D7AF` | `varchar(64)` | NO |  |  |  |
| `C_A67D2A6C` | `text` | YES |  |  |  |
| `C_AC27CD50` | `timestamp` | NO |  |  |  |
| `C_3A7EA708` | `text` | YES |  |  |  |
| `C_2D1EDF72` | `text` | YES |  |  |  |
| `C_ADC752ED` | `text` | YES |  |  |  |
| `C_0FB9353C` | `text` | YES |  |  |  |
| `C_555DADC9` | `varchar(255)` | YES |  |  |  |
| `C_74680EA6` | `varchar(100)` | YES |  |  |  |
| `C_2C193205` | `timestamp` | NO |  |  |  |
| `C_4D807D40` | `varchar(255)` | YES |  |  |  |
| `C_69EB1650` | `timestamp` | YES |  |  |  |

#### `T_C95CF096`

- **PK:** `C_3843971D` (`K_62ee9908`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_7D9B19F2` | `date` | NO |  |  |  |
| `C_D4C800A6` | `text` | NO |  |  |  |
| `C_E20FBEE5` | `int` | YES |  |  |  |
| `C_52968FC9` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | NO |  |  |  |
| `C_A13D6A9F` | `int` | NO |  |  |  |

#### `T_CA6939E5`

- **PK:** `C_3843971D` (`K_38052927`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_C91F1087` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | YES |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_D390039E` | `numeric(12, 2)` | YES |  |  |  |
| `C_8E230A06` | `numeric(12, 4)` | NO |  |  |  |
| `C_71357FA2` | `varchar(100)` | NO |  |  |  |
| `C_D9E44109` | `date` | NO |  |  |  |
| `C_97D80A63` | `date` | NO |  |  |  |
| `C_BF008A36` | `int` | NO |  |  |  |
| `C_1D119E20` | `int` | NO |  |  |  |

#### `T_CA72AF66`

- **PK:** `C_7DB37878` (`K_6f9eef53`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(50)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_CBCC1B25`

- **PK:** `C_7DB37878` (`K_0ed2ec8b`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_D207EFEE` | `int` | NO |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |
| `C_1EE68B99` | `int` | YES |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_CC3856A7`

- **PK:** `C_3843971D` (`K_dd02fa69`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A08D2777` | `varchar(20)` | NO |  |  |  |
| `C_D4E5C147` | `int` | NO |  |  |  |
| `C_5DD9C184` | `numeric(12, 4)` | NO |  |  |  |
| `C_F3BB8675` | `numeric(12, 4)` | NO |  |  |  |
| `C_0EFAB677` | `timestamp` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_24B44209` | `int` | NO |  |  |  |

#### `T_D052670C`

- **PK:** `C_3843971D` (`K_e39553a4`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A08D2777` | `varchar(20)` | NO |  |  |  |
| `C_D4E5C147` | `int` | NO |  |  |  |
| `C_2F2C1C01` | `numeric(12, 4)` | NO |  |  |  |
| `C_7D9B19F2` | `timestamp` | NO |  |  |  |
| `C_899F5890` | `varchar(255)` | NO |  |  |  |
| `C_2ADAB83F` | `varchar(255)` | NO |  |  |  |
| `C_A6C7C3A4` | `text` | NO |  |  |  |
| `C_97E46024` | `int` | NO |  |  |  |
| `C_035B8E23` | `int` | NO |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |

#### `T_D265EF94`

- **PK:** `C_7DB37878` (`K_87ecd25c`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_FA7B1F77` | `varchar(10)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_D3BF25E3`

- **PK:** `C_3843971D` (`K_9b6393fe`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |

#### `T_D537D402`

- **PK:** `C_3843971D` (`K_ab7a14ec`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_BC46B5F4` | `int` | NO |  |  |  |
| `C_B4EFE3DB` | `int` | NO |  |  |  |

#### `T_DC55860B`

- **PK:** `C_3843971D` (`K_858cc5d5`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_03F6B8E3` | `timestamp` | NO |  |  |  |
| `C_80B52150` | `int` | NO |  |  |  |

#### `T_DE1A8215`

- **PK:** `C_3843971D` (`K_4a2792f4`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_61F43369` | `varchar(255)` | NO |  |  |  |
| `C_B8241781` | `text` | NO |  |  |  |
| `C_9A37AE78` | `int` | NO |  |  |  |

#### `T_DE230EB6`

- **PK:** `C_7DB37878` (`K_63f1d93d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_0EC941BE` | `varchar(50)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_7124DEA5` | `text` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_E5419644`

- **PK:** `C_3843971D` (`K_9f225292`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(200)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_D207EFEE` | `int` | NO |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |
| `C_1EE68B99` | `int` | YES |  |  |  |

#### `T_E577A6BA`

- **PK:** `C_3843971D` (`K_0b92a6c7`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_1EB03F39` | `varchar(240)` | NO |  |  |  |
| `C_FAA9DECB` | `varchar(96)` | NO |  |  |  |
| `C_F54A3DF0` | `varchar(64)` | NO |  |  |  |
| `C_E31CC846` | `varchar(124)` | NO |  |  |  |
| `C_70A247FB` | `varchar(64)` | NO |  |  |  |
| `C_63BCD699` | `varchar(63)` | NO |  |  |  |

#### `T_E9BBFB52`

- **PK:** `C_3843971D` (`K_7d71649d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_5F9B0EB3` | `int` | NO |  |  |  |
| `C_F3890CE9` | `int` | NO |  |  |  |

#### `T_EA59F039`

- **PK:** `C_7DB37878` (`K_05ed10f0`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_7DB37878` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)` |
| `C_C867FE78` | `timestamp` | NO |  |  |  |
| `C_00C08FB7` | `text` | NO |  |  |  |
| `C_3843971D` | `int` | NO |  |  |  |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_A0773D8D` | `varchar(100)` | NO |  |  |  |
| `C_4F844C00` | `varchar(50)` | NO |  |  |  |
| `C_E10FE93D` | `int` | NO |  |  |  |

#### `T_EA739DC9`

- **PK:** `C_3843971D` (`K_e5b6e2b0`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_CD4C8ECF` | `varchar(20)` | NO |  |  |  |
| `C_4F627600` | `numeric(5, 2)` | YES |  |  |  |
| `C_E5F33DE1` | `date` | NO |  |  |  |
| `C_9A01ED69` | `date` | YES |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_06B58CC4` | `int` | NO |  |  |  |

#### `T_EC9858F7`

- **PK:** `C_3843971D` (`K_2b0fbb1d`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_F3890CE9` | `int` | NO |  |  |  |
| `C_61F43369` | `int` | NO |  |  |  |

#### `T_F50A1E36`

- **PK:** `C_3843971D` (`K_6a554c87`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(300)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |
| `C_792E36F5` | `varchar(50)` | NO |  |  |  |
| `C_1B9EF054` | `int` | NO |  |  |  |
| `C_67F48386` | `date` | YES |  |  |  |
| `C_E5F33DE1` | `date` | YES |  |  |  |
| `C_A43DB406` | `date` | YES |  |  |  |
| `C_48286F17` | `varchar(20)` | NO |  |  |  |
| `C_4EBF96D0` | `numeric(6, 2)` | YES |  |  |  |
| `C_24B44209` | `int` | YES |  |  |  |
| `C_E95014A5` | `int` | NO |  |  |  |
| `C_B84F8A29` | `int` | YES |  |  |  |
| `C_FC92A130` | `int` | NO |  |  |  |

#### `T_F5BE35D5`

- **PK:** `C_3843971D` (`K_d741ad51`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_A7FF72DB` | `varchar(100)` | NO |  |  |  |
| `C_FA7B1F77` | `varchar(10)` | NO |  |  |  |
| `C_D0B4D949` | `text` | NO |  |  |  |

#### `T_FD6738F9`

- **PK:** `C_3843971D` (`K_87f12342`)

| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |
|--------|------|-------|----|-----|---------|
| `C_3843971D` | `int` | NO | ✅ |  | `AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE)` |
| `C_44F41DED` | `timestamp` | YES |  |  |  |
| `C_80323571` | `timestamp` | NO |  |  |  |
| `C_37F27424` | `timestamp` | NO |  |  |  |
| `C_2A81A9B6` | `varchar(300)` | NO |  |  |  |
| `C_596FDD6A` | `date` | NO |  |  |  |
| `T_8C2E4A03` | `varchar(20)` | NO |  |  |  |
| `C_616CFC6F` | `text` | NO |  |  |  |
| `C_AC4B2BBE` | `date` | NO |  |  |  |
| `C_70509AA4` | `varchar(255)` | NO |  |  |  |
| `C_35A580E8` | `text` | NO |  |  |  |
| `C_87139025` | `text` | NO |  |  |  |
| `C_4B6AA0E6` | `text` | NO |  |  |  |
| `C_3BA5BC28` | `text` | NO |  |  |  |
| `C_0B233812` | `text` | NO |  |  |  |
| `C_8692B17E` | `int` | YES |  |  |  |
| `C_C205C1F9` | `varchar(200)` | NO |  |  |  |
| `C_1EE68B99` | `int` | NO |  |  |  |
| `C_97E46024` | `int` | NO |  |  |  |
| `C_BABC244C` | `int` | NO |  |  |  |

## 🔑 CHAVES PRIMÁRIAS

| Tabela | Constraint | Colunas |
|--------|------------|---------|
| `T_008B72D0` | `K_48587f50` | `C_3843971D` |
| `T_042FAD8B` | `K_ecde6bf7` | `C_3843971D` |
| `T_04EA3513` | `K_2bf410a8` | `C_7DB37878` |
| `T_08331B35` | `K_4223385c` | `C_7DB37878` |
| `T_0F02E5AB` | `K_6f071b23` | `C_7DB37878` |
| `T_110854C7` | `K_eece3af5` | `C_3843971D` |
| `T_189FFA19` | `K_71f6b911` | `C_3843971D` |
| `T_195AE791` | `K_72bccbae` | `C_7DB37878` |
| `T_1AB0BF01` | `K_4d9200ab` | `C_7DB37878` |
| `T_1D285733` | `K_b02aa7a6` | `C_3843971D` |
| `T_1DC445F1` | `K_804b056a` | `C_3843971D` |
| `T_217033D7` | `K_b5774642` | `C_3843971D` |
| `T_2D92DC9D` | `K_3b092f2a` | `C_3843971D` |
| `T_2E5AC9DD` | `K_6b4fde5b` | `C_3843971D` |
| `T_322CEC05` | `K_235ff9cd` | `C_3843971D` |
| `T_3452E3CE` | `K_e540e302` | `C_3843971D` |
| `T_361ECADA` | `K_9162f6ec` | `C_3843971D` |
| `T_36D9977C` | `K_d050bcaf` | `C_3843971D` |
| `T_3C0F4574` | `K_51b912e2` | `C_7DB37878` |
| `T_40D8A68B` | `K_94bd57e2` | `C_7DB37878` |
| `T_415214E3` | `K_3d56e7c0` | `C_3843971D` |
| `T_417C313C` | `K_b35606ba` | `C_3843971D` |
| `T_41B9A0B9` | `K_40d2ab0e` | `C_96548987` |
| `T_429E6B85` | `K_bab6ed82` | `C_3843971D` |
| `T_43C86CA7` | `K_9cd41fda` | `C_7DB37878` |
| `T_46761816` | `K_9a8262f6` | `C_3843971D` |
| `T_4FF564D3` | `K_99e9fd34` | `C_3843971D` |
| `T_50CDAAFF` | `K_1c58fc74` | `C_3843971D` |
| `T_51F27CE2` | `K_635cffb6` | `C_3843971D` |
| `T_57755815` | `K_9eb0557c` | `C_7DB37878` |
| `T_5802694A` | `K_883b7676` | `C_7DB37878` |
| `T_58324603` | `K_fd1fbf4e` | `C_7DB37878` |
| `T_5DA267DD` | `K_8710a1db` | `C_3843971D` |
| `T_5FB11F7A` | `K_8b1f1a1f` | `C_7DB37878` |
| `T_6105DF1C` | `K_197491f5` | `C_7DB37878` |
| `T_6772EFBF` | `K_b2a0a512` | `C_3843971D` |
| `T_6C45B3AB` | `K_8aea1854` | `C_3843971D` |
| `T_6C95C894` | `K_cad02d75` | `C_3843971D` |
| `T_6F5C08ED` | `K_42d26c34` | `C_7DB37878` |
| `T_6F76DECF` | `K_75eafc27` | `C_3843971D` |
| `T_6FE1FD64` | `K_2a278db1` | `C_7DB37878` |
| `T_7246DB20` | `K_a0a1b4a6` | `C_3843971D` |
| `T_75198600` | `K_8ed3bb1f` | `C_3843971D` |
| `T_767E14CD` | `K_753f6d87` | `C_89F8A056` |
| `T_7779E836` | `K_2cb85e5e` | `C_7DB37878` |
| `T_79317E82` | `K_6763e947` | `C_7DB37878` |
| `T_7F849C39` | `K_70ff6f5a` | `C_3843971D` |
| `T_806C737C` | `K_e791ba61` | `C_3843971D` |
| `T_829B25D9` | `K_40284068` | `C_7DB37878` |
| `T_84B7D0DC` | `K_936df83d` | `C_7DB37878` |
| `T_85194794` | `K_1dcc0120` | `C_3843971D` |
| `T_86B0D73F` | `K_659c8472` | `C_3843971D` |
| `T_872E94DF` | `K_bc217c4b` | `C_7DB37878` |
| `T_8C2E4A03` | `K_9a2cf01d` | `C_3843971D` |
| `T_9634BF2F` | `K_1f2b04f6` | `C_3843971D` |
| `T_98A73B6C` | `K_a9d4b58f` | `C_7DB37878` |
| `T_9AFBDDA9` | `K_da01ebe9` | `C_3843971D` |
| `T_9B4B4111` | `K_92286dc3` | `C_3843971D` |
| `T_A3873C8D` | `K_dfb284f0` | `C_7DB37878` |
| `T_A3BA632F` | `K_b98315c7` | `C_3843971D` |
| `T_A44ED7F9` | `K_7ef110e4` | `C_7DB37878` |
| `T_A93B273A` | `K_455fa8c9` | `C_3843971D` |
| `T_AED32ABC` | `K_b852801b` | `C_3843971D` |
| `T_AF95AC82` | `K_99c4cecb` | `C_3843971D` |
| `T_B2749B4E` | `K_6ab72bc1` | `C_7DB37878` |
| `T_B6A4FC8C` | `K_ec80d1eb` | `C_7DB37878` |
| `T_BC0C970B` | `K_e07288a3` | `C_3843971D` |
| `T_BE8FBFEA` | `K_11bb07c8` | `C_3843971D` |
| `T_BF4B991C` | `K_1c08ab81` | `C_3843971D` |
| `T_BFC85B87` | `K_3c9cd54d` | `C_3843971D` |
| `T_C004F0F1` | `K_d9847efd` | `C_7DB37878` |
| `T_C0D68196` | `K_c9b02899` | `C_7DB37878` |
| `T_C7D24495` | `K_c3a99a69` | `C_7DB37878` |
| `T_C8A9BFFE` | `K_3b227846` | `C_3843971D` |
| `T_C931CB03` | `K_b5a329aa` | `C_3843971D` |
| `T_C95CF096` | `K_62ee9908` | `C_3843971D` |
| `T_CA6939E5` | `K_38052927` | `C_3843971D` |
| `T_CA72AF66` | `K_6f9eef53` | `C_7DB37878` |
| `T_CBCC1B25` | `K_0ed2ec8b` | `C_7DB37878` |
| `T_CC3856A7` | `K_dd02fa69` | `C_3843971D` |
| `T_D052670C` | `K_e39553a4` | `C_3843971D` |
| `T_D265EF94` | `K_87ecd25c` | `C_7DB37878` |
| `T_D3BF25E3` | `K_9b6393fe` | `C_3843971D` |
| `T_D537D402` | `K_ab7a14ec` | `C_3843971D` |
| `T_DC55860B` | `K_858cc5d5` | `C_3843971D` |
| `T_DE1A8215` | `K_4a2792f4` | `C_3843971D` |
| `T_DE230EB6` | `K_63f1d93d` | `C_7DB37878` |
| `T_E5419644` | `K_9f225292` | `C_3843971D` |
| `T_E577A6BA` | `K_0b92a6c7` | `C_3843971D` |
| `T_E9BBFB52` | `K_7d71649d` | `C_3843971D` |
| `T_EA59F039` | `K_05ed10f0` | `C_7DB37878` |
| `T_EA739DC9` | `K_e5b6e2b0` | `C_3843971D` |
| `T_EC9858F7` | `K_2b0fbb1d` | `C_3843971D` |
| `T_F50A1E36` | `K_6a554c87` | `C_3843971D` |
| `T_F5BE35D5` | `K_d741ad51` | `C_3843971D` |
| `T_FD6738F9` | `K_87f12342` | `C_3843971D` |

## 🔗 RELACIONAMENTOS — FOREIGN KEYS

| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |
|---------------|-----------|----------------|-----------|------------|
| `T_008B72D0` | `C_BF7FC51B` | `T_F50A1E36` | `C_3843971D` | `K_203a1af8` |
| `T_008B72D0` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_59e19ad3` |
| `T_110854C7` | `C_1EE68B99` | `T_BE8FBFEA` | `C_3843971D` | `K_51208573` |
| `T_110854C7` | `C_B7E9CDAB` | `T_BC0C970B` | `C_3843971D` | `K_6a91ecb4` |
| `T_110854C7` | `C_7EC8E5BB` | `T_1DC445F1` | `C_3843971D` | `K_0f0f6fa2` |
| `T_110854C7` | `C_CEC71448` | `T_8C2E4A03` | `C_3843971D` | `K_5a969fd2` |
| `T_189FFA19` | `C_76E51CA4` | `T_BC0C970B` | `C_3843971D` | `K_ea0c22cf` |
| `T_217033D7` | `C_BF7FC51B` | `T_F50A1E36` | `C_3843971D` | `K_7ced836b` |
| `T_217033D7` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_fe5c270f` |
| `T_361ECADA` | `C_2CB7E946` | `T_4FF564D3` | `C_3843971D` | `K_735141b2` |
| `T_361ECADA` | `C_E5BB97D1` | `T_36D9977C` | `C_3843971D` | `K_658a86e4` |
| `T_36D9977C` | `C_06B58CC4` | `T_86B0D73F` | `C_3843971D` | `K_5f056b72` |
| `T_417C313C` | `C_BF008A36` | `T_D3BF25E3` | `C_3843971D` | `K_c294a89e` |
| `T_417C313C` | `C_1D119E20` | `T_2D92DC9D` | `C_3843971D` | `K_73a1ebca` |
| `T_429E6B85` | `C_BF008A36` | `T_D3BF25E3` | `C_3843971D` | `K_3f981147` |
| `T_429E6B85` | `C_1D119E20` | `T_2D92DC9D` | `C_3843971D` | `K_5754f6d1` |
| `T_50CDAAFF` | `C_94BF01BE` | `T_46761816` | `C_3843971D` | `K_7f1b10de` |
| `T_5DA267DD` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_e62a2f9a` |
| `T_6C45B3AB` | `C_52007D21` | `T_86B0D73F` | `C_3843971D` | `K_813ba752` |
| `T_6C45B3AB` | `C_FB759242` | `T_86B0D73F` | `C_3843971D` | `K_1048da68` |
| `T_6C95C894` | `C_C8126FA8` | `T_BC0C970B` | `C_3843971D` | `K_8ca92404` |
| `T_6C95C894` | `C_252EE3C7` | `T_FD6738F9` | `C_3843971D` | `K_df862ff1` |
| `T_7246DB20` | `C_2CB7E946` | `T_4FF564D3` | `C_3843971D` | `K_23672a6e` |
| `T_7F849C39` | `C_238B70A3` | `T_BC0C970B` | `C_3843971D` | `K_7f8e6003` |
| `T_7F849C39` | `C_B84F8A29` | `T_BC0C970B` | `C_3843971D` | `K_7b103ac1` |
| `T_7F849C39` | `C_B4EFE3DB` | `T_415214E3` | `C_3843971D` | `K_330dcfeb` |
| `T_806C737C` | `C_CEC71448` | `T_8C2E4A03` | `C_3843971D` | `K_3f4c3d9b` |
| `T_85194794` | `C_BF7FC51B` | `T_F50A1E36` | `C_3843971D` | `K_529d3ebe` |
| `T_85194794` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_ef3f1d38` |
| `T_86B0D73F` | `C_6105EC46` | `T_1DC445F1` | `C_3843971D` | `K_c1681b43` |
| `T_9634BF2F` | `C_8C7FDCD2` | `T_AF95AC82` | `C_3843971D` | `K_d0d57c04` |
| `T_9634BF2F` | `C_94BF01BE` | `T_46761816` | `C_3843971D` | `K_2b3544d5` |
| `T_9AFBDDA9` | `C_F2A8BEB4` | `T_7246DB20` | `C_3843971D` | `K_dd107705` |
| `T_9AFBDDA9` | `C_61F43369` | `T_2E5AC9DD` | `C_3843971D` | `K_e565aba4` |
| `T_9B4B4111` | `C_4D784B7A` | `T_6C45B3AB` | `C_3843971D` | `K_dc0fb87f` |
| `T_9B4B4111` | `C_522843BA` | `T_6772EFBF` | `C_3843971D` | `K_71af0f35` |
| `T_A3BA632F` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_82343ddb` |
| `T_A3BA632F` | `C_B84F8A29` | `T_BC0C970B` | `C_3843971D` | `K_b035bc99` |
| `T_AF95AC82` | `C_E20FBEE5` | `T_BC0C970B` | `C_3843971D` | `K_b9173a5c` |
| `T_AF95AC82` | `C_5CE17026` | `T_51F27CE2` | `C_3843971D` | `K_50353304` |
| `T_BC0C970B` | `C_06B58CC4` | `T_86B0D73F` | `C_3843971D` | `K_a108ecf6` |
| `T_BE8FBFEA` | `C_6105EC46` | `T_1DC445F1` | `C_3843971D` | `K_b1244546` |
| `T_BF4B991C` | `C_4E43E1E9` | `T_75198600` | `C_3843971D` | `K_6a43978a` |
| `T_BF4B991C` | `C_58DA583E` | `T_E577A6BA` | `C_3843971D` | `K_1e617015` |
| `T_BF4B991C` | `C_3D99CE42` | `T_322CEC05` | `C_3843971D` | `K_21dc1f65` |
| `T_BF4B991C` | `C_006FE370` | `T_A93B273A` | `C_3843971D` | `K_0f913798` |
| `T_BFC85B87` | `C_F2A8BEB4` | `T_7246DB20` | `C_3843971D` | `K_d8fa733a` |
| `T_BFC85B87` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_70fa42bd` |
| `T_C8A9BFFE` | `C_E5BB97D1` | `T_36D9977C` | `C_3843971D` | `K_b51bcac8` |
| `T_C95CF096` | `C_B84F8A29` | `T_BC0C970B` | `C_3843971D` | `K_5f53ac4e` |
| `T_C95CF096` | `C_E20FBEE5` | `T_BC0C970B` | `C_3843971D` | `K_db24bfcf` |
| `T_C95CF096` | `C_52968FC9` | `T_110854C7` | `C_3843971D` | `K_8cc0f689` |
| `T_C95CF096` | `C_A13D6A9F` | `T_110854C7` | `C_3843971D` | `K_b21d7d12` |
| `T_CA6939E5` | `C_BF008A36` | `T_D3BF25E3` | `C_3843971D` | `K_90c024c0` |
| `T_CA6939E5` | `C_1D119E20` | `T_2D92DC9D` | `C_3843971D` | `K_d2954b34` |
| `T_CC3856A7` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_cdf4ab0d` |
| `T_D052670C` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_750674f8` |
| `T_D052670C` | `C_97E46024` | `T_BC0C970B` | `C_3843971D` | `K_60ae2de3` |
| `T_D052670C` | `C_035B8E23` | `T_F5BE35D5` | `C_3843971D` | `K_75bb9c03` |
| `T_D537D402` | `C_BC46B5F4` | `T_AED32ABC` | `C_3843971D` | `K_d1146669` |
| `T_D537D402` | `C_B4EFE3DB` | `T_415214E3` | `C_3843971D` | `K_ac45f2f6` |
| `T_DC55860B` | `C_80B52150` | `T_C8A9BFFE` | `C_3843971D` | `K_1d3cf0f6` |
| `T_E5419644` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_e48a5be9` |
| `T_E5419644` | `C_1EE68B99` | `T_BE8FBFEA` | `C_3843971D` | `K_8d4a10f6` |
| `T_E9BBFB52` | `C_5F9B0EB3` | `T_F50A1E36` | `C_3843971D` | `K_8fc2397e` |
| `T_E9BBFB52` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_b8d3c7da` |
| `T_EA739DC9` | `C_1EE68B99` | `T_BE8FBFEA` | `C_3843971D` | `K_00062f66` |
| `T_EA739DC9` | `C_06B58CC4` | `T_86B0D73F` | `C_3843971D` | `K_901f564e` |
| `T_EC9858F7` | `C_61F43369` | `T_2E5AC9DD` | `C_3843971D` | `K_30fd0e08` |
| `T_EC9858F7` | `C_F3890CE9` | `T_36D9977C` | `C_3843971D` | `K_21e79310` |
| `T_F50A1E36` | `C_24B44209` | `T_110854C7` | `C_3843971D` | `K_403c4dda` |
| `T_F50A1E36` | `C_E95014A5` | `T_36D9977C` | `C_3843971D` | `K_c5edac04` |
| `T_F50A1E36` | `C_B84F8A29` | `T_BC0C970B` | `C_3843971D` | `K_a2a18484` |
| `T_F50A1E36` | `C_FC92A130` | `T_E5419644` | `C_3843971D` | `K_f4a45688` |
| `T_FD6738F9` | `C_1EE68B99` | `T_BE8FBFEA` | `C_3843971D` | `K_e48b295e` |
| `T_FD6738F9` | `C_97E46024` | `T_BC0C970B` | `C_3843971D` | `K_6ba4c540` |
| `T_FD6738F9` | `C_BABC244C` | `T_1D285733` | `C_3843971D` | `K_04e241a7` |
