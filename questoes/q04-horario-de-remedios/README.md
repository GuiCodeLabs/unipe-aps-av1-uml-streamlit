# 💊 Questão 04 — Horário de Remédios

## 📌 Sobre a questão

Esta questão tem como objetivo modelar e desenvolver uma solução para o controle de **horários de medicação**, com base em um cenário de acompanhamento do uso de remédios por um paciente.

O sistema permite cadastrar informações sobre o tratamento e organizar automaticamente os horários de uso dos medicamentos, incluindo:

* sugestão de horários de medicação
* escolha dos horários pelo usuário
* geração da planilha diária de horários
* reorganização dos horários em caso de atraso

---

## 🎯 Objetivo

Construir a solução da questão em duas partes:

### Parte 1 — Análise Orientada a Objetos

Identificar e documentar:

* classes
* atributos
* métodos
* relacionamentos
* requisitos funcionais
* requisitos não funcionais
* diagrama de classes

---

### Parte 2 — Aplicação Web

Desenvolver uma aplicação em **Python com Streamlit** que simule o funcionamento do sistema proposto.

---

## 📄 Cenário resumido

Para cada remédio, devem ser cadastradas as seguintes informações:

* nome do paciente
* nome do remédio
* dosagem
* data de início
* quantidade de dias do tratamento
* quantidade de vezes ao dia

O sistema deve:

* sugerir horários possíveis de medicação
* permitir que o usuário escolha os horários
* calcular a data final do tratamento
* gerar a planilha diária de horários
* reorganizar os horários em caso de atraso

---

## 🧠 Modelagem da solução

A solução foi estruturada com base nas seguintes classes:

* `Paciente`
* `Remedio`
* `PlanoMedicacao`
* `HorarioMedicacao`

### 🔗 Relacionamentos principais

* um paciente pode ter vários remédios
* um remédio possui um plano de medicação
* um plano de medicação possui vários horários

Os relacionamentos foram representados como **atributos derivados**, conforme solicitado no enunciado.

---

## 📁 Estrutura da questão

```text
q04-horario-de-remedios/
├── README.md
├── analise/
│   ├── q04-classes-atributos-metodos.md
│   ├── q04-requisitos.txt
│   └── q04-requisitos-nao-funcionais.txt
├── diagramas/
│   ├── diagrama-classes-q04.png
│   └── diagrama-classes-q04.puml
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt
```

---

## 🖥️ Aplicação desenvolvida

A aplicação foi implementada em **Python com Streamlit**, permitindo interação com os dados através de uma interface web simples.

### Funcionalidades principais

* cadastro de pacientes
* cadastro de remédios
* validação de dados
* cálculo automático da data final do tratamento
* sugestão de horários baseada na frequência diária
* criação de planos de medicação
* visualização da planilha diária
* marcação de horários como tomado ou atrasado
* reorganização automática dos horários

---

## 🛠️ Tecnologias utilizadas

* Python
* Streamlit
* Dataclasses
* datetime

---

## 🚀 Como executar a aplicação

No terminal, dentro da pasta `app`, execute:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Observações

* A aplicação utiliza armazenamento em memória (`session_state`)
* Ideal para fins acadêmicos e demonstração da solução
* Não utiliza banco de dados

---

## 🏁 Conclusão

A solução proposta atende aos requisitos da questão, demonstrando:

* aplicação dos conceitos de orientação a objetos
* modelagem com UML
* implementação prática com Streamlit

O sistema permite simular de forma eficiente o controle de horários de medicação, incluindo a reorganização dos horários em caso de atraso, conforme descrito no problema.
