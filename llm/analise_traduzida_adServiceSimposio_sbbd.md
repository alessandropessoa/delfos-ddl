## 🔥 Análise de Hotspots — Centralidade Matemática no Grafo de Dependências

Com base exclusivamente no **grafo direcionado** formado pelas 77 arestas de chave estrangeira (FK) do schema DDL, calculei o **grau de centralidade** de cada tabela. O grau de entrada (quantas FKs apontam para ela) e o grau de saída (quantas FKs partem dela) definem a criticidade estrutural — são os **hubs** que concentram a integridade referencial e os caminhos de join.

### 📌 As 5 Tabelas mais Críticas (Hotspots)

| # | Tabela | FK Entrada | FK Saída | Grau Total | Papel Estrutural |
|---|--------|------------|----------|------------|------------------|
| 1 | **`FUNCIONARIOS`** | 12 | 1 | **13** | Catálogo/Domínio central referenciado por 12 tabelas distintas |
| 2 | **`CONTRATOS`** | 8 | 4 | **12** | Entidade de negócio principal (ex.: Pedido/Contrato) com múltiplas dependências |
| 3 | **`USUARIOS`** | 9 | 1 | **10** | Segundo maior domínio referenciado (ex.: Cliente/Localidade) |
| 4 | **`KANBAN_CARD`** | 4 | 4 | **8** | Tabela associativa/agregadora que conecta 4 hubs diferentes |
| 5 | **`PESSOAS`** | 5 | 1 | **6** | Domínio de suporte (ex.: Endereço/Contato) com forte dependência de entrada |

### 🧮 Por que essa Centralidade é Matematicamente Relevante?

1. **Degree Centrality (grau total)**:  
   - `FUNCIONARIOS` e `CONTRATOS` são vértices com grau >10. Em um grafo de 96 nós, isso representa **top 5% de concentração de arestas**. Qualquer operação de manutenção (ex.: exclusão de um registro) dispara verificações em 12 outras tabelas, gerando locks em cadeia.

2. **Betweenness Centrality implícita**:  
   - `KANBAN_CARD` atua como **ponte** entre `CONTRATOS`, `USUARIOS`, `FUNCIONARIOS` e `KANBAN_QUADRO`. Ela está no caminho crítico de qualquer consulta que una esses quatro domínios.

3. **Risco de Deadlock e Hotspot de Buffer Cache**:  
   - A ausência de **índices explícitos** (apenas PKs existem) significa que cada FK gera *full table scans* nas tabelas filhas durante verificações de integridade ou joins. As 5 tabelas listadas serão as **mais acessadas** em qualquer plano de execução que envolva mais de 2 entidades.

---

## 🔧 Sugestões de Melhoria de Normalização e Relacionamentos

### 1. Normalização de Colunas de Auditoria Repetidas

**Problema identificado:**  
Colunas como `DELETED_AT` (`updated_at`), `CREATED_AT` (`created_at`), `UPDATED_AT` (`version`/`last_modified`) aparecem em **mais de 80 tabelas**. Isso é uma violação da **Forma Normal Domínio-Chave (DKNF)**, gerando redundância de metadados e dificultando políticas globais de auditoria.

**Sugestão de Normalização:**

- **Opção A (Herança de Tabela):**  
  Se o SGBD suportar (ex.: PostgreSQL), criar uma tabela base `T_Auditavel` com as colunas de auditoria e usar `INHERITS`.  
- **Opção B (Tabela de Log Separada):**  
  Criar uma tabela única `T_Auditoria_Registros` com `(tabela_origem, id_registro, created_at, updated_at, modified_by)`. Isso reduz o volume de dados repetidos e centraliza o rastreamento.

### 2. Dependências Transitivas em Colunas Descritivas

**Problema identificado:**  
- `NOME` (varchar) e `DESCRICAO` (text) estão presentes em **dezenas de tabelas** com nomes como "descrição", "observação".  
- `OBSERVACAO` (text) aparece em tabelas de domínios diferentes, sugerindo que um mesmo atributo semântico (ex.: "comentário") está sendo replicado em vez de referenciar uma tabela de notas genérica.

