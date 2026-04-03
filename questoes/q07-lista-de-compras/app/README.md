# :shopping_cart: Aplicação — Questão 07

## :pushpin: Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit e SQLite** para atender à **Questão 07 — Lista de Compras**.

O sistema permite controlar uma lista de compras mensal, cadastrando:
- produto
- unidade de compra
- quantidade prevista para o mês
- quantidade que efetivamente será comprada
- preço estimado

Além disso, a aplicação calcula automaticamente:
- subtotal por item
- total geral da lista mensal

---

## :white_check_mark: Funcionalidades

- cadastrar produtos
- cadastrar unidades de compra
- criar e controlar listas por mês e ano
- cadastrar item da lista mensal
- listar itens cadastrados
- editar item existente
- excluir item cadastrado
- calcular subtotal por item
- calcular total da lista
- exibir resumo mensal da compra

---

## :computer: Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- SQLite

---

## :open_file_folder: Estrutura da pasta

```text
app/
├── app.py
├── README.md
├── requirements.txt
└── data/
    └── app.db