# :pencil2: Questão 02 — TextoSaída

## :pushpin: Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para a classe **TextoSaída**, com base em um cenário de configuração e exibição de textos em diferentes tipos de componentes visuais.

O problema descreve uma classe capaz de armazenar e configurar informações de exibição de texto, permitindo definir:

- conteúdo do texto
- tamanho da letra
- cor da fonte
- cor do fundo
- tipo de componente em que o texto será exibido

Os componentes possíveis para exibição são:

- **label**
- **edit**
- **memo**

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

A classe **TextoSaída** deve permitir configurar a exibição de um texto por meio dos seguintes atributos:

- conteúdo
- tamanho da letra
- cor da fonte
- cor do fundo
- tipo de componente

Além disso, a classe deve possuir métodos para:

- definir o texto
- alterar o tamanho da letra
- alterar a cor da fonte
- alterar a cor do fundo
- definir o tipo de componente
- exibir o conteúdo formatado

As cores disponíveis para configuração são:

- preto
- branco
- azul
- amarelo
- cinza

---

## :open_file_folder: Estrutura da questão

```text
q02-texto-saida/
├── README.md
├── analise/
│   ├── q02-classes-atributos-metodos.md
│   ├── q02-requisitos.txt
│   └── q02-requisitos-nao-funcionais.txt
├── diagramas/
│   ├── diagrama-classes-q02.puml
│   └── diagrama-classes-q02.png
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt