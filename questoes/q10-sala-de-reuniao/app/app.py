import streamlit as st
import pandas as pd
from dataclasses import dataclass, field
from datetime import date, time, datetime
from typing import List, Optional


st.set_page_config(
    page_title="Questão 10 - Sala de Reunião",
    page_icon=":office:",
    layout="wide"
)


# =========================================================
# MODELO DE CLASSES
# =========================================================
@dataclass
class SalaReuniao:
    numero: str
    quantidadeLugares: int

    def cadastrar(self):
        return True

    def editarCapacidade(self, nova_capacidade: int):
        self.quantidadeLugares = nova_capacidade

    def obterDisponibilidade(self, data_reuniao: date, horario_inicio: time, horario_fim: time, reunioes: List["Reuniao"]) -> bool:
        for reuniao in reunioes:
            if reuniao.sala.numero == self.numero and reuniao.data == data_reuniao:
                if horarios_conflitam(
                    horario_inicio,
                    horario_fim,
                    reuniao.horarioInicio,
                    reuniao.horarioFim
                ):
                    return False
        return True


@dataclass
class Funcionario:
    nome: str
    cargo: str
    ramal: str

    def cadastrar(self):
        return True

    def editarDados(self, novo_nome: str, novo_cargo: str, novo_ramal: str):
        self.nome = novo_nome
        self.cargo = novo_cargo
        self.ramal = novo_ramal

    def obterContato(self):
        return f"{self.nome} - Ramal: {self.ramal}"


@dataclass
class Reuniao:
    data: date
    horarioInicio: time
    horarioFim: time
    assunto: str
    funcionario: Funcionario
    sala: SalaReuniao
    id: int = field(default=0)

    def agendar(self):
        return True

    def editar(self, novo_assunto: str):
        self.assunto = novo_assunto

    def realocar(self, novaSala: SalaReuniao, novaData: date, novoHorarioInicio: time, novoHorarioFim: time):
        self.sala = novaSala
        self.data = novaData
        self.horarioInicio = novoHorarioInicio
        self.horarioFim = novoHorarioFim

    def cancelar(self):
        return True

    def obterResumo(self):
        return (
            f"{self.data.strftime('%d/%m/%Y')} | "
            f"{self.horarioInicio.strftime('%H:%M')} - {self.horarioFim.strftime('%H:%M')} | "
            f"{self.sala.numero} | {self.funcionario.nome} | {self.assunto}"
        )


class ControleReunioes:
    def __init__(self):
        self.reunioes: List[Reuniao] = []
        self.salas: List[SalaReuniao] = []
        self.funcionarios: List[Funcionario] = []

    def adicionaSala(self, sala: SalaReuniao):
        self.salas.append(sala)

    def adicionaFuncionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def agendarReuniao(self, reuniao: Reuniao):
        if self.verificarConflitos(
            sala=reuniao.sala,
            data=reuniao.data,
            horarioInicio=reuniao.horarioInicio,
            horarioFim=reuniao.horarioFim
        ):
            raise ValueError("Já existe reunião nessa sala para esse intervalo de horário.")
        self.reunioes.append(reuniao)

    def realocarReuniao(
        self,
        reuniao_id: int,
        novaSala: SalaReuniao,
        novaData: date,
        novoHorarioInicio: time,
        novoHorarioFim: time
    ):
        reuniao = self.buscarReuniaoPorId(reuniao_id)
        if reuniao is None:
            raise ValueError("Reunião não encontrada.")

        if self.verificarConflitos(
            sala=novaSala,
            data=novaData,
            horarioInicio=novoHorarioInicio,
            horarioFim=novoHorarioFim,
            ignorar_reuniao_id=reuniao_id
        ):
            raise ValueError("Conflito de horário na nova sala/data.")

        reuniao.realocar(novaSala, novaData, novoHorarioInicio, novoHorarioFim)

    def cancelarReuniao(self, reuniao_id: int):
        self.reunioes = [r for r in self.reunioes if r.id != reuniao_id]

    def listarReunioesPorData(self, data: date):
        return [r for r in self.reunioes if r.data == data]

    def consultarSalasLivres(self, data: date, horarioInicio: time, horarioFim: time):
        livres = []
        for sala in self.salas:
            if not self.verificarConflitos(sala, data, horarioInicio, horarioFim):
                livres.append(sala)
        return livres

    def verificarConflitos(
        self,
        sala: SalaReuniao,
        data: date,
        horarioInicio: time,
        horarioFim: time,
        ignorar_reuniao_id: Optional[int] = None
    ):
        for reuniao in self.reunioes:
            if ignorar_reuniao_id is not None and reuniao.id == ignorar_reuniao_id:
                continue

            if reuniao.sala.numero == sala.numero and reuniao.data == data:
                if horarios_conflitam(
                    horarioInicio,
                    horarioFim,
                    reuniao.horarioInicio,
                    reuniao.horarioFim
                ):
                    return True
        return False

    def buscarReuniaoPorId(self, reuniao_id: int) -> Optional[Reuniao]:
        for reuniao in self.reunioes:
            if reuniao.id == reuniao_id:
                return reuniao
        return None


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def horarios_conflitam(inicio1: time, fim1: time, inicio2: time, fim2: time) -> bool:
    dt_base = date.today()
    a1 = datetime.combine(dt_base, inicio1)
    b1 = datetime.combine(dt_base, fim1)
    a2 = datetime.combine(dt_base, inicio2)
    b2 = datetime.combine(dt_base, fim2)
    return a1 < b2 and a2 < b1


