# Questão 07 — Lista de Compras

## Análise do problema

O cenário apresenta uma lista de compras mensal controlada por Carolina.

Para cada item da lista, são informados:
- nome do produto
- unidade de compra
- quantidade prevista para o mês
- quantidade que efetivamente será comprada
- preço estimado

Além disso:
- a quantidade comprada pode variar de um mês para outro
- não há necessidade de controlar marca
- mensalmente, Carolina pode revisar quanto pagou e atualizar o preço estimado
- ao final, a lista apresenta o total da compra

Como o enunciado pede os relacionamentos representados como atributos derivados, eles serão indicados com `/`.

---

## Classes identificadas

### Classe `Produto`
Representa o produto da lista de compras.

#### Atributos
- nome : string

#### Métodos
- cadastrar()
- editarNome()

#### Exemplos
- arroz
- feijão
- açúcar
- carne

---

### Classe `UnidadeCompra`
Representa a unidade utilizada na compra do produto.

#### Atributos
- descricao : string
- sigla : string

#### Métodos
- cadastrar()
- editarDescricao()

#### Exemplos
- Quilograma / Kg
- Litro / L
- Unidade / Un

---

### Classe `ItemListaCompra`
Representa cada item lançado na lista mensal.

#### Atributos
- quantidadeMes : float
- quantidadeCompra : float
- precoEstimado : decimal
- /produto : Produto
- /unidadeCompra : UnidadeCompra
- /subtotal : decimal

#### Métodos
- cadastrar()
- editar()
- excluir()
- calcularSubtotal()
- atualizarQuantidadeCompra(novaQuantidade : float)
- atualizarPrecoEstimado(novoPreco : decimal)

---

### Classe `ListaComprasMensal`
Representa a lista de compras de um determinado mês.

#### Atributos
- mes : int
- ano : int
- /itens : List<ItemListaCompra>
- /total : decimal

#### Métodos
- adicionarItem(item : ItemListaCompra)
- removerItem(item : ItemListaCompra)
- listarItens()
- calcularTotal()
- emitirResumo()
- atualizarPrecoProduto(produto : Produto, novoPreco : decimal)

---

## Relacionamentos como atributos derivados

Na modelagem, os relacionamentos podem ser representados assim:

### Na classe `ItemListaCompra`
- /produto : Produto
- /unidadeCompra : UnidadeCompra

### Na classe `ListaComprasMensal`
- /itens : List<ItemListaCompra>

Isso indica que:
- cada item da lista está associado a um produto
- cada item da lista usa uma unidade de compra
- uma lista mensal possui vários itens

---

## Resumo da modelagem

A modelagem mais adequada para a questão fica com as seguintes classes:
- Produto
- UnidadeCompra
- ItemListaCompra
- ListaComprasMensal

A classe `ItemListaCompra` concentra os dados que realmente variam mês a mês, como:
- quantidade prevista
- quantidade comprada
- preço estimado

A classe `Produto` guarda apenas a identidade do produto.
A classe `UnidadeCompra` organiza melhor a unidade usada.
A classe `ListaComprasMensal` reúne os itens e calcula o total da compra.