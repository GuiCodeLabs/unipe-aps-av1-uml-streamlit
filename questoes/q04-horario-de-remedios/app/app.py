import streamlit as st
from dataclasses import dataclass, field
from datetime import date, time, datetime, timedelta
from typing import List, Optional


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Horário de Remédios",
    page_icon="💊",
    layout="wide"
)


# =========================================================
# CLASSES DO DOMÍNIO
# =========================================================
@dataclass
class Paciente:
    id: int
    nome: str

    def cadastrar(self):
        return self

    def editarNome(self, novo_nome: str):
        self.nome = novo_nome

    def obterDados(self):
        return {
            "id": self.id,
            "nome": self.nome
        }


@dataclass
class Remedio:
    id: int
    nome: str
    dosagem: str
    dataInicio: date
    quantidadedDias: int
    vezesAoDia: int
    paciente: Paciente

    def cadastrar(self):
        return self

    def calcularDataFim(self):
        return self.dataInicio + timedelta(days=self.quantidadedDias - 1)

    def obterResumo(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "dosagem": self.dosagem,
            "dataInicio": self.dataInicio.strftime("%d/%m/%Y"),
            "quantidadeDias": self.quantidadedDias,
            "vezesAoDia": self.vezesAoDia,
            "paciente": self.paciente.nome,
            "dataFim": self.calcularDataFim().strftime("%d/%m/%Y")
        }

    def validarCadastro(self):
        if not self.nome.strip():
            return False, "Informe o nome do remédio."
        if not self.dosagem.strip():
            return False, "Informe a dosagem."
        if self.quantidadedDias <= 0:
            return False, "A quantidade de dias deve ser maior que zero."
        if self.vezesAoDia <= 0:
            return False, "A quantidade de vezes ao dia deve ser maior que zero."
        return True, "Cadastro válido."


@dataclass
class HorarioMedicacao:
    id: int
    hora: time
    status: str
    observacao: str
    remedio: Remedio

    def marcarComoTomado(self):
        self.status = "Tomado"

    def marcarComoAtrasado(self):
        self.status = "Atrasado"

    def reagendar(self, nova_hora: time):
        self.hora = nova_hora
        self.status = "Reagendado"

    def exibirHorario(self):
        return {
            "id": self.id,
            "hora": self.hora.strftime("%H:%M"),
            "status": self.status,
            "observacao": self.observacao,
            "remedio": self.remedio.nome,
            "paciente": self.remedio.paciente.nome
        }


