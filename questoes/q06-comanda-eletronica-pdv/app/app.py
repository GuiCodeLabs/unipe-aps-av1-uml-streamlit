from dataclasses import dataclass, field
from typing import List, Optional

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Questão 06 - Comanda Eletrônica (PDV)",
    page_icon="🧾",
    layout="wide"
)


# =========================================================
# MODELO ORIENTADO A OBJETOS
# =========================================================
@dataclass
class Produto:
    codigo: int
    nome: str
    valor_unitario: float

    def cadastrar(self) -> dict:
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "valor_unitario": self.valor_unitario
        }

    def editar_preco(self, novo_preco: float) -> None:
        self.valor_unitario = float(novo_preco)


@dataclass
class ItemComanda:
    quantidade: int
    produto: Produto

    def calcular_subtotal(self) -> float:
        return self.quantidade * self.produto.valor_unitario


@dataclass
class Comanda:
    numero: int
    status: str = "Aberta"
    itens: List[ItemComanda] = field(default_factory=list)

    def adicionar_item(self, produto: Produto, quantidade: int) -> None:
        if self.status != "Aberta":
            raise ValueError("A comanda já está finalizada.")

        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        for item in self.itens:
            if item.produto.codigo == produto.codigo:
                item.quantidade += quantidade
                return

        self.itens.append(ItemComanda(quantidade=quantidade, produto=produto))

    def remover_item(self, codigo_produto: int) -> None:
        if self.status != "Aberta":
            raise ValueError("Não é possível remover itens de uma comanda finalizada.")

        self.itens = [
            item for item in self.itens
            if item.produto.codigo != codigo_produto
        ]

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.itens)

    def finalizar_compra(self) -> None:
        if not self.itens:
            raise ValueError("Não é possível finalizar uma comanda sem itens.")
        self.status = "Finalizada"


class Caixa:
    def __init__(self):
        self.comandas: List[Comanda] = []

    def abrir_comanda(self, numero: int) -> Comanda:
        if self.buscar_comanda(numero) is not None:
            raise ValueError("Já existe uma comanda com esse número.")

        comanda = Comanda(numero=numero)
        self.comandas.append(comanda)
        return comanda

    def buscar_comanda(self, numero: int) -> Optional[Comanda]:
        for comanda in self.comandas:
            if comanda.numero == numero:
                return comanda
        return None

    def registrar_consumo(self, numero_comanda: int, produto: Produto, quantidade: int) -> None:
        comanda = self.buscar_comanda(numero_comanda)
        if comanda is None:
            raise ValueError("Comanda não encontrada.")
        comanda.adicionar_item(produto, quantidade)

    def listar_itens(self, numero_comanda: int) -> List[ItemComanda]:
        comanda = self.buscar_comanda(numero_comanda)
        if comanda is None:
            raise ValueError("Comanda não encontrada.")
        return comanda.itens

    def fechar_comanda(self, numero_comanda: int) -> float:
        comanda = self.buscar_comanda(numero_comanda)
        if comanda is None:
            raise ValueError("Comanda não encontrada.")

        total = comanda.calcular_total()
        comanda.finalizar_compra()
        return total


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
def inicializar_estado() -> None:
    if "produtos" not in st.session_state:
        st.session_state.produtos = []

    if "caixa" not in st.session_state:
        st.session_state.caixa = Caixa()

    if "dados_iniciais_carregados" not in st.session_state:
        carregar_dados_iniciais()
        st.session_state.dados_iniciais_carregados = True


def carregar_dados_iniciais() -> None:
    produtos_iniciais = [
        Produto(1, "Pão Francês", 0.80),
        Produto(2, "Café", 3.50),
        Produto(3, "Bolo de Chocolate", 6.00),
        Produto(4, "Suco de Laranja", 5.50),
    ]

    st.session_state.produtos = produtos_iniciais

    caixa = st.session_state.caixa
    try:
        caixa.abrir_comanda(101)
        caixa.registrar_consumo(101, produtos_iniciais[0], 4)
        caixa.registrar_consumo(101, produtos_iniciais[1], 2)

        caixa.abrir_comanda(102)
        caixa.registrar_consumo(102, produtos_iniciais[2], 1)
    except ValueError:
        pass


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def obter_produto_por_codigo(codigo: int) -> Optional[Produto]:
    for produto in st.session_state.produtos:
        if produto.codigo == codigo:
            return produto
    return None


def produtos_para_dataframe() -> pd.DataFrame:
    if not st.session_state.produtos:
        return pd.DataFrame()

    dados = []
    for produto in st.session_state.produtos:
        dados.append({
            "Código": produto.codigo,
            "Nome": produto.nome,
            "Valor Unitário": f"R$ {produto.valor_unitario:.2f}"
        })

    return pd.DataFrame(dados)


