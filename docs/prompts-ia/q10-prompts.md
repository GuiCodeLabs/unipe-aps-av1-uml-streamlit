# Questão 10 — Prompts da aplicação

## Sobre a questão

A questão 10 trata de um sistema de **controle de salas de reunião**.
Patrícia precisa controlar:
- uso das salas
- data
- horário
- funcionário
- cargo
- ramal
- assunto da reunião
- quantidade de lugares da sala

Também é necessário permitir realocação de reuniões e consulta de salas livres em determinada data e faixa de horário.

---

## Diagrama da questão

![Diagrama de Classes da Questão 10](/questoes/q10-sala-de-reuniao/diagramas/diagrama-classes-q10.png)

> Caso a imagem não apareça no GitHub, verifique se o arquivo `diagrama-classes-q10.png` existe nessa pasta.

---

## Prompt 1 — Geração do app.py

Use a descrição da questão 10 como base para gerar uma aplicação web em Python utilizando Streamlit.

Contexto da questão:
Patrícia controla três salas de reunião da empresa. Existe a necessidade de cadastrar funcionários com nome, cargo e ramal, cadastrar salas com número e quantidade de lugares, alocar reuniões por data e horário, realocar reuniões mudando sala, data e horário, e consultar salas livres em determinada data e faixa de horário.

Requisitos para a aplicação:
- identificar classes, atributos e métodos com base no enunciado
- implementar o sistema em Python
- usar Streamlit
- permitir cadastrar funcionários
- permitir cadastrar salas com número e quantidade de lugares
- permitir agendar reuniões com data, horário e assunto
- permitir associar uma reunião a um funcionário responsável
- permitir realocar reunião
- permitir consultar salas disponíveis por data e faixa de horário
- listar reuniões agendadas
- o código deve ser funcional
- gerar tudo em `app.py`

---

## Prompt 2 — Refinamento do app

Melhore a aplicação Streamlit da questão 10.

Ajustes desejados:
- organizar a interface por abas
- separar cadastro de funcionários, salas, agendamentos e consultas
- melhorar a validação de conflitos de horário
- permitir editar e excluir reuniões
- tornar mais clara a consulta de salas livres
- deixar o código mais organizado em funções e classes

---

## Prompt 3 — README da aplicação

Gere um README.md apenas para a aplicação da questão 10.

O README deve conter:
- nome da aplicação
- objetivo
- funcionalidades
- tecnologias utilizadas
- instruções para instalação e execução
- explicação breve sobre agendamento, realocação e consulta de salas livres

---

## Observação

Este arquivo registra os prompts principais utilizados com IA na construção da aplicação da questão 10.