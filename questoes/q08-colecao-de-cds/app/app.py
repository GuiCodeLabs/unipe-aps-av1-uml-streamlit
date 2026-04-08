import streamlit as st
import pandas as pd
from dataclasses import dataclass, field
from typing import List, Optional


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Questão 08 - Coleção de CDs",
    page_icon="💿",
    layout="wide"
)


# =========================================================
# MODELO ORIENTADO A OBJETOS
# =========================================================
@dataclass
class Artista:
    nome: str

    def cadastrar(self) -> str:
        return f"Artista '{self.nome}' cadastrado com sucesso."

    def editarNome(self, novo_nome: str) -> None:
        self.nome = novo_nome.strip()

    def obterNome(self) -> str:
        return self.nome


@dataclass
class CD:
    titulo: str
    anoLancamento: int
    artista: Artista

    def cadastrar(self) -> str:
        return f"CD '{self.titulo}' cadastrado com sucesso."

    def editar(self, novo_titulo: str, novo_ano: int, novo_artista: Artista) -> None:
        self.titulo = novo_titulo.strip()
        self.anoLancamento = int(novo_ano)
        self.artista = novo_artista

    def excluir(self) -> str:
        return f"CD '{self.titulo}' excluído com sucesso."

    def obterDescricao(self) -> str:
        return f"{self.titulo} ({self.anoLancamento}) - {self.artista.obterNome()}"


@dataclass
class ColecaoCDs:
    cds: List[CD] = field(default_factory=list)

    def adicionarCD(self, cd: CD) -> None:
        self.cds.append(cd)

    def removerCD(self, cd: CD) -> None:
        self.cds.remove(cd)

    def listarCDs(self) -> List[CD]:
        return self.cds

    def buscarPorTitulo(self, titulo: str) -> List[CD]:
        termo = titulo.strip().lower()
        return [cd for cd in self.cds if termo in cd.titulo.lower()]

    def buscarPorArtista(self, nomeArtista: str) -> List[CD]:
        termo = nomeArtista.strip().lower()
        return [cd for cd in self.cds if termo in cd.artista.obterNome().lower()]


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
def inicializar_estado():
    if "artistas" not in st.session_state:
        st.session_state.artistas = []

    if "colecao" not in st.session_state:
        st.session_state.colecao = ColecaoCDs()

    if "dados_iniciais" not in st.session_state:
        artista1 = Artista("Legião Urbana")
        artista2 = Artista("Titãs")

        st.session_state.artistas.extend([artista1, artista2])

        st.session_state.colecao.adicionarCD(CD("Dois", 1986, artista1))
        st.session_state.colecao.adicionarCD(CD("Cabeça Dinossauro", 1986, artista2))

        st.session_state.dados_iniciais = True


def obter_artista_por_nome(nome: str) -> Optional[Artista]:
    for artista in st.session_state.artistas:
        if artista.obterNome() == nome:
            return artista
    return None


def artista_ja_existe(nome: str) -> bool:
    return any(a.obterNome().lower() == nome.strip().lower() for a in st.session_state.artistas)


def cd_ja_existe(titulo: str, artista_nome: str) -> bool:
    for cd in st.session_state.colecao.listarCDs():
        if cd.titulo.lower() == titulo.strip().lower() and cd.artista.obterNome().lower() == artista_nome.strip().lower():
            return True
    return False


def converter_para_dataframe(lista_cds: List[CD]) -> pd.DataFrame:
    if not lista_cds:
        return pd.DataFrame()

    dados = []
    for i, cd in enumerate(lista_cds):
        dados.append({
            "Índice": i,
            "Título": cd.titulo,
            "Ano de Lançamento": cd.anoLancamento,
            "Artista": cd.artista.obterNome(),
            "Descrição": cd.obterDescricao()
        })
    return pd.DataFrame(dados)


# =========================================================
# INICIALIZAÇÃO
# =========================================================
inicializar_estado()

st.title("💿 Questão 08 — Coleção de CDs")
st.markdown(
    """
Aplicação em **Python + Streamlit** baseada no diagrama de classes enviado,
para gerenciar uma coleção de CDs com **artistas**, **cadastro**, **listagem** e **buscas**.
"""
)

aba1, aba2, aba3, aba4 = st.tabs([
    "Cadastrar Artista",
    "Cadastrar CD",
    "Listagem e Busca",
    "Gerenciar Registros"
])


# =========================================================
# ABA 1 - CADASTRO DE ARTISTA
# =========================================================
with aba1:
    st.subheader("Cadastrar artista")

    with st.form("form_artista", clear_on_submit=True):
        nome_artista = st.text_input("Nome do artista ou conjunto")
        salvar_artista = st.form_submit_button("Cadastrar artista")

        if salvar_artista:
            if not nome_artista.strip():
                st.error("Informe o nome do artista.")
            elif artista_ja_existe(nome_artista):
                st.warning("Esse artista já está cadastrado.")
            else:
                novo_artista = Artista(nome_artista.strip())
                st.session_state.artistas.append(novo_artista)
                st.success(novo_artista.cadastrar())


