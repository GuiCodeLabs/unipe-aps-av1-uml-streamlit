# :cd: Questão 08 — Coleção de CDs

## :pushpin: Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para o controle de uma **coleção de CDs**.

O cenário descreve Adriano, que possui muitos CDs e deseja cadastrar sua coleção para saber exatamente quais discos possui.

Para cada CD, devem ser armazenadas as seguintes informações:

- nome do cantor(a) ou conjunto
- título do CD
- ano de lançamento

---

## :dart: Objetivo

Construir a solução da questão em duas partes:

### Parte 1 — Análise Orientada a Objetos
Identificar e documentar:

- classes
- atributos
- métodos
- relacionamentos
- requisitos funcionais
- requisitos não funcionais
- diagrama de classes

### Parte 2 — Aplicação Web
Desenvolver uma aplicação em **Python com Streamlit** para simular o funcionamento da solução proposta.

---

## :page_facing_up: Cenário resumido

Adriano possui uma coleção grande de CDs e gostaria de cadastrar os discos em um sistema.

Cada CD deve possuir:
- artista
- título
- ano de lançamento

A proposta da modelagem é organizar esses dados para permitir cadastro, consulta e gerenciamento da coleção.

---

## :classical_building: Classes identificadas

As classes definidas para esta questão foram:

- `Artista`
- `CD`
- `ColecaoCDs`

### Resumo das responsabilidades

- **Artista**: representa o cantor, cantora ou conjunto.
- **CD**: representa cada disco da coleção.
- **ColecaoCDs**: controla a lista de CDs cadastrados.

---

## :gear: Arquivos da questão

```text
q08-colecao-de-cds/
├── README.md
├── analise/
│   ├── q08-classes-atributos-metodos.md
│   ├── q08-requisitos.txt
│   └── q08-requisitos-nao-funcionais.txt
├── diagramas/
│   └── diagrama-classes-q08.puml
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt