# :money_with_wings: Aplicação — Questão 05

## :pushpin: Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit e SQLite** para atender à **Questão 05 — Gastos Diários**.

O sistema permite registrar gastos diários de Vera, informando:
- tipo do gasto
- data do gasto
- valor
- forma de pagamento

Além disso, a aplicação gera um **relatório mensal**, mostrando:
- total de gastos do mês
- listagem dos lançamentos do período
- agrupamento por tipo de gasto
- agrupamento por forma de pagamento

---

## :white_check_mark: Funcionalidades

- cadastrar gasto diário
- cadastrar novos tipos de gasto
- cadastrar novas formas de pagamento
- listar gastos cadastrados
- editar gasto existente
- excluir gasto cadastrado
- filtrar gastos por mês e ano
- calcular total mensal
- agrupar totais por tipo de gasto
- agrupar totais por forma de pagamento

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