@dataclass
class PlanoMedicacao:
    id: int
    remedio: Remedio
    horarios: List[HorarioMedicacao] = field(default_factory=list)
    dataFim: Optional[date] = None

    def sugerirHorarios(self):
        sugestoes = {
            1: ["08:00"],
            2: ["08:00", "20:00"],
            3: ["08:00", "14:00", "20:00"],
            4: ["06:00", "12:00", "18:00", "00:00"],
            5: ["06:00", "10:00", "14:00", "18:00", "22:00"],
            6: ["06:00", "10:00", "14:00", "18:00", "22:00", "02:00"],
        }
        return sugestoes.get(self.remedio.vezesAoDia, ["08:00"])

    def definirHorarios(self, lista_horarios: List[time]):
        self.horarios.clear()
        for idx, h in enumerate(lista_horarios, start=1):
            self.horarios.append(
                HorarioMedicacao(
                    id=idx,
                    hora=h,
                    status="Pendente",
                    observacao="",
                    remedio=self.remedio
                )
            )
        self.dataFim = self.calcularDataFimTratamento()

    def gerarHorariosDoDia(self, data: date):
        if data < self.remedio.dataInicio or data > self.calcularDataFimTratamento():
            return []
        return self.horarios

    def reorganizarHorariosDoDia(self):
        atrasados = [h for h in self.horarios if h.status == "Atrasado"]
        if not atrasados:
            return False

        base_dt = datetime.combine(date.today(), atrasados[0].hora)
        intervalo_horas = max(1, 24 // max(1, self.remedio.vezesAoDia))

        horarios_ordenados = sorted(self.horarios, key=lambda x: x.hora)
        for i, horario in enumerate(horarios_ordenados):
            nova_hora_dt = base_dt + timedelta(hours=i * intervalo_horas)
            horario.reagendar(nova_hora_dt.time())

        return True

    def calcularDataFimTratamento(self):
        return self.remedio.calcularDataFim()


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
def inicializar_estado():
    if "pacientes" not in st.session_state:
        st.session_state.pacientes = []
    if "remedios" not in st.session_state:
        st.session_state.remedios = []
    if "planos" not in st.session_state:
        st.session_state.planos = []
    if "paciente_id_seq" not in st.session_state:
        st.session_state.paciente_id_seq = 1
    if "remedio_id_seq" not in st.session_state:
        st.session_state.remedio_id_seq = 1
    if "plano_id_seq" not in st.session_state:
        st.session_state.plano_id_seq = 1


def gerar_id(chave_seq: str):
    novo_id = st.session_state[chave_seq]
    st.session_state[chave_seq] += 1
    return novo_id


def buscar_paciente_por_id(paciente_id: int):
    for paciente in st.session_state.pacientes:
        if paciente.id == paciente_id:
            return paciente
    return None


def buscar_remedio_por_id(remedio_id: int):
    for remedio in st.session_state.remedios:
        if remedio.id == remedio_id:
            return remedio
    return None


def buscar_plano_por_id(plano_id: int):
    for plano in st.session_state.planos:
        if plano.id == plano_id:
            return plano
    return None


def texto_para_time(valor: str):
    return datetime.strptime(valor, "%H:%M").time()


def time_para_texto(valor: time):
    return valor.strftime("%H:%M")


# =========================================================
# DADOS INICIAIS
# =========================================================
def carregar_exemplo():
    if st.session_state.pacientes:
        return

    paciente = Paciente(
        id=gerar_id("paciente_id_seq"),
        nome="Maurício"
    ).cadastrar()
    st.session_state.pacientes.append(paciente)

    remedio = Remedio(
        id=gerar_id("remedio_id_seq"),
        nome="Amoxicilina",
        dosagem="500mg",
        dataInicio=date.today(),
        quantidadedDias=7,
        vezesAoDia=3,
        paciente=paciente
    ).cadastrar()
    st.session_state.remedios.append(remedio)

    plano = PlanoMedicacao(
        id=gerar_id("plano_id_seq"),
        remedio=remedio
    )
    plano.definirHorarios([
        texto_para_time("08:00"),
        texto_para_time("14:00"),
        texto_para_time("20:00")
    ])
    st.session_state.planos.append(plano)


# =========================================================
# INTERFACE
# =========================================================
inicializar_estado()
carregar_exemplo()

st.title("💊 Sistema de Horário de Remédios")
st.write(
    "Aplicação em Streamlit baseada no diagrama de classes: "
    "**Paciente**, **Remedio**, **PlanoMedicacao** e **HorarioMedicacao**."
)

aba1, aba2, aba3, aba4 = st.tabs([
    "Pacientes",
    "Remédios",
    "Planos de Medicação",
    "Planilha do Dia"
])


# =========================================================
# ABA 1 - PACIENTES
# =========================================================
with aba1:
    st.subheader("Cadastro de Pacientes")

    with st.form("form_paciente", clear_on_submit=True):
        nome_paciente = st.text_input("Nome do paciente")
        salvar_paciente = st.form_submit_button("Cadastrar paciente")

        if salvar_paciente:
            if not nome_paciente.strip():
                st.error("Informe o nome do paciente.")
            else:
                paciente = Paciente(
                    id=gerar_id("paciente_id_seq"),
                    nome=nome_paciente.strip()
                ).cadastrar()
                st.session_state.pacientes.append(paciente)
                st.success("Paciente cadastrado com sucesso!")

    st.markdown("---")
    st.subheader("Pacientes cadastrados")

    if not st.session_state.pacientes:
        st.info("Nenhum paciente cadastrado.")
    else:
        for paciente in st.session_state.pacientes:
            dados = paciente.obterDados()
            st.write(f"**ID:** {dados['id']} | **Nome:** {dados['nome']}")


# =========================================================
# ABA 2 - REMÉDIOS
# =========================================================
with aba2:
    st.subheader("Cadastro de Remédios")

    if not st.session_state.pacientes:
        st.warning("Cadastre pelo menos um paciente antes de cadastrar um remédio.")
    else:
        mapa_pacientes = {
            f"{p.id} - {p.nome}": p.id for p in st.session_state.pacientes
        }

        with st.form("form_remedio", clear_on_submit=True):
            nome_remedio = st.text_input("Nome do remédio")
            dosagem = st.text_input("Dosagem")
            data_inicio = st.date_input("Data de início", value=date.today())
            quantidade_dias = st.number_input("Quantidade de dias", min_value=1, step=1)
            vezes_ao_dia = st.number_input("Vezes ao dia", min_value=1, max_value=6, step=1)
            paciente_selecionado = st.selectbox(
                "Paciente",
                options=list(mapa_pacientes.keys())
            )

            salvar_remedio = st.form_submit_button("Cadastrar remédio")

            if salvar_remedio:
                paciente_id = mapa_pacientes[paciente_selecionado]
                paciente = buscar_paciente_por_id(paciente_id)

                remedio = Remedio(
                    id=gerar_id("remedio_id_seq"),
                    nome=nome_remedio.strip(),
                    dosagem=dosagem.strip(),
                    dataInicio=data_inicio,
                    quantidadedDias=int(quantidade_dias),
                    vezesAoDia=int(vezes_ao_dia),
                    paciente=paciente
                )

                valido, msg = remedio.validarCadastro()
                if not valido:
                    st.error(msg)
                else:
                    st.session_state.remedios.append(remedio.cadastrar())
                    st.success("Remédio cadastrado com sucesso!")

    st.markdown("---")
    st.subheader("Remédios cadastrados")

    if not st.session_state.remedios:
        st.info("Nenhum remédio cadastrado.")
    else:
        for remedio in st.session_state.remedios:
            resumo = remedio.obterResumo()
            st.write(
                f"**ID:** {resumo['id']} | "
                f"**Remédio:** {resumo['nome']} | "
                f"**Paciente:** {resumo['paciente']} | "
                f"**Dosagem:** {resumo['dosagem']} | "
                f"**Início:** {resumo['dataInicio']} | "
                f"**Fim:** {resumo['dataFim']} | "
                f"**Vezes ao dia:** {resumo['vezesAoDia']}"
            )


# =========================================================
# ABA 3 - PLANOS DE MEDICAÇÃO
# =========================================================
with aba3:
    st.subheader("Criar Plano de Medicação")

    if not st.session_state.remedios:
        st.warning("Cadastre pelo menos um remédio antes de criar um plano.")
    else:
        mapa_remedios = {
            f"{r.id} - {r.nome} ({r.paciente.nome})": r.id
            for r in st.session_state.remedios
        }

        remedio_escolhido = st.selectbox(
            "Escolha o remédio",
            options=list(mapa_remedios.keys()),
            key="select_plano_remedio"
        )

        remedio_id = mapa_remedios[remedio_escolhido]
        remedio = buscar_remedio_por_id(remedio_id)

        plano_temp = PlanoMedicacao(id=0, remedio=remedio)
        sugestoes = plano_temp.sugerirHorarios()

        st.write("**Horários sugeridos:**", ", ".join(sugestoes))

        horarios_escolhidos = []
        cols = st.columns(min(len(sugestoes), 4))
        for i, horario_sugestao in enumerate(sugestoes):
            with cols[i % len(cols)]:
                horarios_escolhidos.append(
                    st.time_input(
                        f"Horário {i + 1}",
                        value=texto_para_time(horario_sugestao),
                        key=f"time_input_{remedio.id}_{i}"
                    )
                )

        if st.button("Criar plano de medicação"):
            plano = PlanoMedicacao(
                id=gerar_id("plano_id_seq"),
                remedio=remedio
            )
            plano.definirHorarios(horarios_escolhidos)
            st.session_state.planos.append(plano)
            st.success("Plano de medicação criado com sucesso!")

    st.markdown("---")
    st.subheader("Planos cadastrados")

    if not st.session_state.planos:
        st.info("Nenhum plano cadastrado.")
    else:
        for plano in st.session_state.planos:
            st.markdown(
                f"""
**Plano ID:** {plano.id}  
**Paciente:** {plano.remedio.paciente.nome}  
**Remédio:** {plano.remedio.nome}  
**Dosagem:** {plano.remedio.dosagem}  
**Início:** {plano.remedio.dataInicio.strftime("%d/%m/%Y")}  
**Fim:** {plano.calcularDataFimTratamento().strftime("%d/%m/%Y")}  
**Horários:** {", ".join([time_para_texto(h.hora) for h in plano.horarios])}
                """
            )
            st.markdown("---")


# =========================================================
# ABA 4 - PLANILHA DO DIA
# =========================================================
with aba4:
    st.subheader("Planilha de Horários do Dia")

    if not st.session_state.planos:
        st.warning("Crie um plano de medicação para visualizar a planilha do dia.")
    else:
        data_consulta = st.date_input("Selecione a data", value=date.today(), key="data_planilha")

        opcoes_planos = {
            f"Plano {p.id} - {p.remedio.nome} ({p.remedio.paciente.nome})": p.id
            for p in st.session_state.planos
        }

        plano_selecionado_txt = st.selectbox(
            "Selecione o plano",
            options=list(opcoes_planos.keys())
        )
        plano_id = opcoes_planos[plano_selecionado_txt]
        plano = buscar_plano_por_id(plano_id)

        horarios_do_dia = plano.gerarHorariosDoDia(data_consulta)

        if not horarios_do_dia:
            st.info("Não há horários para esta data.")
        else:
            st.write(
                f"**Paciente:** {plano.remedio.paciente.nome} | "
                f"**Remédio:** {plano.remedio.nome} | "
                f"**Data:** {data_consulta.strftime('%d/%m/%Y')}"
            )
            st.markdown("---")

            for horario in horarios_do_dia:
                col1, col2, col3, col4 = st.columns([2, 2, 3, 3])

                with col1:
                    st.write(f"**Hora:** {horario.hora.strftime('%H:%M')}")

                with col2:
                    st.write(f"**Status:** {horario.status}")

                with col3:
                    nova_obs = st.text_input(
                        f"Observação #{horario.id}",
                        value=horario.observacao,
                        key=f"obs_{plano.id}_{horario.id}"
                    )
                    horario.observacao = nova_obs

                with col4:
                    btn1, btn2 = st.columns(2)
                    if btn1.button("Tomado", key=f"tomado_{plano.id}_{horario.id}"):
                        horario.marcarComoTomado()
                        st.rerun()

                    if btn2.button("Atrasado", key=f"atrasado_{plano.id}_{horario.id}"):
                        horario.marcarComoAtrasado()
                        st.rerun()

            st.markdown("---")
            if st.button("Reorganizar horários do dia"):
                reorganizado = plano.reorganizarHorariosDoDia()
                if reorganizado:
                    st.success("Horários reorganizados com sucesso.")
                else:
                    st.info("Nenhum horário atrasado encontrado para reorganizar.")
                st.rerun()

            st.markdown("---")
            st.subheader("Resumo dos horários")

            for horario in plano.horarios:
                dados = horario.exibirHorario()
                st.write(
                    f"**{dados['hora']}** | "
                    f"{dados['remedio']} | "
                    f"{dados['status']} | "
                    f"Obs.: {dados['observacao'] if dados['observacao'] else '-'}"
                )