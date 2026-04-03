import streamlit as st
from enum import Enum


class Direcao(Enum):
    CIMA = "Cima"
    BAIXO = "Baixo"
    ESQUERDA = "Esquerda"
    DIREITA = "Direita"


class Boneco:
    def __init__(self, nome: str, posicao_x: int = 0, posicao_y: int = 0, direcao_atual: Direcao = Direcao.CIMA):
        self.nome = nome
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.direcao_atual = direcao_atual

    def mover(self):
        if self.direcao_atual == Direcao.CIMA:
            self.posicao_y += 1
        elif self.direcao_atual == Direcao.BAIXO:
            self.posicao_y -= 1
        elif self.direcao_atual == Direcao.DIREITA:
            self.posicao_x += 1
        elif self.direcao_atual == Direcao.ESQUERDA:
            self.posicao_x -= 1

    def mover_cima(self):
        self.direcao_atual = Direcao.CIMA
        self.mover()

    def mover_baixo(self):
        self.direcao_atual = Direcao.BAIXO
        self.mover()

    def mover_esquerda(self):
        self.direcao_atual = Direcao.ESQUERDA
        self.mover()

    def mover_direita(self):
        self.direcao_atual = Direcao.DIREITA
        self.mover()

    def alterar_direcao(self, nova_direcao: Direcao):
        self.direcao_atual = nova_direcao

    def exibir_posicao(self) -> str:
        return f"({self.posicao_x}, {self.posicao_y})"

    def exibir_estado(self) -> str:
        return (
            f"Nome: {self.nome} | "
            f"Posição X: {self.posicao_x} | "
            f"Posição Y: {self.posicao_y} | "
            f"Direção: {self.direcao_atual.value}"
        )

    def reiniciar_posicao(self):
        self.posicao_x = 0
        self.posicao_y = 0
        self.direcao_atual = Direcao.CIMA


def inicializar_boneco():
    if "boneco" not in st.session_state:
        st.session_state.boneco = Boneco("Boneco")


def desenhar_area(posicao_x: int, posicao_y: int, tamanho: int = 11) -> str:
    grade = []
    centro = tamanho // 2

    for y in range(tamanho - 1, -1, -1):
        linha = []
        for x in range(tamanho):
            eixo_x = x - centro
            eixo_y = y - centro

            if eixo_x == posicao_x and eixo_y == posicao_y:
                linha.append("B")
            elif eixo_x == 0 and eixo_y == 0:
                linha.append("+")
            else:
                linha.append(".")
        grade.append(" ".join(linha))

    return "\n".join(grade)


st.set_page_config(page_title="Questão 3 - Boneco em Movimento", page_icon="🕹️", layout="centered")

inicializar_boneco()
boneco = st.session_state.boneco

st.title("Questão 3 - Boneco em Movimento")
st.markdown("Aplicação em Python com Streamlit para movimentar um boneco na tela.")

with st.container():
    st.subheader("Dados do boneco")

    col1, col2, col3 = st.columns(3)

    with col1:
        nome = st.text_input("Nome", value=boneco.nome)

    with col2:
        posicao_x = st.number_input("Posição X", value=boneco.posicao_x, step=1)

    with col3:
        posicao_y = st.number_input("Posição Y", value=boneco.posicao_y, step=1)

    direcao = st.selectbox(
        "Direção atual",
        options=[d.value for d in Direcao],
        index=list(Direcao).index(boneco.direcao_atual)
    )

    if st.button("Salvar dados"):
        boneco.nome = nome.strip() if nome.strip() else "Boneco"
        boneco.posicao_x = int(posicao_x)
        boneco.posicao_y = int(posicao_y)
        boneco.alterar_direcao(Direcao(direcao))
        st.success("Dados do boneco atualizados com sucesso.")

st.divider()

st.subheader("Movimentação")

col_a, col_b, col_c = st.columns([1, 1, 1])

with col_b:
    if st.button("⬆️ Cima", use_container_width=True):
        boneco.mover_cima()

col_d, col_e, col_f = st.columns([1, 1, 1])

with col_d:
    if st.button("⬅️ Esquerda", use_container_width=True):
        boneco.mover_esquerda()

with col_e:
    if st.button("🔄 Reiniciar", use_container_width=True):
        boneco.reiniciar_posicao()

with col_f:
    if st.button("➡️ Direita", use_container_width=True):
        boneco.mover_direita()

with col_b:
    if st.button("⬇️ Baixo", use_container_width=True):
        boneco.mover_baixo()

st.divider()

st.subheader("Estado atual do boneco")
st.info(boneco.exibir_estado())

col_info1, col_info2 = st.columns(2)
with col_info1:
    st.metric("Posição atual", boneco.exibir_posicao())
with col_info2:
    st.metric("Direção", boneco.direcao_atual.value)

st.subheader("Visualização da área")
st.caption("B = Boneco | + = origem (0,0)")
st.code(desenhar_area(boneco.posicao_x, boneco.posicao_y), language="text")