# :office: Questão 10 — Sala de Reunião

## :pushpin: Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para o controle de **salas de reunião** de uma empresa.

No cenário, Patrícia é responsável por controlar o uso de três salas de reunião utilizadas por todos os setores. Além do agendamento, existe a necessidade de:

- registrar informações do funcionário responsável pela reunião
- controlar sala, data, horário e assunto
- realizar realocação de reuniões
- consultar quais salas estão livres em uma determinada data e faixa de horário
- informar a quantidade de lugares de cada sala

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

Patrícia controla, em planilhas, a utilização de três salas de reunião da empresa.

Cada reunião envolve informações como:

- sala de reunião
- data
- horário
- assunto
- funcionário responsável
- cargo
- ramal

Além do agendamento, o sistema também deve permitir:

- realocar reuniões para outra sala, data ou horário
- consultar salas disponíveis em uma faixa de horário
- exibir a capacidade de cada sala

---

## :open_file_folder: Estrutura da questão

```text
q10-sala-de-reuniao/
├── README.md
├── analise/
│   ├── q10-classes-atributos-metodos.md
│   ├── q10-requisitos.txt
│   └── q10-requisitos-nao-funcionais.txt
├── diagramas/
│   ├── diagrama-classes-q10.png
│   └── diagrama-classes-q10.puml
└── app/
    ├── app.py
    ├── README.md
    ├── requirements.txt
    └── data/
        └── app.db