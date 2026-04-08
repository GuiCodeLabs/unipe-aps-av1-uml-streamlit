# Questão 04 — Prompts da aplicação

## Sobre a questão

A questão 04 trata de uma aplicação de **controle de horário de remédios**, onde são cadastrados dados como:
- nome de quem vai tomar o remédio
- data de início
- quantidade de dias
- quantidade de vezes ao dia
- dosagem
- nome do remédio

Além disso, a aplicação deve sugerir horários, permitir escolha dos melhores horários, exibir a planilha diária e reorganizar horários em caso de atraso.

---

## Diagrama da questão

![Diagrama de Classes da Questão 04](/questoes/q04-horario-de-remedios/diagramas/diagrama-classes-q04.png)

> Caso a imagem não apareça no GitHub, verifique se o arquivo `diagrama-classes-q04.png` existe nessa pasta.

---

## Prompt 1 — Geração do app.py

Use a descrição da questão 04 como base para gerar uma aplicação web em Python utilizando Streamlit.

Contexto da questão:
A aplicação controla horários de remédios no smartphone de Maurício. Para cada remédio, devem ser cadastrados nome do paciente, data de início, quantidade de dias prescrita, quantidade de vezes ao dia, dosagem e nome do remédio. Ao cadastrar, a aplicação sugere horários possíveis, o usuário escolhe os melhores horários, a aplicação informa até quando o remédio deve ser tomado e prepara uma planilha diária. Se houver atraso, os horários do dia devem ser reorganizados.

Requisitos para a aplicação:
- identificar as classes, atributos e métodos com base no enunciado
- implementar o sistema em Python
- usar Streamlit como interface
- permitir cadastrar remédios
- sugerir horários possíveis com base na quantidade de vezes ao dia
- permitir selecionar horários
- exibir uma planilha de horários do dia
- permitir reorganizar os horários em caso de atraso
- permitir visualizar a data final do tratamento
- o código deve ser funcional
- gerar tudo em `app.py`

---

## Prompt 2 — Refinamento do app

Melhore a aplicação Streamlit da questão 04.

Ajustes desejados:
- organizar melhor o layout
- separar áreas de cadastro, listagem e planilha do dia
- melhorar a lógica de sugestão de horários
- mostrar claramente a data final do tratamento
- permitir edição e exclusão de registros
- deixar o código mais limpo e modularizado

---

## Prompt 3 — README da aplicação

Gere um README.md apenas para a aplicação da questão 04.

O README deve conter:
- resumo da proposta
- funcionalidades principais
- tecnologias usadas
- instruções para executar
- observações sobre armazenamento dos dados
- explicação rápida da planilha de horários

---

## Observação

Este arquivo registra os prompts principais utilizados com IA na construção da aplicação da questão 04.