**Sugestão:**

- Criar uma tabela **`T_Descricao_Item`** com `(id, tipo_item, id_item, descricao, observacao)` e remover essas colunas das tabelas filhas. Isso evita `NULLs` desnecessários e permite versionamento de descrições sem alterar a entidade principal.

### 3. Relacionamentos Muitos-para-Muitos Implícitos

**Problema identificado:**  
`KANBAN_CARD` possui **4 FKs de saída** e **4 FKs de entrada**. Ela parece ser uma **tabela associativa** entre `CONTRATOS`, `USUARIOS`, `FUNCIONARIOS` e `KANBAN_QUADRO`. Contudo, ela também contém colunas de dados (`TITULO`, `DESCRICAO`, datas, valores numéricos).

**Sugestão de Refinamento:**

- Avaliar se essas colunas de dados **dependem funcionalmente da combinação das FKs** (chave composta). Se sim, a tabela está correta (entidade associativa com atributos).  
- Caso contrário, separar em:
  - `T_Relacionamento_X_Y` (apenas FKs)  
  - `T_Detalhes_Relacionamento` (atributos dependentes)

Isso melhora a **3ª Forma Normal (3FN)** e evita anomalias de atualização.

### 4. Ausência de Índices para Chaves Estrangeiras

**Impacto direto nos hotspots:**  
Nenhuma das 77 FKs possui índice explícito no DDL. Em sistemas OLTP, isso é **crítico**. Recomenda-se criar **índices B‑tree** em **todas** as colunas FK das 5 tabelas hotspot.

| Tabela (Filha) | Coluna FK | Tabela Pai (Hotspot) |
|----------------|-----------|----------------------|
| `CONTRATOS` | `GESTOR_RESPONSAVEL_ID` | `FUNCIONARIOS` |
| `NOTIFICACOES` | `DESTINATARIO_ID` | `FUNCIONARIOS` |
| `ANEXO_RELATORIO` | `ENVIADO_POR_ID` | `FUNCIONARIOS` |
| ... (mais 9 ocorrências) | ... | `FUNCIONARIOS` |

A criação desses índices reduzirá o tempo de verificação de integridade referencial em **DELETE/UPDATE** e acelerará **JOINs** entre as tabelas centrais.

### 5. Tipo de Relacionamento Recomendado

- **`FUNCIONARIOS` ↔ Tabelas Filhas:** `1 : N` (Um registro em BC0C970B está associado a muitos nas filhas).  
- **`CONTRATOS` ↔ `KANBAN_CARD`:** `1 : N` (Um cabeçalho para muitos itens/eventos).  
- **`USUARIOS` ↔ `KANBAN_CARD`:** `1 : N` (Uma localidade/pessoa para muitos registros agregados).

Não há evidência de relacionamentos `N : M` não resolvidos, mas a repetição de colunas descritivas sugere que alguns **catálogos de domínio** (ex.: tipo de item, status) estão embutidos como literais nas tabelas filhas, o que deveria ser normalizado para tabelas de lookup.

---

## 📊 Conclusão da Análise Estática

| Métrica de Hotspot | Tabela | Ação Imediata |
|--------------------|--------|---------------|
| **Maior Grau de Entrada** | `FUNCIONARIOS` | Criar índices nas FKs que apontam para ela. Avaliar particionamento se houver muitos registros históricos. |
| **Maior Grau de Saída** | `KANBAN_CARD` | Verificar normalização de atributos não-chave. Monitorar bloqueios em transações que a utilizam. |
| **Maior número de colunas** | `RELATORIO_VISITA` (19 colunas) | Sugere possível *denormalização* intencional; validar se é um agregado materializado. |

> ⚠️ **Nota:** Sem dados populados, esta análise identifica **riscos estruturais**. A criticidade real em produção dependerá do volume de dados e da frequência de acesso a essas tabelas. Recomenda-se complementar com **query profiling** e **estatísticas do otimizador**.