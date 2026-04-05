# 🧾 Aplicação — Questão 06: Comanda Eletrônica (PDV)

## 📌 Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit** com base no diagrama de classes fornecido, simulando o funcionamento de uma **comanda eletrônica de padaria (PDV)**.

O sistema permite registrar os produtos consumidos por um cliente em uma comanda e, ao final, realizar o fechamento da conta no caixa.

---

## ✅ Funcionalidades

* cadastrar produtos
* visualizar lista de produtos
* editar preço de produtos
* abrir novas comandas
* registrar consumo (produto + quantidade)
* visualizar itens da comanda
* remover itens da comanda
* calcular total automaticamente
* finalizar compra (fechar comanda)
* visualizar resumo geral (comandas abertas, fechadas e faturamento)

---

## 🧠 Modelagem aplicada

A aplicação segue o diagrama de classes com as seguintes entidades:

* **Produto**
* **ItemComanda**
* **Comanda**
* **Caixa**

Cada classe foi implementada diretamente no código utilizando conceitos de **Programação Orientada a Objetos (POO)**.

---

## 💻 Tecnologias utilizadas

* Python
* Streamlit
* Pandas

---

## 🚀 Como executar

1. Instale as dependências:

```bash
pip install streamlit pandas
```

2. Execute a aplicação:

```bash
streamlit run app.py
```

---

## 📂 Estrutura

```text
app/
└── app.py
```

---

## 📝 Como usar

1. Acesse a aba **Produtos** e cadastre os produtos disponíveis.
2. Vá para a aba **Comandas** e abra uma nova comanda.
3. Registre os produtos consumidos pelo cliente.
4. Visualize os itens adicionados e o total da comanda.
5. Acesse a aba **Caixa / Fechamento** para finalizar a compra.
6. Consulte o resumo geral do sistema.

---

## ⚠️ Observações

* Os dados são armazenados em memória usando `session_state`.
* Ao reiniciar a aplicação, os dados serão perdidos.
* Ideal para fins acadêmicos e demonstração do funcionamento do sistema.

---
