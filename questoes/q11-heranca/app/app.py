from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

import pandas as pd
import streamlit as st


# =========================================================
# CONFIGURAÇÃO INICIAL
# =========================================================
st.set_page_config(
    page_title="Questão 11 - Herança",
    page_icon=":busts_in_silhouette:",
    layout="wide"
)


# =========================================================
# MODELO ORIENTADO A OBJETOS
# =========================================================
@dataclass
class Endereco:
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str

    def formatado(self) -> str:
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"


@dataclass
class Telefone:
    numero: str
    tipo: str

    def formatado(self) -> str:
        return f"{self.tipo}: {self.numero}"


@dataclass
class Pessoa:
    nome: str
    data_nascimento: date
    endereco: Endereco
    telefones: List[Telefone] = field(default_factory=list)

    def cadastrar(self) -> str:
        return f"{self.nome} cadastrada com sucesso."

    def obter_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade


@dataclass
class Cargo:
    nome: str
    descricao: str


@dataclass
class Profissao:
    nome: str
    descricao: str


@dataclass
class Funcionario(Pessoa):
    matricula: int = 0
    cargo: Optional[Cargo] = None
    salario: float = 0.0
    data_admissao: Optional[date] = None

    def reajustar_salario(self, percentual: float) -> float:
        self.salario += self.salario * (percentual / 100)
        return self.salario

    def promover(self, novo_cargo: Cargo) -> None:
        self.cargo = novo_cargo


@dataclass
class Cliente(Pessoa):
    codigo: str = ""
    profissao: Optional[Profissao] = None


# =========================================================
# ESTADO
# =========================================================
def inicializar_estado():
    if "funcionarios" not in st.session_state:
        st.session_state.funcionarios = []

    if "clientes" not in st.session_state:
        st.session_state.clientes = []

    if "dados_exemplo" not in st.session_state:
        popular_dados_exemplo()
        st.session_state.dados_exemplo = True


def popular_dados_exemplo():
    endereco_1 = Endereco(
        logradouro="Rua das Flores",
        numero="120",
        bairro="Centro",
        cidade="João Pessoa",
        estado="PB",
        cep="58000-000"
    )
    telefones_1 = [
        Telefone(numero="(83) 99999-1111", tipo="Celular"),
        Telefone(numero="(83) 3222-1111", tipo="Residencial")
    ]
    cargo_1 = Cargo(nome="Analista de Sistemas", descricao="Responsável por análise e modelagem")
    funcionario = Funcionario(
        matricula=1001,
        nome="Marcos Silva",
        data_nascimento=date(1995, 5, 10),
        endereco=endereco_1,
        telefones=telefones_1,
        cargo=cargo_1,
        salario=3500.00,
        data_admissao=date(2023, 2, 1)
    )

    endereco_2 = Endereco(
        logradouro="Av. Beira Rio",
        numero="450",
        bairro="Manaíra",
        cidade="João Pessoa",
        estado="PB",
        cep="58038-000"
    )
    telefones_2 = [Telefone(numero="(83) 98888-2222", tipo="Celular")]
    profissao_1 = Profissao(nome="Designer", descricao="Profissional da área de design")
    cliente = Cliente(
        codigo="CLI-001",
        nome="Ana Souza",
        data_nascimento=date(1998, 9, 25),
        endereco=endereco_2,
        telefones=telefones_2,
        profissao=profissao_1
    )

    st.session_state.funcionarios.append(funcionario)
    st.session_state.clientes.append(cliente)


def criar_endereco(logradouro, numero, bairro, cidade, estado, cep):
    return Endereco(
        logradouro=logradouro.strip(),
        numero=numero.strip(),
        bairro=bairro.strip(),
        cidade=cidade.strip(),
        estado=estado.strip(),
        cep=cep.strip()
    )


def criar_lista_telefones(texto_telefones: str) -> List[Telefone]:
    """
    Formato esperado por linha:
    tipo - numero
    Exemplo:
    Celular - (83) 99999-0000
    Residencial - (83) 3222-0000
    """
    telefones = []
    linhas = [linha.strip() for linha in texto_telefones.splitlines() if linha.strip()]

    for linha in linhas:
        if " - " in linha:
            tipo, numero = linha.split(" - ", 1)
            telefones.append(Telefone(numero=numero.strip(), tipo=tipo.strip()))
        else:
            telefones.append(Telefone(numero=linha.strip(), tipo="Contato"))

    return telefones


