# :cd: Aplicação — Questão 09

## :pushpin: Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit e SQLite** para atender à **Questão 09 — Coleção de CDs (Variação A)**.

O sistema permite cadastrar e gerenciar:

- CDs
- músicos
- músicas
- faixas
- duração de cada faixa
- CDs marcados como coletânea
- CDs marcados como duplos

Também disponibiliza as consultas pedidas no enunciado:

- CDs de um determinado músico
- em quais CDs está uma determinada música

---

## :white_check_mark: Funcionalidades

- cadastrar músicos
- cadastrar músicas
- cadastrar CDs
- informar se o CD é coletânea
- informar se o CD é duplo
- associar um ou mais músicos a um CD
- cadastrar faixas de um CD
- informar duração de cada faixa
- listar CDs cadastrados
- editar CD
- excluir CD
- editar faixa
- excluir faixa
- consultar CDs por músico
- consultar CDs por música
- listar coletâneas
- listar CDs duplos

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