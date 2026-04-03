# Questão 09 — Coleção de CDs (Variação A)

## Sobre a questão

Esta questão é uma variação do problema de coleção de CDs.

No novo cenário, Adriano percebeu que alguns CDs são **coletâneas**, ou seja, podem possuir **vários músicos** associados ao mesmo CD. Além disso, ele deseja controlar:

- o título do CD
- o ano de lançamento
- se o CD é coletânea
- se o CD é duplo
- a lista de músicos do CD
- a lista de músicas de cada CD
- a duração de cada faixa

Também são desejadas as seguintes consultas:

- identificar os CDs de um determinado músico
- identificar em quais CDs está uma determinada música

---

## Objetivo

Modelar orientadamente a objetos o cenário proposto, identificando:

- classes
- atributos
- métodos
- relacionamentos
- multiplicidades

Além disso, representar os relacionamentos como **atributos derivados**, conforme solicitado no enunciado.

---

## Modelagem adotada

Para representar corretamente o problema, foram consideradas as seguintes classes:

- `CD`
- `Musico`
- `Musica`
- `Faixa`
- `ControleColecaoCD`

### Decisão de modelagem

A classe `Faixa` foi criada para representar corretamente a presença de uma música em um CD com sua respectiva duração.

Essa escolha melhora a modelagem porque:

- um CD possui várias faixas
- cada faixa referencia uma música
- uma mesma música pode aparecer em mais de um CD
- os músicos ficam associados ao CD, e não diretamente às músicas

Isso segue exatamente o que o enunciado pede, já que Adriano quer cadastrar os músicos **sem relacioná-los às músicas**.

---

## Estrutura da pasta

```text
q09-colecao-de-cds-variacao-a/
├── README.md
├── analise/
│   ├── q09-classes-atributos-metodos.md
│   ├── q09-requisitos.txt
│   └── q09-requisitos-nao-funcionais.txt
├── diagramas/
│   ├── diagrama-classes-q09.png
│   └── diagrama-classes-q09.puml
└── app/
    ├── app.py
    ├── README.md
    ├── requirements.txt
    └── data/
        └── app.db