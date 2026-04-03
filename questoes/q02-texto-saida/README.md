# :pencil2: Questão 02 — TextoSaída 

## :pushpin: Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para a classe **TextoSaída**, com base em um cenário de configuração e exibição de textos.

O problema descreve uma classe que permite configurar a apresentação de um texto, controlando aspectos visuais como tamanho da letra, cor da fonte, cor do fundo e o tipo de componente onde o texto será exibido.

A solução deve permitir exibir o texto em diferentes formatos:

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

A classe **TextoSaída** deve permitir configurar um texto através dos seguintes atributos:

- conteúdo do texto
- tamanho da letra
- cor da fonte
- cor do fundo
- tipo de componente

Além disso, a classe deve disponibilizar operações para:

- definir o texto
- alterar o tamanho da letra
- alterar a cor da fonte
- alterar a cor do fundo
- definir o tipo de componente
- exibir o texto configurado

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