# =========================================================
# ABA 2 - CADASTRO DE CD
# =========================================================
with aba2:
    st.subheader("Cadastrar CD")

    if not st.session_state.artistas:
        st.info("Cadastre pelo menos um artista antes de cadastrar um CD.")
    else:
        with st.form("form_cd", clear_on_submit=True):
            titulo = st.text_input("Título do CD")
            ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, step=1, value=2020)
            artista_escolhido = st.selectbox(
                "Artista",
                options=[artista.obterNome() for artista in st.session_state.artistas]
            )

            salvar_cd = st.form_submit_button("Cadastrar CD")

            if salvar_cd:
                if not titulo.strip():
                    st.error("Informe o título do CD.")
                elif cd_ja_existe(titulo, artista_escolhido):
                    st.warning("Esse CD já está cadastrado para esse artista.")
                else:
                    artista_obj = obter_artista_por_nome(artista_escolhido)
                    novo_cd = CD(titulo.strip(), int(ano), artista_obj)
                    st.session_state.colecao.adicionarCD(novo_cd)
                    st.success(novo_cd.cadastrar())


# =========================================================
# ABA 3 - LISTAGEM E BUSCA
# =========================================================
with aba3:
    st.subheader("Listagem da coleção")

    cds = st.session_state.colecao.listarCDs()
    df = converter_para_dataframe(cds)

    if df.empty:
        st.info("Nenhum CD cadastrado.")
    else:
        st.dataframe(df[["Título", "Ano de Lançamento", "Artista", "Descrição"]], use_container_width=True)

    st.markdown("---")
    st.subheader("Buscar CDs")

    col1, col2 = st.columns(2)

    with col1:
        termo_titulo = st.text_input("Buscar por título")
        if st.button("Pesquisar título"):
            resultados = st.session_state.colecao.buscarPorTitulo(termo_titulo)
            df_resultado = converter_para_dataframe(resultados)

            if df_resultado.empty:
                st.warning("Nenhum CD encontrado com esse título.")
            else:
                st.success(f"{len(df_resultado)} CD(s) encontrado(s).")
                st.dataframe(df_resultado[["Título", "Ano de Lançamento", "Artista"]], use_container_width=True)

    with col2:
        termo_artista = st.text_input("Buscar por artista")
        if st.button("Pesquisar artista"):
            resultados = st.session_state.colecao.buscarPorArtista(termo_artista)
            df_resultado = converter_para_dataframe(resultados)

            if df_resultado.empty:
                st.warning("Nenhum CD encontrado para esse artista.")
            else:
                st.success(f"{len(df_resultado)} CD(s) encontrado(s).")
                st.dataframe(df_resultado[["Título", "Ano de Lançamento", "Artista"]], use_container_width=True)


# =========================================================
# ABA 4 - GERENCIAR REGISTROS
# =========================================================
with aba4:
    st.subheader("Editar artista")

    if st.session_state.artistas:
        nomes_artistas = [artista.obterNome() for artista in st.session_state.artistas]
        artista_selecionado_nome = st.selectbox("Selecione um artista", nomes_artistas, key="artista_edicao")
        artista_obj = obter_artista_por_nome(artista_selecionado_nome)

        with st.form("form_editar_artista"):
            novo_nome_artista = st.text_input("Novo nome do artista", value=artista_obj.obterNome())
            salvar_edicao_artista = st.form_submit_button("Salvar nome do artista")

            if salvar_edicao_artista:
                if not novo_nome_artista.strip():
                    st.error("Informe um nome válido.")
                else:
                    artista_obj.editarNome(novo_nome_artista)
                    st.success("Nome do artista atualizado com sucesso.")
                    st.rerun()
    else:
        st.info("Nenhum artista cadastrado.")

    st.markdown("---")
    st.subheader("Editar ou excluir CD")

    cds = st.session_state.colecao.listarCDs()

    if cds:
        mapa_cds = {
            f"{i} - {cd.obterDescricao()}": i
            for i, cd in enumerate(cds)
        }

        cd_chave = st.selectbox("Selecione um CD", list(mapa_cds.keys()))
        cd_indice = mapa_cds[cd_chave]
        cd_obj = cds[cd_indice]

        with st.form("form_editar_cd"):
            novo_titulo = st.text_input("Título", value=cd_obj.titulo)
            novo_ano = st.number_input(
                "Ano de lançamento",
                min_value=1900,
                max_value=2100,
                step=1,
                value=int(cd_obj.anoLancamento)
            )

            artista_nomes = [artista.obterNome() for artista in st.session_state.artistas]
            indice_artista_atual = artista_nomes.index(cd_obj.artista.obterNome())

            novo_artista_nome = st.selectbox(
                "Artista",
                options=artista_nomes,
                index=indice_artista_atual
            )

            col_btn1, col_btn2 = st.columns(2)
            salvar_cd = col_btn1.form_submit_button("Salvar alterações")
            excluir_cd_btn = col_btn2.form_submit_button("Excluir CD")

            if salvar_cd:
                if not novo_titulo.strip():
                    st.error("Informe o título do CD.")
                else:
                    novo_artista_obj = obter_artista_por_nome(novo_artista_nome)
                    cd_obj.editar(novo_titulo, int(novo_ano), novo_artista_obj)
                    st.success("CD atualizado com sucesso.")
                    st.rerun()

            if excluir_cd_btn:
                mensagem = cd_obj.excluir()
                st.session_state.colecao.removerCD(cd_obj)
                st.success(mensagem)
                st.rerun()
    else:
        st.info("Nenhum CD cadastrado para gerenciar.")