# 💊 Aplicação — Questão 04

## 📌 Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit** para atender à **Questão 04 — Horário de Remédios**.

O sistema permite o controle de medicamentos de um paciente, incluindo:

* cadastro de pacientes
* cadastro de remédios
* criação de planos de medicação
* definição de horários de uso
* visualização da planilha diária
* reorganização de horários em caso de atraso

---

## 🎯 Objetivo

Simular um sistema de controle de horários de medicação, baseado no modelo orientado a objetos definido no diagrama de classes, permitindo interação com os dados por meio de uma interface web simples.

---

## ✅ Funcionalidades

* cadastrar pacientes
* cadastrar remédios associados a um paciente
* validar dados no cadastro de remédios
* calcular automaticamente a data final do tratamento
* sugerir horários com base na quantidade de vezes ao dia
* permitir ao usuário definir horários personalizados
* criar plano de medicação
* listar planos cadastrados
* visualizar planilha de horários do dia
* marcar horários como:

  * tomado
  * atrasado
* reorganizar horários automaticamente em caso de atraso
* exibir resumo dos horários

---

## 🧠 Modelagem utilizada

A aplicação foi construída com base nas seguintes classes:

* `Paciente`
* `Remedio`
* `PlanoMedicacao`
* `HorarioMedicacao`

Seguindo o diagrama de classes definido na etapa de análise.

---

## 🖥️ Tecnologias utilizadas

* Python
* Streamlit
* Dataclasses
* datetime

---

## 📂 Estrutura da pasta

```text
app/
├── app.py
├── README.md
```

---

## 🚀 Como executar

No terminal, dentro da pasta `app`, execute:

```bash
pip install streamlit
streamlit run app.py
```

---

## 📋 Como usar

1. Cadastre um paciente
2. Cadastre um remédio associado ao paciente
3. Crie um plano de medicação
4. Ajuste os horários sugeridos
5. Acesse a aba **Planilha do Dia**
6. Marque os horários como **Tomado** ou **Atrasado**
7. Utilize a opção de **Reorganizar horários** quando necessário

---

## ⚠️ Observação

A aplicação utiliza armazenamento em memória com `st.session_state`, sendo adequada para fins acadêmicos e demonstração da solução proposta.

---

## 📌 Observação adicional

A lógica da aplicação segue o comportamento descrito no enunciado da questão, incluindo:

* sugestão automática de horários
* organização da planilha diária
* reorganização dos horários em caso de atraso

---

## 🏁 Conclusão

A aplicação atende aos requisitos da questão, demonstrando a aplicação prática dos conceitos de:

* análise orientada a objetos
* modelagem UML
* implementação em Python com Streamlit
