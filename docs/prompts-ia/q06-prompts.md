# Questão 06 — Prompts da aplicação

## Sobre a questão

A questão 06 trata de uma **comanda eletrônica de padaria (PDV)**.
O cliente usa uma comanda durante as compras, e o atendente registra:
- produto
- quantidade

No caixa, a comanda é lida para calcular o valor total da compra com base no valor unitário de cada produto.

---

## Diagrama da questão

![Diagrama de Classes da Questão 06](/questoes/q06-comanda-eletronica-pdv/diagramas/diagrama-classes-q06.png)

> Caso a imagem não apareça no GitHub, verifique se o arquivo `diagrama-classes-q06.png` existe nessa pasta.

---

## Prompt 1 — Geração do app.py

Use a descrição da questão 06 como base para gerar uma aplicação web em Python utilizando Streamlit.

Contexto da questão:
A aplicação faz o controle de comanda eletrônica da padaria Doce Sabor. O cliente utiliza uma comanda com numeração. A cada produto consumido, o atendente registra o produto e a quantidade. No caixa, a comanda é lida e o sistema calcula o valor total com base no valor unitário dos produtos.

Requisitos para a aplicação:
- identificar classes, atributos e métodos a partir do enunciado
- implementar o sistema em Python
- usar Streamlit
- permitir cadastrar produtos com nome e valor unitário
- permitir criar comandas com numeração
- permitir adicionar itens e quantidades à comanda
- listar os itens registrados
- calcular subtotal por item
- calcular valor total da compra
- permitir finalizar comanda
- o código deve ser funcional
- gerar tudo em `app.py`

---

## Prompt 2 — Refinamento do app

Melhore a aplicação Streamlit da questão 06.

Ajustes desejados:
- organizar melhor a interface
- separar cadastro de produtos, abertura de comandas e fechamento da compra
- permitir editar ou remover itens da comanda
- melhorar o cálculo do total
- deixar o sistema mais intuitivo
- estruturar melhor o código em funções e classes

---

## Prompt 3 — README da aplicação

Gere um README.md apenas para a aplicação da questão 06.

O README deve conter:
- título
- objetivo da aplicação
- funcionalidades
- tecnologias utilizadas
- como instalar dependências
- como executar com Streamlit
- como funciona o fluxo de abertura e fechamento da comanda

---

## Observação

Este arquivo registra os prompts principais utilizados com IA na construção da aplicação da questão 06.