def comandas_para_dataframe() -> pd.DataFrame:
    caixa = st.session_state.caixa

    if not caixa.comandas:
        return pd.DataFrame()

    dados = []
    for comanda in caixa.comandas:
        dados.append({
            "Número": comanda.numero,
            "Status": comanda.status,
            "Qtd. Itens": len(comanda.itens),
            "Total": f"R$ {comanda.calcular_total():.2f}"
        })

    return pd.DataFrame(dados)


def itens_comanda_para_dataframe(comanda: Comanda) -> pd.DataFrame:
    if not comanda.itens:
        return pd.DataFrame()

    dados = []
    for item in comanda.itens:
        dados.append({
            "Código Produto": item.produto.codigo,
            "Produto": item.produto.nome,
            "Quantidade": item.quantidade,
            "Valor Unitário": f"R$ {item.produto.valor_unitario:.2f}",
            "Subtotal": f"R$ {item.calcular_subtotal():.2f}"
        })

    return pd.DataFrame(dados)


def cadastrar_produto(codigo: int, nome: str, valor_unitario: float) -> None:
    if obter_produto_por_codigo(codigo) is not None:
        raise ValueError("Já existe um produto com esse código.")

    produto = Produto(codigo=codigo, nome=nome.strip(), valor_unitario=float(valor_unitario))
    st.session_state.produtos.append(produto)


# =========================================================
# INTERFACE
# =========================================================
inicializar_estado()

st.title("🧾 Questão 06 — Comanda Eletrônica (PDV)")
st.markdown(
    """
Aplicação web baseada no diagrama de classes da imagem, com as classes
**Produto**, **ItemComanda**, **Comanda** e **Caixa**.
"""
)

aba1, aba2, aba3 = st.tabs(["Produtos", "Comandas", "Caixa / Fechamento"])


