## 🧠 Interpretação do Resultado: Por que a Eficácia da Máscara Falhou?

O relatório mostra que **todos os experimentos passaram, exceto a Eficácia da Máscara**, que obteve **ganho de entropia negativo** (-0.07 bits). Vamos destrinchar isso.

### 🔍 O que significa "ganho de entropia negativo"?

- **Entropia de Shannon** mede a *aleatoriedade* ou *imprevisibilidade* de um conjunto de strings.  
- Um **ganho positivo** indica que os nomes mascarados são mais aleatórios que os originais (desejável para anonimização).  
- Um **ganho negativo** significa que os nomes mascarados são **menos diversos** que os originais — ou seja, o processo de mascaramento *reduziu* a entropia do esquema.

### 📊 Por que isso aconteceu no seu caso?

Olhando os dados do relatório:

| Métrica                     | Original | Mascarado |
|-----------------------------|----------|-----------|
| Razão de unicidade          | 0.30     | 0.30      |
| Número de nomes únicos      | ~289/964 | ~289/964  |

A razão de unicidade ficou **idêntica** (0,30), então a quantidade de nomes distintos é a mesma.  
No entanto, a entropia caiu ligeiramente. Isso indica que os nomes mascarados têm **padrões mais repetitivos** do que os originais.

#### Causa mais provável:

Você usou o modo padrão `--mode hash` com comprimento de hash `--length 8`.  
O algoritmo gera um hash SHA-256 do nome original e pega os **primeiros 8 caracteres hexadecimais**.  
Com 96 tabelas e 964 colunas, o espaço de 8 caracteres hexa (16^8 = 4,29 bilhões de possibilidades) é grande, **mas**:

- O prefixo fixo (`T_` para tabelas, `C_` para colunas) consome 2 caracteres, restando apenas **6 caracteres hexa** de variação (16^6 ≈ 16,7 milhões).
- A distribuição dos primeiros 6 caracteres de um hash **não é uniforme na prática** para entradas pequenas e sem salt.
- Além disso, a entropia é calculada **caractere a caractere** em toda a string concatenada, e o uso de prefixos fixos (`T_`, `C_`) reduz a diversidade global de caracteres.

### 📉 Consequência Prática

Embora a correlação topológica (isomorfismo) seja perfeita (r=1.0) e o risco de reidentificação seja baixo (k elevado), **a baixa entropia pode facilitar ataques de dicionário** se o atacante conhecer o algoritmo de hash e o comprimento usado.  
Em um cenário de segurança mais rigoroso, isso pode ser considerado uma fragilidade.

---

## 🛠️ O Que Fazer Para Corrigir

Você precisa **aumentar a entropia dos nomes mascarados**. Há duas abordagens principais, que podem ser combinadas.

### 🔧 Opção 1: Aumentar o comprimento do hash (mais simples)

Execute novamente o pipeline com `--length` maior, por exemplo 12 ou 16.

```bash
python delfos.py pipeline app-adservice.sql --output-dir ./output-exp-adservice-longhash --mode hash --length 12
```

**O que muda:**  
- Nomes como `T_7EE4E828` viram `T_7EE4E828A1B2` (12 caracteres hexa no total, 10 após o prefixo).  
- Aumenta drasticamente o espaço de saída e a variação caractere a caractere.  
- O ganho de entropia provavelmente se tornará positivo.

### 🔧 Opção 2: Usar modo `scoped` (recomendado para máxima segurança)

O modo `scoped` gera um hash **único por tabela.coluna**, impedindo que o mesmo nome em contextos diferentes receba o mesmo hash.

```bash
python delfos.py pipeline app-adservice.sql --output-dir ./output-exp-adservice-scoped --mode scoped
```

**O que muda:**  
- O hash é calculado com um *namespace* (`tabela.coluna`), não apenas o nome da coluna.  
- Mesmo que duas tabelas tenham coluna `id`, elas receberão hashes diferentes.  
- A entropia aumenta porque o espaço de entrada é maior e mais diverso.

### 🔧 Opção 3: Combinar `scoped` com `length` maior

Para máxima entropia e segurança:

```bash
python delfos.py pipeline app-adservice.sql --output-dir ./output-exp-adservice-seguro --mode scoped --length 16
```

---

## 🔄 Como Validar a Correção

Após gerar o novo artefato, execute novamente a validação completa:

```bash
python evaluate.py --dir ./output-exp-adservice-longhash --full-validation
```

Compare o novo relatório. Você deve ver:

- **Ganho de entropia positivo** (ex: +2.5 bits).  
- Todos os demais critérios mantendo-se aprovados.

---

## 📚 Interpretação Técnica Detalhada

### Entropia de Shannon em nomes de esquema

A função de entropia implementada no avaliador concatena **todos os nomes de objetos** (tabelas, colunas, constraints, índices) em uma única string gigante e calcula a entropia de caracteres nessa string.

**Exemplo simplificado:**  
- Original: `"users" + "id" + "name" + ...`  
- Mascarado: `"T_7EE4E828" + "C_CF4A6E1B" + "C_74507A61" + ...`

Se os hashes de 8 caracteres produzem muitos caracteres repetidos (por exemplo, muitos `A`, `B`, `C` nas primeiras posições), a entropia cai.

### Por que o isomorfismo continuou perfeito?

O SRE (Structural Relevance Score) **não depende dos nomes**, apenas da **estrutura de chaves e índices**.  
Como o mascaramento preserva todas as PKs, FKs e índices, a topologia é idêntica — daí r = 1.0.

### Por que o risco de reidentificação passou?

O k‑anonymity foi alto porque o número de tabelas (96) e colunas (964) é grande, e os comprimentos dos nomes mascarados são uniformes (todos os nomes de tabela têm o mesmo comprimento `T_XXXXXXXX`).  
Isso torna difícil isolar um único objeto pelo comprimento.  
**Atenção:** Isso não significa que o esquema seja imune a ataques de dicionário, apenas que a métrica de k‑anonymity (baseada em comprimento e prefixo) não detecta a baixa entropia dos caracteres. Por isso o experimento de eficácia é importante.

---

## ✅ Resumo das Ações

| Ação                                                                 | Comando                                                                                         | Resultado Esperado                          |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------|
| 1. Regerar com hash mais longo                                        | `python delfos.py pipeline ... --length 12`                                                      | Ganho de entropia > 0                       |
| 2. Regerar com modo scoped                                            | `python delfos.py pipeline ... --mode scoped`                                                    | Entropia máxima, unicidade total            |
| 3. Reexecutar validação completa                                      | `python evaluate.py --dir ./novo-diretorio --full-validation`                                    | Relatório com "APROVADO" em todos os itens  |

Após a correção, o relatório deve exibir:

```
| **Eficácia da Máscara**  | ✅ PASSOU | Subst. = 100.0%, Entropia = +2.34 bits |
```

E o veredito final será **✅ APROVADO**.