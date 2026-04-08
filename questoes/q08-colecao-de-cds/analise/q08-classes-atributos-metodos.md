# Questão 08 — Coleção de CDs

## Análise do problema

O cenário apresenta uma coleção de CDs de Adriano, que deseja cadastrar os discos para ter um melhor controle de sua coleção.

Para cada CD, o sistema deve armazenar:
- nome do cantor(a) ou conjunto
- título do CD
- ano de lançamento

Como o enunciado pede que os relacionamentos sejam representados como atributos derivados.

---

## Classes identificadas

### Classe `Artista`
Representa o cantor, cantora ou conjunto responsável pelo CD.

#### Atributos
- nome : string

#### Métodos
- cadastrar()
- editarNome()
- obterNome()

---

### Classe `CD`
Representa cada item da coleção de Adriano.

#### Atributos
- titulo : string
- anoLancamento : int
- artista : Artista

#### Métodos
- cadastrar()
- editar()
- excluir()
- obterDescricao()

---

### Classe `ColecaoCDs`
Responsável por armazenar e organizar os CDs cadastrados.

#### Atributos
- cds : List<CD>

#### Métodos
- adicionarCD(cd : CD)
- removerCD(cd : CD)
- listarCDs()
- buscarPorTitulo(titulo : string)
- buscarPorArtista(nomeArtista : string)

---

## Relacionamentos como atributos derivados

Na classe `CD`, o relacionamento pode ser representado assim:

- artista : Artista

Isso indica que:
- um CD possui um artista
- um artista pode estar associado a vários CDs

---

## Resumo da modelagem

A modelagem mais adequada para a questão fica com as seguintes classes:
- Artista
- CD
- ColecaoCDs

A classe `CD` é a principal do problema, pois representa cada disco da coleção.
A classe `Artista` organiza a informação do cantor(a) ou conjunto.
A classe `ColecaoCDs` centraliza o gerenciamento dos CDs cadastrados, facilitando listagem e busca.