def funcionarios_para_dataframe():
    dados = []
    for funcionario in st.session_state.funcionarios:
        dados.append({
            "Matrícula": funcionario.matricula,
            "Nome": funcionario.nome,
            "Idade": funcionario.obter_idade(),
            "Cargo": funcionario.cargo.nome if funcionario.cargo else "",
            "Salário": f"R$ {funcionario.salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "Admissão": funcionario.data_admissao.strftime("%d/%m/%Y") if funcionario.data_admissao else "",
            "Cidade": funcionario.endereco.cidade,
            "Telefones": "; ".join(t.formatado() for t in funcionario.telefones)
        })
    return pd.DataFrame(dados)


def clientes_para_dataframe():
    dados = []
    for cliente in st.session_state.clientes:
        dados.append({
            "Código": cliente.codigo,
            "Nome": cliente.nome,
            "Idade": cliente.obter_idade(),
            "Profissão": cliente.profissao.nome if cliente.profissao else "",
            "Cidade": cliente.endereco.cidade,
            "Telefones": "; ".join(t.formatado() for t in cliente.telefones)
        })
    return pd.DataFrame(dados)


# =========================================================
# INÍCIO
# =========================================================
inicializar_estado()

st.title(":busts_in_silhouette: Questão 11 — Herança")
st.markdown(
    """
Aplicação demonstrativa em **Python + Streamlit** para representar o conceito de **herança**,
utilizando a superclasse `Pessoa` e as subclasses `Funcionario` e `Cliente`.
"""
)

st.info(
    "Nesta solução, os atributos comuns ficam em Pessoa, enquanto os atributos específicos permanecem em Funcionario e Cliente."
)

aba1, aba2, aba3, aba4 = st.tabs(
    ["Visão da Herança", "Cadastrar Funcionário", "Cadastrar Cliente", "Listagens"]
)

# =========================================================
# ABA 1 - VISÃO DA HERANÇA
# =========================================================
with aba1:
    st.subheader("Estrutura da modelagem")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Superclasse `Pessoa`")
        st.markdown("""
- nome
- data_nascimento
- endereco
- telefones
- cadastrar()
- obter_idade()
""")

    with col2:
        st.markdown("### Subclasse `Funcionario`")
        st.markdown("""
- matricula
- cargo
- salario
- data_admissao
- reajustar_salario()
- promover()
""")

    with col3:
        st.markdown("### Subclasse `Cliente`")
        st.markdown("""
- codigo
- profissao
""")

    st.markdown("---")
    st.subheader("Exemplo prático da herança")

    total_pessoas = len(st.session_state.funcionarios) + len(st.session_state.clientes)
    col4, col5, col6 = st.columns(3)
    col4.metric("Funcionários cadastrados", len(st.session_state.funcionarios))
    col5.metric("Clientes cadastrados", len(st.session_state.clientes))
    col6.metric("Total de objetos derivados de Pessoa", total_pessoas)


# =========================================================
# ABA 2 - CADASTRAR FUNCIONÁRIO
# =========================================================
with aba2:
    st.subheader("Cadastro de funcionário")

    with st.form("form_funcionario", clear_on_submit=True):
        st.markdown("### Dados pessoais")
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome")
            data_nascimento = st.date_input("Data de nascimento", value=date(2000, 1, 1))
            matricula = st.number_input("Matrícula", min_value=1, step=1)

        with col2:
            salario = st.number_input("Salário", min_value=0.0, step=0.01, format="%.2f")
            data_admissao = st.date_input("Data de admissão", value=date.today())
            cargo_nome = st.text_input("Cargo")

        cargo_descricao = st.text_input("Descrição do cargo")

        st.markdown("### Endereço")
        col3, col4, col5 = st.columns(3)
        with col3:
            logradouro = st.text_input("Logradouro")
            numero = st.text_input("Número")
        with col4:
            bairro = st.text_input("Bairro")
            cidade = st.text_input("Cidade")
        with col5:
            estado = st.text_input("Estado")
            cep = st.text_input("CEP")

        st.markdown("### Telefones")
        telefones_texto = st.text_area(
            "Informe um telefone por linha no formato: Tipo - Número",
            placeholder="Celular - (83) 99999-0000\nResidencial - (83) 3222-0000"
        )

        enviar_funcionario = st.form_submit_button("Cadastrar funcionário")

        if enviar_funcionario:
            if not nome.strip():
                st.error("Informe o nome do funcionário.")
            elif not cargo_nome.strip():
                st.error("Informe o cargo do funcionário.")
            else:
                endereco = criar_endereco(logradouro, numero, bairro, cidade, estado, cep)
                telefones = criar_lista_telefones(telefones_texto)
                cargo = Cargo(nome=cargo_nome.strip(), descricao=cargo_descricao.strip())

                funcionario = Funcionario(
                    matricula=int(matricula),
                    nome=nome.strip(),
                    data_nascimento=data_nascimento,
                    endereco=endereco,
                    telefones=telefones,
                    cargo=cargo,
                    salario=float(salario),
                    data_admissao=data_admissao
                )

                st.session_state.funcionarios.append(funcionario)
                st.success(funcionario.cadastrar())


