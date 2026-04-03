# Questão 05 — Gastos Diários

## Análise do problema

O cenário apresenta uma planilha de controle de gastos diários, onde cada gasto possui:
- tipo do gasto
- data do gasto
- valor do gasto
- forma de pagamento

Além disso, no final do mês, deve ser possível:
- listar os gastos mensais
- agrupar os gastos por tipo
- exibir quanto foi gasto em cada forma de pagamento

Como o enunciado pede que os relacionamentos sejam representados como atributos derivados, os vínculos com tipo de gasto e forma de pagamento serão indicados com `/`.

---

## Classes identificadas

### Classe `Gasto`
Representa cada gasto diário lançado por Vera.

#### Atributos
- data : date
- valor : decimal
- /tipo : TipoGasto
- /formaPagamento : FormaPagamento

#### Métodos
- cadastrar()
- editar()
- excluir()
- obterResumo()

---

### Classe `TipoGasto`
Representa a categoria do gasto.

#### Atributos
- descricao : string

#### Métodos
- cadastrar()
- editarDescricao()

#### Exemplos
- remédio
- roupa
- refeição

---

### Classe `FormaPagamento`
Representa a forma usada para pagar um gasto.

#### Atributos
- descricao : string

#### Métodos
- cadastrar()
- editarDescricao()

#### Exemplos
- dinheiro
- cartão de crédito
- cartão de débito
- ticket alimentação
- refeição

---

### Classe `ControleGastos`
Responsável por manter os gastos cadastrados e gerar os relatórios mensais.

#### Atributos
- gastos : List<Gasto>

#### Métodos
- adicionarGasto(gasto : Gasto)
- removerGasto(gasto : Gasto)
- listarGastosDoMes(mes : int, ano : int)
- calcularTotalMensal(mes : int, ano : int)
- agruparTotalPorTipo(mes : int, ano : int)
- agruparTotalPorFormaPagamento(mes : int, ano : int)
- emitirRelatorioMensal(mes : int, ano : int)

---

## Relacionamentos como atributos derivados

Na classe `Gasto`, os relacionamentos podem ser representados assim:

- /tipo : TipoGasto
- /formaPagamento : FormaPagamento

Isso indica que:
- um gasto possui um tipo de gasto
- um gasto possui uma forma de pagamento

---

## Resumo da modelagem

A modelagem mais adequada para a questão fica com as seguintes classes:
- Gasto
- TipoGasto
- FormaPagamento
- ControleGastos

A classe `Gasto` é a principal do problema, pois representa cada lançamento diário.
A classe `ControleGastos` concentra as operações de consulta e geração do resumo mensal.
As classes `TipoGasto` e `FormaPagamento` organizam melhor o domínio e evitam deixar essas informações soltas apenas como texto.