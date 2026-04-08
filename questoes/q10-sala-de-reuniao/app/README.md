# :office: Aplicação — Questão 10

## :pushpin: Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit** para atender à **Questão 10 — Sala de Reunião**.

O sistema simula o controle de uso das salas de reunião da empresa, permitindo cadastrar salas, funcionários e reuniões, além de consultar disponibilidade de salas por data e faixa de horário. A proposta está alinhada ao cenário da questão, que exige controle de alocação, realocação e consulta de salas livres. :contentReference[oaicite:0]{index=0}

---

## :white_check_mark: Funcionalidades

- cadastrar salas de reunião
- visualizar salas cadastradas
- cadastrar funcionários
- visualizar funcionários cadastrados
- agendar reuniões
- listar reuniões cadastradas
- editar assunto da reunião
- realocar reunião para outra sala, data ou horário
- cancelar reunião
- consultar salas livres por data e faixa de horário
- impedir conflitos de horário na mesma sala

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