# =========================================================
# ABA 3 - CADASTRAR CLIENTE
# =========================================================
with aba3:
    st.subheader("Cadastro de cliente")

    with st.form("form_cliente", clear_on_submit=True):
        st.markdown("### Dados pessoais")
        col1, col2 = st.columns(2)

        with col1:
            nome_cliente = st.text_input("Nome", key="nome_cliente")
            data_nascimento_cliente = st.date_input(
                "Data de nascimento",
                value=date(2000, 1, 1),
                key="data_nascimento_cliente"
            )

        with col2:
            codigo = st.text_input("Código do cliente")
            profissao_nome = st.text_input("Profissão")

        profissao_descricao = st.text_input("Descrição da profissão")

        st.markdown("### Endereço")
        col3, col4, col5 = st.columns(3)
        with col3:
            logradouro_cliente = st.text_input("Logradouro", key="logradouro_cliente")
            numero_cliente = st.text_input("Número", key="numero_cliente")
        with col4:
            bairro_cliente = st.text_input("Bairro", key="bairro_cliente")
            cidade_cliente = st.text_input("Cidade", key="cidade_cliente")
        with col5:
            estado_cliente = st.text_input("Estado", key="estado_cliente")
            cep_cliente = st.text_input("CEP", key="cep_cliente")

        st.markdown("### Telefones")
        telefones_cliente_texto = st.text_area(
            "Informe um telefone por linha no formato: Tipo - Número",
            placeholder="Celular - (83) 98888-0000",
            key="telefones_cliente"
        )

        enviar_cliente = st.form_submit_button("Cadastrar cliente")

        if enviar_cliente:
            if not nome_cliente.strip():
                st.error("Informe o nome do cliente.")
            elif not codigo.strip():
                st.error("Informe o código do cliente.")
            else:
                endereco_cliente = criar_endereco(
                    logradouro_cliente,
                    numero_cliente,
                    bairro_cliente,
                    cidade_cliente,
                    estado_cliente,
                    cep_cliente
                )
                telefones_cliente = criar_lista_telefones(telefones_cliente_texto)
                profissao = Profissao(
                    nome=profissao_nome.strip(),
                    descricao=profissao_descricao.strip()
                )

                cliente = Cliente(
                    codigo=codigo.strip(),
                    nome=nome_cliente.strip(),
                    data_nascimento=data_nascimento_cliente,
                    endereco=endereco_cliente,
                    telefones=telefones_cliente,
                    profissao=profissao
                )

                st.session_state.clientes.append(cliente)
                st.success(cliente.cadastrar())


# =========================================================
# ABA 4 - LISTAGENS
# =========================================================
with aba4:
    st.subheader("Funcionários cadastrados")
    df_funcionarios = funcionarios_para_dataframe()
    if df_funcionarios.empty:
        st.info("Nenhum funcionário cadastrado.")
    else:
        st.dataframe(df_funcionarios, use_container_width=True)

        st.markdown("### Reajuste salarial")
        nomes_func = [f"{f.matricula} - {f.nome}" for f in st.session_state.funcionarios]
        selecionado = st.selectbox("Selecione um funcionário", options=nomes_func)
        percentual = st.number_input("Percentual de reajuste", min_value=0.0, step=1.0, format="%.2f")

        if st.button("Aplicar reajuste"):
            matricula_selecionada = int(selecionado.split(" - ")[0])
            funcionario = next(
                (f for f in st.session_state.funcionarios if f.matricula == matricula_selecionada),
                None
            )
            if funcionario:
                novo_salario = funcionario.reajustar_salario(percentual)
                st.success(
                    f"Novo salário de {funcionario.nome}: R$ {novo_salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                )
                st.rerun()

    st.markdown("---")
    st.subheader("Clientes cadastrados")
    df_clientes = clientes_para_dataframe()
    if df_clientes.empty:
        st.info("Nenhum cliente cadastrado.")
    else:
        st.dataframe(df_clientes, use_container_width=True)