def formatar_hora(h: time) -> str:
    return h.strftime("%H:%M")


def inicializar_estado():
    if "controle" not in st.session_state:
        controle = ControleReunioes()

        sala1 = SalaReuniao("Sala 101", 8)
        sala2 = SalaReuniao("Sala 105", 12)
        sala3 = SalaReuniao("Sala 201", 20)

        controle.adicionaSala(sala1)
        controle.adicionaSala(sala2)
        controle.adicionaSala(sala3)

        func1 = Funcionario("Dr. Glauco", "Diretor", "101")
        func2 = Funcionario("Dra. Maria", "Gerente Jurídica", "205")
        func3 = Funcionario("Mariana", "Analista", "312")

        controle.adicionaFuncionario(func1)
        controle.adicionaFuncionario(func2)
        controle.adicionaFuncionario(func3)

        reuniao1 = Reuniao(
            id=1,
            data=date.today(),
            horarioInicio=time(8, 30),
            horarioFim=time(9, 30),
            assunto="Processo empresa Mar e Lua",
            funcionario=func1,
            sala=sala1
        )

        reuniao2 = Reuniao(
            id=2,
            data=date.today(),
            horarioInicio=time(9, 0),
            horarioFim=time(10, 0),
            assunto="Palestra sobre a nova lei de falências",
            funcionario=func2,
            sala=sala2
        )

        reuniao3 = Reuniao(
            id=3,
            data=date.today(),
            horarioInicio=time(9, 0),
            horarioFim=time(10, 0),
            assunto="Análise de material",
            funcionario=func3,
            sala=sala3
        )

        controle.agendarReuniao(reuniao1)
        controle.agendarReuniao(reuniao2)
        controle.agendarReuniao(reuniao3)

        st.session_state.controle = controle
        st.session_state.proximo_id_reuniao = 4


def gerar_id_reuniao():
    novo_id = st.session_state.proximo_id_reuniao
    st.session_state.proximo_id_reuniao += 1
    return novo_id


def obter_sala_por_numero(numero: str) -> Optional[SalaReuniao]:
    for sala in st.session_state.controle.salas:
        if sala.numero == numero:
            return sala
    return None


def obter_funcionario_por_nome(nome: str) -> Optional[Funcionario]:
    for funcionario in st.session_state.controle.funcionarios:
        if funcionario.nome == nome:
            return funcionario
    return None


def montar_dataframe_reunioes(reunioes: List[Reuniao]) -> pd.DataFrame:
    if not reunioes:
        return pd.DataFrame()

    dados = []
    for r in sorted(reunioes, key=lambda x: (x.data, x.horarioInicio, x.sala.numero)):
        dados.append({
            "ID": r.id,
            "Data": r.data.strftime("%d/%m/%Y"),
            "Início": formatar_hora(r.horarioInicio),
            "Fim": formatar_hora(r.horarioFim),
            "Sala": r.sala.numero,
            "Lugares": r.sala.quantidadeLugares,
            "Funcionário": r.funcionario.nome,
            "Cargo": r.funcionario.cargo,
            "Ramal": r.funcionario.ramal,
            "Assunto": r.assunto
        })
    return pd.DataFrame(dados)


# =========================================================
# APP
# =========================================================
inicializar_estado()
controle: ControleReunioes = st.session_state.controle

st.title(":office: Questão 10 — Controle de Salas de Reunião")
st.markdown(
    """
Aplicação web em **Python + Streamlit** baseada no diagrama enviado.
O sistema permite controlar **salas**, **funcionários** e **reuniões**,
incluindo agendamento, realocação, cancelamento e consulta de salas livres.
"""
)

abas = st.tabs([
    "Salas",
    "Funcionários",
    "Agendar Reunião",
    "Reuniões",
    "Consultar Salas Livres"
])


