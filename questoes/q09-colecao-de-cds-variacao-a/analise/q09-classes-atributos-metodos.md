# Questão 09 — Coleção de CDs (Variação A)

## Análise do problema

Na questão 8, bastava cadastrar o nome do cantor ou conjunto, o título do CD e o ano de lançamento.
Na questão 9, o cenário foi ampliado:

- alguns CDs são coletâneas
- um CD pode ter vários músicos
- deve ser informado se o CD é de coletânea
- deve ser informado se o CD é duplo
- cada CD deve ter sua lista de músicas
- cada faixa deve possuir duração
- deve ser possível consultar os CDs de um determinado músico
- deve ser possível consultar em quais CDs está uma determinada música

Como o enunciado diz que Adriano quer cadastrar a lista de músicos **sem relacioná-los às músicas**, a relação entre músico e música não deve existir diretamente.
Por isso, a modelagem mais adequada é separar os conceitos em classes próprias.

---

## Classes identificadas

### Classe `CD`
Representa cada CD da coleção de Adriano.

#### Atributos
- titulo : string
- anoLancamento : int
- coletanea : boolean
- duplo : boolean
- /musicos : List<Musico>
- /faixas : List<Faixa>

#### Métodos
- cadastrar()
- editar()
- excluir()
- adicionarMusico(musico : Musico)
- removerMusico(musico : Musico)
- adicionarFaixa(faixa : Faixa)
- removerFaixa(faixa : Faixa)
- listarFaixas()
- obterDetalhes()

---

### Classe `Musico`
Representa o cantor, cantora ou conjunto associado ao CD.

#### Atributos
- nome : string

#### Métodos
- cadastrar()
- editarNome()
- obterCDs()

---

### Classe `Musica`
Representa a música em si.

#### Atributos
- titulo : string

#### Métodos
- cadastrar()
- editarTitulo()
- obterCDs()

---

### Classe `Faixa`
Representa a ocorrência de uma música dentro de um CD.

#### Atributos
- numero : int
- duracao : time
- /musica : Musica

#### Métodos
- cadastrar()
- editar()
- alterarDuracao()
- obterDescricao()

---

### Classe `ControleColecaoCD`
Responsável por armazenar a coleção e executar as consultas.

#### Atributos
- cds : List<CD>
- musicos : List<Musico>
- musicas : List<Musica>

#### Métodos
- adicionarCD(cd : CD)
- removerCD(cd : CD)
- listarCDs()
- buscarCDsPorMusico(musico : Musico)
- buscarCDsPorMusica(musica : Musica)
- listarColetaneas()
- listarCDsDuplos()

---

## Relacionamentos representados como atributos derivados

Na classe `CD`:
- /musicos : List<Musico>
- /faixas : List<Faixa>

Na classe `Faixa`:
- /musica : Musica

Esses relacionamentos indicam que:
- um CD possui um ou vários músicos
- um CD possui uma ou várias faixas
- cada faixa referencia uma música
- uma mesma música pode aparecer em mais de um CD

Importante:
não existe relacionamento direto entre `Musico` e `Musica`,
porque o enunciado diz que Adriano quer cadastrar os músicos **sem relacioná-los às músicas**.

---

## Resumo da modelagem

A modelagem mais adequada para a questão 9 fica com as classes:

- CD
- Musico
- Musica
- Faixa
- ControleColecaoCD

A classe `CD` é a principal do cenário.
A classe `Faixa` é importante porque permite representar corretamente a lista de músicas de cada CD com a duração de cada faixa.
A classe `ControleColecaoCD` concentra as consultas pedidas no enunciado, principalmente:
- CDs de um determinado músico
- em quais CDs está uma determinada música