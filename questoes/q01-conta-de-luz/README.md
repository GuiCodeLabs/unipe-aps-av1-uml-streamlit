# :bulb: Questão 01 — Conta de Luz

## :pushpin: Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para o controle mensal de **contas de luz**, com base em um cenário de acompanhamento de consumo e gastos.

O problema descreve uma planilha utilizada para registrar informações mensais da conta de energia elétrica, permitindo armazenar dados de leitura, consumo, pagamento e média de consumo, além de realizar consultas sobre:

- mês de **menor consumo**
- mês de **maior consumo**

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

Para cada conta de luz, devem ser cadastradas as seguintes informações:

- data em que a leitura foi realizada
- número da leitura
- quantidade de KW gasto no mês
- valor a pagar
- data do pagamento
- média de consumo

A aplicação também deve permitir consultas mensais para identificar:

- o mês de menor consumo
- o mês de maior consumo

---

## :open_file_folder: Estrutura da questão

```text
q01-conta-de-luz/
├── README.md
├── analise/
│   ├── classes-atributos-metodos.md
│   ├── requisitos-funcionais.txt
│   └── requisitos-nao-funcionais.txt
├── diagramas/
│   ├── diagrama-classes-q01.puml
│   └── diagrama-classes-q01.png
└── app/
    ├── app.py
    └── README.md