# =========================================================
# ABA 1 - SALAS
# =========================================================
with abas[0]:
    st.subheader("Cadastro e visualização de salas")

    with st.form("form_sala", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            numero = st.text_input("Número da sala", placeholder="Ex.: Sala 301")
        with col2:
            quantidade_lugares = st.number_input("Quantidade de lugares", min_value=1, step=1)

        salvar_sala = st.form_submit_button("Cadastrar sala")

        if salvar_sala:
            if not numero.strip():
                st.error("Informe o número da sala.")
            elif obter_sala_por_numero(numero.strip()) is not None:
                st.warning("Já existe uma sala com esse número.")
            else:
                nova_sala = SalaReuniao(numero=numero.strip(), quantidadeLugares=int(quantidade_lugares))
                controle.adicionaSala(nova_sala)
                st.success("Sala cadastrada com sucesso!")

    st.markdown("---")

    if controle.salas:
        dados_salas = pd.DataFrame([
            {"Número": s.numero, "Lugares": s.quantidadeLugares}
            for s in controle.salas
        ])
        st.dataframe(dados_salas, use_container_width=True)
    else:
        st.info("Nenhuma sala cadastrada.")


# =========================================================
# ABA 2 - FUNCIONÁRIOS
# =========================================================
with abas[1]:
    st.subheader("Cadastro e visualização de funcionários")

    with st.form("form_funcionario", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            nome = st.text_input("Nome")
        with col2:
            cargo = st.text_input("Cargo")
        with col3:
            ramal = st.text_input("Ramal")

        salvar_funcionario = st.form_submit_button("Cadastrar funcionário")

        if salvar_funcionario:
            if not nome.strip() or not cargo.strip() or not ramal.strip():
                st.error("Preencha nome, cargo e ramal.")
            elif obter_funcionario_por_nome(nome.strip()) is not None:
                st.warning("Já existe um funcionário com esse nome.")
            else:
                novo_funcionario = Funcionario(
                    nome=nome.strip(),
                    cargo=cargo.strip(),
                    ramal=ramal.strip()
                )
                controle.adicionaFuncionario(novo_funcionario)
                st.success("Funcionário cadastrado com sucesso!")

    st.markdown("---")

    if controle.funcionarios:
        dados_funcionarios = pd.DataFrame([
            {"Nome": f.nome, "Cargo": f.cargo, "Ramal": f.ramal}
            for f in controle.funcionarios
        ])
        st.dataframe(dados_funcionarios, use_container_width=True)
    else:
        st.info("Nenhum funcionário cadastrado.")


# =========================================================
# ABA 3 - AGENDAR REUNIÃO
# =========================================================
with abas[2]:
    st.subheader("Agendar nova reunião")

    if not controle.salas or not controle.funcionarios:
        st.warning("Cadastre ao menos uma sala e um funcionário antes de agendar reuniões.")
    else:
        with st.form("form_reuniao", clear_on_submit=True):
            col1, col2 = st.columns(2)

            with col1:
                data_reuniao = st.date_input("Data da reunião", value=date.today())
                horario_inicio = st.time_input("Horário de início", value=time(9, 0), step=1800)
                funcionario_nome = st.selectbox(
                    "Funcionário responsável",
                    options=[f.nome for f in controle.funcionarios]
                )

            with col2:
                horario_fim = st.time_input("Horário de fim", value=time(10, 0), step=1800)
                sala_numero = st.selectbox(
                    "Sala",
                    options=[s.numero for s in controle.salas]
                )
                assunto = st.text_input("Assunto")

            salvar_reuniao = st.form_submit_button("Agendar reunião")

            if salvar_reuniao:
                if not assunto.strip():
                    st.error("Informe o assunto da reunião.")
                elif horario_inicio >= horario_fim:
                    st.error("O horário final deve ser maior que o horário inicial.")
                else:
                    funcionario = obter_funcionario_por_nome(funcionario_nome)
                    sala = obter_sala_por_numero(sala_numero)

                    nova_reuniao = Reuniao(
                        id=gerar_id_reuniao(),
                        data=data_reuniao,
                        horarioInicio=horario_inicio,
                        horarioFim=horario_fim,
                        assunto=assunto.strip(),
                        funcionario=funcionario,
                        sala=sala
                    )

                    try:
                        controle.agendarReuniao(nova_reuniao)
                        st.success("Reunião agendada com sucesso!")
                    except ValueError as e:
                        st.error(str(e))


# =========================================================
# ABA 4 - REUNIÕES
# =========================================================
with abas[3]:
    st.subheader("Visualizar, realocar e cancelar reuniões")

    df_reunioes = montar_dataframe_reunioes(controle.reunioes)

    if df_reunioes.empty:
        st.info("Nenhuma reunião cadastrada.")
    else:
        st.dataframe(df_reunioes, use_container_width=True)

        st.markdown("---")
        st.subheader("Realocar ou cancelar reunião")

        mapa_reunioes = {
            f'ID {r.id} | {r.data.strftime("%d/%m/%Y")} | {r.sala.numero} | {r.assunto}': r.id
            for r in sorted(controle.reunioes, key=lambda x: (x.data, x.horarioInicio))
        }

        reuniao_label = st.selectbox("Selecione a reunião", list(mapa_reunioes.keys()))
        reuniao_id = mapa_reunioes[reuniao_label]
        reuniao = controle.buscarReuniaoPorId(reuniao_id)

        if reuniao:
            with st.form("form_realocar"):
                st.markdown("### Dados atuais")
                st.write(reuniao.obterResumo())

                col1, col2 = st.columns(2)
                with col1:
                    nova_data = st.date_input("Nova data", value=reuniao.data)
                    novo_horario_inicio = st.time_input("Novo horário de início", value=reuniao.horarioInicio, step=1800)
                with col2:
                    novo_horario_fim = st.time_input("Novo horário de fim", value=reuniao.horarioFim, step=1800)
                    nova_sala_numero = st.selectbox(
                        "Nova sala",
                        options=[s.numero for s in controle.salas],
                        index=[s.numero for s in controle.salas].index(reuniao.sala.numero)
                    )

                novo_assunto = st.text_input("Novo assunto", value=reuniao.assunto)

                col_btn1, col_btn2 = st.columns(2)
                btn_realocar = col_btn1.form_submit_button("Salvar alterações")
                btn_cancelar = col_btn2.form_submit_button("Cancelar reunião")

                if btn_realocar:
                    if not novo_assunto.strip():
                        st.error("Informe o assunto.")
                    elif novo_horario_inicio >= novo_horario_fim:
                        st.error("O horário final deve ser maior que o horário inicial.")
                    else:
                        try:
                            reuniao.editar(novo_assunto.strip())
                            nova_sala = obter_sala_por_numero(nova_sala_numero)
                            controle.realocarReuniao(
                                reuniao_id=reuniao.id,
                                novaSala=nova_sala,
                                novaData=nova_data,
                                novoHorarioInicio=novo_horario_inicio,
                                novoHorarioFim=novo_horario_fim
                            )
                            st.success("Reunião realocada/atualizada com sucesso!")
                            st.rerun()
                        except ValueError as e:
                            st.error(str(e))

                if btn_cancelar:
                    controle.cancelarReuniao(reuniao.id)
                    st.success("Reunião cancelada com sucesso!")
                    st.rerun()


# =========================================================
# ABA 5 - CONSULTAR SALAS LIVRES
# =========================================================
with abas[4]:
    st.subheader("Consultar salas livres por data e faixa de horário")

    if not controle.salas:
        st.warning("Nenhuma sala cadastrada.")
    else:
        col1, col2, col3 = st.columns(3)

        with col1:
            data_consulta = st.date_input("Data", value=date.today(), key="consulta_data")
        with col2:
            hora_inicio_consulta = st.time_input("Horário inicial", value=time(9, 0), step=1800, key="consulta_inicio")
        with col3:
            hora_fim_consulta = st.time_input("Horário final", value=time(10, 0), step=1800, key="consulta_fim")

        if st.button("Consultar disponibilidade"):
            if hora_inicio_consulta >= hora_fim_consulta:
                st.error("O horário final deve ser maior que o horário inicial.")
            else:
                salas_livres = controle.consultarSalasLivres(
                    data=data_consulta,
                    horarioInicio=hora_inicio_consulta,
                    horarioFim=hora_fim_consulta
                )

                if salas_livres:
                    st.success("Salas disponíveis encontradas.")
                    df_livres = pd.DataFrame([
                        {
                            "Sala": sala.numero,
                            "Lugares": sala.quantidadeLugares
                        }
                        for sala in salas_livres
                    ])
                    st.dataframe(df_livres, use_container_width=True)
                else:
                    st.warning("Nenhuma sala livre encontrada para esse período.")

        st.markdown("---")
        st.subheader("Reuniões da data selecionada")

        reunioes_data = controle.listarReunioesPorData(data_consulta)
        df_data = montar_dataframe_reunioes(reunioes_data)

        if df_data.empty:
            st.info("Não há reuniões nesta data.")
        else:
            st.dataframe(df_data, use_container_width=True)