# =========================================================
# ABA 1 - PRODUTOS
# =========================================================
with aba1:
    st.subheader("Cadastro e visualização de produtos")

    with st.form("form_produto", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            codigo = st.number_input("Código", min_value=1, step=1)
        with col2:
            nome = st.text_input("Nome do produto")
        with col3:
            valor_unitario = st.number_input(
                "Valor unitário (R$)",
                min_value=0.01,
                step=0.01,
                format="%.2f"
            )

        enviar_produto = st.form_submit_button("Cadastrar produto")

        if enviar_produto:
            try:
                if not nome.strip():
                    raise ValueError("Informe o nome do produto.")
                cadastrar_produto(int(codigo), nome, valor_unitario)
                st.success("Produto cadastrado com sucesso!")
            except ValueError as erro:
                st.error(str(erro))

    st.markdown("---")
    st.subheader("Produtos cadastrados")

    df_produtos = produtos_para_dataframe()
    if df_produtos.empty:
        st.info("Nenhum produto cadastrado.")
    else:
        st.dataframe(df_produtos, use_container_width=True)

        st.markdown("---")
        st.subheader("Editar preço do produto")

        opcoes_produtos = {
            f"{produto.codigo} - {produto.nome}": produto.codigo
            for produto in st.session_state.produtos
        }

        produto_escolhido = st.selectbox(
            "Selecione o produto",
            options=list(opcoes_produtos.keys())
        )

        produto_codigo = opcoes_produtos[produto_escolhido]
        produto = obter_produto_por_codigo(produto_codigo)

        if produto:
            with st.form("form_editar_preco"):
                novo_preco = st.number_input(
                    "Novo preço (R$)",
                    min_value=0.01,
                    value=float(produto.valor_unitario),
                    step=0.01,
                    format="%.2f"
                )
                salvar_preco = st.form_submit_button("Atualizar preço")

                if salvar_preco:
                    produto.editar_preco(novo_preco)
                    st.success("Preço atualizado com sucesso!")
                    st.rerun()


# =========================================================
# ABA 2 - COMANDAS
# =========================================================
with aba2:
    st.subheader("Abertura de comandas e registro de consumo")

    col_a, col_b = st.columns([1, 2])

    with col_a:
        with st.form("form_abrir_comanda", clear_on_submit=True):
            numero_comanda = st.number_input("Número da comanda", min_value=1, step=1)
            abrir = st.form_submit_button("Abrir comanda")

            if abrir:
                try:
                    st.session_state.caixa.abrir_comanda(int(numero_comanda))
                    st.success("Comanda aberta com sucesso!")
                except ValueError as erro:
                    st.error(str(erro))

    with col_b:
        if not st.session_state.produtos:
            st.warning("Cadastre produtos antes de registrar consumo.")
        else:
            comandas_abertas = [
                comanda for comanda in st.session_state.caixa.comandas
                if comanda.status == "Aberta"
            ]

            if not comandas_abertas:
                st.info("Não há comandas abertas no momento.")
            else:
                with st.form("form_registrar_consumo", clear_on_submit=True):
                    opcoes_comandas = {
                        f"Comanda {comanda.numero}": comanda.numero
                        for comanda in comandas_abertas
                    }
                    opcoes_produtos = {
                        f"{produto.codigo} - {produto.nome} (R$ {produto.valor_unitario:.2f})": produto.codigo
                        for produto in st.session_state.produtos
                    }

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        comanda_escolhida = st.selectbox("Comanda", list(opcoes_comandas.keys()))
                    with col2:
                        produto_escolhido = st.selectbox("Produto", list(opcoes_produtos.keys()))
                    with col3:
                        quantidade = st.number_input("Quantidade", min_value=1, step=1)

                    registrar = st.form_submit_button("Registrar consumo")

                    if registrar:
                        try:
                            numero = opcoes_comandas[comanda_escolhida]
                            codigo_produto = opcoes_produtos[produto_escolhido]
                            produto = obter_produto_por_codigo(codigo_produto)

                            if produto is None:
                                raise ValueError("Produto não encontrado.")

                            st.session_state.caixa.registrar_consumo(
                                numero_comanda=numero,
                                produto=produto,
                                quantidade=int(quantidade)
                            )
                            st.success("Consumo registrado com sucesso!")
                        except ValueError as erro:
                            st.error(str(erro))

    st.markdown("---")
    st.subheader("Comandas cadastradas")

    df_comandas = comandas_para_dataframe()
    if df_comandas.empty:
        st.info("Nenhuma comanda cadastrada.")
    else:
        st.dataframe(df_comandas, use_container_width=True)

        st.markdown("---")
        st.subheader("Visualizar itens da comanda")

        opcoes_todas = {
            f"Comanda {comanda.numero} - {comanda.status}": comanda.numero
            for comanda in st.session_state.caixa.comandas
        }

        escolha = st.selectbox("Selecione a comanda", list(opcoes_todas.keys()))
        numero = opcoes_todas[escolha]
        comanda = st.session_state.caixa.buscar_comanda(numero)

        if comanda:
            df_itens = itens_comanda_para_dataframe(comanda)

            if df_itens.empty:
                st.info("Essa comanda ainda não possui itens.")
            else:
                st.dataframe(df_itens, use_container_width=True)
                st.metric("Total atual da comanda", f"R$ {comanda.calcular_total():.2f}")

            if comanda.status == "Aberta" and comanda.itens:
                st.markdown("---")
                st.subheader("Remover item da comanda")

                mapa_itens = {
                    f"{item.produto.codigo} - {item.produto.nome}": item.produto.codigo
                    for item in comanda.itens
                }

                item_escolhido = st.selectbox(
                    "Selecione o item para remover",
                    list(mapa_itens.keys()),
                    key=f"remove_item_{comanda.numero}"
                )

                if st.button("Remover item", key=f"btn_remove_{comanda.numero}"):
                    codigo_item = mapa_itens[item_escolhido]
                    try:
                        comanda.remover_item(codigo_item)
                        st.success("Item removido com sucesso!")
                        st.rerun()
                    except ValueError as erro:
                        st.error(str(erro))


# =========================================================
# ABA 3 - CAIXA / FECHAMENTO
# =========================================================
with aba3:
    st.subheader("Fechamento de comandas")

    comandas_abertas = [
        comanda for comanda in st.session_state.caixa.comandas
        if comanda.status == "Aberta"
    ]

    if not comandas_abertas:
        st.info("Não há comandas abertas para fechamento.")
    else:
        opcoes_fechamento = {
            f"Comanda {comanda.numero} - Total R$ {comanda.calcular_total():.2f}": comanda.numero
            for comanda in comandas_abertas
        }

        escolha_fechamento = st.selectbox(
            "Selecione a comanda para fechar",
            options=list(opcoes_fechamento.keys())
        )

        numero_fechamento = opcoes_fechamento[escolha_fechamento]
        comanda_fechamento = st.session_state.caixa.buscar_comanda(numero_fechamento)

        if comanda_fechamento:
            df_itens_fechamento = itens_comanda_para_dataframe(comanda_fechamento)

            if not df_itens_fechamento.empty:
                st.dataframe(df_itens_fechamento, use_container_width=True)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Quantidade de itens", len(comanda_fechamento.itens))
            with col2:
                st.metric("Valor total", f"R$ {comanda_fechamento.calcular_total():.2f}")

            if st.button("Finalizar compra e fechar comanda"):
                try:
                    total = st.session_state.caixa.fechar_comanda(numero_fechamento)
                    st.success(
                        f"Compra finalizada com sucesso! "
                        f"Comanda {numero_fechamento} fechada. Total: R$ {total:.2f}"
                    )
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))

    st.markdown("---")
    st.subheader("Resumo geral")

    total_comandas = len(st.session_state.caixa.comandas)
    abertas = len([c for c in st.session_state.caixa.comandas if c.status == "Aberta"])
    finalizadas = len([c for c in st.session_state.caixa.comandas if c.status == "Finalizada"])
    faturamento = sum(
        comanda.calcular_total()
        for comanda in st.session_state.caixa.comandas
        if comanda.status == "Finalizada"
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de comandas", total_comandas)
    col2.metric("Abertas", abertas)
    col3.metric("Finalizadas", finalizadas)
    col4.metric("Faturamento", f"R$ {faturamento:.2f}")