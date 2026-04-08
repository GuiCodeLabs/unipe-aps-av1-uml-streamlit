# 🧾 Questão 06 — Comanda Eletrônica (PDV)

## 📌 Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para o controle de uma **comanda eletrônica** em uma padaria.

O sistema simula o funcionamento de uma comanda utilizada por clientes durante suas compras, permitindo registrar produtos consumidos e calcular o valor total ao final da compra.

---

## 🎯 Objetivo

Construir a solução da questão em duas partes:

### Parte 1 — Análise Orientada a Objetos
Identificar e documentar:

- classes
- atributos
- métodos
- relacionamentos (como atributos derivados)
- requisitos funcionais
- requisitos não funcionais
- diagrama de classes

---

### Parte 2 — Aplicação Web

Desenvolver uma aplicação em **Python com Streamlit** que simule o funcionamento do sistema, permitindo:

- abertura de comandas
- registro de consumo de produtos
- cálculo do valor total
- finalização da comanda

---

## 📄 Cenário resumido

O cliente utiliza uma comanda eletrônica durante suas compras na padaria.

A cada produto consumido, o atendente registra:

- o produto
- a quantidade consumida

Ao final da compra, no caixa:

- a comanda é lida
- os valores unitários dos produtos são considerados
- o sistema calcula o valor total da compra
- a comanda é finalizada

---

## 🧱 Classes, Atributos e Métodos

### 🟦 Classe Produto

**Atributos**
- codigo : int  
- nome : string  
- valorUnitario : decimal  

**Métodos**
- cadastrar()  
- editarPreco()  

---

### 🟨 Classe ItemComanda

**Atributos**
- quantidade : int  
- /produto : Produto  

**Métodos**
- calcularSubtotal()  

---

### 🟩 Classe Comanda

**Atributos**
- numero : int  
- status : string  
- /itens : List<ItemComanda>  

**Métodos**
- adicionarItem(produto, quantidade)  
- removerItem(item)  
- calcularTotal()  
- finalizarCompra()  

---

### 🟥 Classe Caixa

**Atributos**
- comandas : List<Comanda>  

**Métodos**
- abrirComanda(numero)  
- buscarComanda(numero)  
- registrarConsumo(numeroComanda, produto, quantidade)  
- fecharComanda(numeroComanda)  

---

## 🔗 Relacionamentos

- Uma **Comanda** possui vários **ItemComanda**  
- Um **ItemComanda** está associado a um **Produto**  
- Um **Caixa** gerencia várias **Comandas**  

Os relacionamentos foram representados como **atributos derivados** (`/`), conforme solicitado na questão.

---

## 📋 Requisitos Funcionais

- RF01 - O sistema deve permitir abrir uma nova comanda.  
- RF02 - O sistema deve permitir registrar produtos consumidos.  
- RF03 - O sistema deve permitir informar a quantidade de produtos.  
- RF04 - O sistema deve armazenar os itens da comanda.  
- RF05 - O sistema deve permitir listar os itens da comanda.  
- RF06 - O sistema deve calcular o valor total da comanda.  
- RF07 - O sistema deve utilizar o valor unitário dos produtos no cálculo.  
- RF08 - O sistema deve permitir remover itens da comanda.  
- RF09 - O sistema deve permitir buscar uma comanda pelo número.  
- RF10 - O sistema deve permitir finalizar a comanda.  
- RF11 - O sistema deve alterar o status da comanda após finalização.  

---

## ⚙️ Requisitos Não Funcionais

- RNF01 - O sistema deve possuir interface simples e intuitiva.  
- RNF02 - O sistema deve ser desenvolvido em Python.  
- RNF03 - O sistema deve utilizar Streamlit para a interface web.  
- RNF04 - O sistema deve apresentar os valores de forma clara.  
- RNF05 - O sistema deve garantir consistência dos dados.  
- RNF06 - O sistema deve permitir fácil manutenção do código.  

---

## 🧠 Regras de Negócio

- O subtotal de cada item é calculado por:
  
  quantidade × valorUnitario  

- O valor total da comanda é a soma dos subtotais dos itens  

- A comanda deve possuir pelo menos um item para ser finalizada  

- Após finalização, a comanda não pode ser alterada  

---

## 📊 Diagrama de Classes

O diagrama de classes foi desenvolvido utilizando **PlantUML**, representando:

- classes
- atributos
- métodos
- relacionamentos com multiplicidade

Arquivo disponível em:

diagramas/diagrama-classes-q06.puml

---

## 💻 Aplicação

A aplicação foi desenvolvida em:

- Python  
- Streamlit  

### Funcionalidades:

- abrir comanda  
- registrar consumo  
- listar itens  
- calcular total  
- finalizar compra  

---

## 🚀 Como executar

Dentro da pasta `app`, execute:

```bash
pip install -r requirements.txt
streamlit run app.py

---

## 📌


📁 Estrutura da pasta

q06-comanda-eletronica-pdv/
├── README.md
├── analise/
│   ├── q06-classes-atributos-metodos.md
│   ├── q06-requisitos.txt
│   └── q06-requisitos-nao-funcionais.txt
├── diagramas/
│   └── diagrama-classes-q06.puml
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt
    