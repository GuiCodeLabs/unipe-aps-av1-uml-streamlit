# :busts_in_silhouette: Aplicação — Questão 11

## :pushpin: Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit** para atender à **Questão 11 — Herança**.

A proposta da questão é demonstrar a criação de uma **superclasse** com os atributos comuns entre `Funcionario` e `Cliente`, reorganizando a modelagem orientada a objetos.

Nesta solução:
- `Pessoa` é a superclasse
- `Funcionario` herda de `Pessoa`
- `Cliente` herda de `Pessoa`

---

## :white_check_mark: Funcionalidades

- demonstrar a estrutura de herança da modelagem
- cadastrar funcionários
- cadastrar clientes
- calcular idade com base na data de nascimento
- listar funcionários cadastrados
- listar clientes cadastrados
- aplicar reajuste salarial em funcionário

---

## :computer: Tecnologias utilizadas

- Python
- Streamlit
- Pandas

---

## :open_file_folder: Estrutura da pasta

```text
app/
├── app.py
├── README.md
└── requirements.txt