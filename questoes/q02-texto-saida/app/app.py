import streamlit as st
import pandas as pd


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Questão 02 - TextoSaída",
    page_icon="📝",
    layout="wide"
)


# =========================================================
# CLASSE DO DIAGRAMA
# =========================================================
class TextoSaida:
    def __init__(
        self,
        conteudo: str = "",
        tamanho_letra: int = 16,
        cor_fonte: str = "preto",
        cor_fundo: str = "branco",
        tipo_componente: str = "label",
    ):
        self.conteudo = conteudo
        self.tamanhoLetra = tamanho_letra
        self.corFonte = cor_fonte
        self.corFundo = cor_fundo
        self.tipoComponente = tipo_componente

    def definirTexto(self, texto: str):
        self.conteudo = texto

    def alterarTamanhoLetra(self, tamanho: int):
        self.tamanhoLetra = tamanho

    def alterarCorFonte(self, cor: str):
        self.corFonte = cor

    def alterarCorFundo(self, cor: str):
        self.corFundo = cor

    def definirTipoComponente(self, tipo: str):
        self.tipoComponente = tipo

    def exibir(self) -> str:
        cor_fonte_css = mapear_cor_css(self.corFonte)
        cor_fundo_css = mapear_cor_css(self.corFundo)

        conteudo_seguro = (
            self.conteudo.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        estilo_base = f"""
            font-size: {self.tamanhoLetra}px;
            color: {cor_fonte_css};
            background-color: {cor_fundo_css};
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #cccccc;
            margin-top: 8px;
            white-space: pre-wrap;
            word-break: break-word;
        """

        if self.tipoComponente == "label":
            return f"""
            <div style="{estilo_base}">
                {conteudo_seguro}
            </div>
            """

        if self.tipoComponente == "edit":
            return f"""
            <input
                type="text"
                value="{conteudo_seguro}"
                readonly
                style="{estilo_base} width: 100%; box-sizing: border-box;"
            />
            """

        if self.tipoComponente == "memo":
            return f"""
            <textarea
                readonly
                style="{estilo_base} width: 100%; height: 180px; box-sizing: border-box; resize: none;"
            >{conteudo_seguro}</textarea>
            """

        return f"""
        <div style="{estilo_base}">
            {conteudo_seguro}
        </div>
        """


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def mapear_cor_css(cor: str) -> str:
    mapa = {
        "preto": "black",
        "branco": "white",
        "azul": "blue",
        "amarelo": "#FFD700",
        "cinza": "gray",
    }
    return mapa.get(cor.lower(), "black")


def inicializar_estado():
    if "objetos_texto" not in st.session_state:
        st.session_state.objetos_texto = []

    if "proximo_id" not in st.session_state:
        st.session_state.proximo_id = 1


def adicionar_objeto(texto_saida: TextoSaida):
    registro = {
        "id": st.session_state.proximo_id,
        "conteudo": texto_saida.conteudo,
        "tamanhoLetra": texto_saida.tamanhoLetra,
        "corFonte": texto_saida.corFonte,
        "corFundo": texto_saida.corFundo,
        "tipoComponente": texto_saida.tipoComponente,
    }
    st.session_state.objetos_texto.append(registro)
    st.session_state.proximo_id += 1


def obter_objeto_por_id(objeto_id: int):
    for item in st.session_state.objetos_texto:
        if item["id"] == objeto_id:
            return item
    return None


def atualizar_objeto(objeto_id: int, texto_saida: TextoSaida):
    for item in st.session_state.objetos_texto:
        if item["id"] == objeto_id:
            item["conteudo"] = texto_saida.conteudo
            item["tamanhoLetra"] = texto_saida.tamanhoLetra
            item["corFonte"] = texto_saida.corFonte
            item["corFundo"] = texto_saida.corFundo
            item["tipoComponente"] = texto_saida.tipoComponente
            break


def excluir_objeto(objeto_id: int):
    st.session_state.objetos_texto = [
        item for item in st.session_state.objetos_texto if item["id"] != objeto_id
    ]


def listar_objetos_dataframe():
    if not st.session_state.objetos_texto:
        return pd.DataFrame()

    return pd.DataFrame(
        [
            {
                "ID": item["id"],
                "Conteúdo": item["conteudo"],
                "Tamanho da Letra": item["tamanhoLetra"],
                "Cor da Fonte": item["corFonte"],
                "Cor do Fundo": item["corFundo"],
                "Tipo do Componente": item["tipoComponente"],
            }
            for item in st.session_state.objetos_texto
        ]
    )


def criar_objeto_texto(
    conteudo: str,
    tamanho_letra: int,
    cor_fonte: str,
    cor_fundo: str,
    tipo_componente: str,
) -> TextoSaida:
    obj = TextoSaida()
    obj.definirTexto(conteudo)
    obj.alterarTamanhoLetra(tamanho_letra)
    obj.alterarCorFonte(cor_fonte)
    obj.alterarCorFundo(cor_fundo)
    obj.definirTipoComponente(tipo_componente)
    return obj


# =========================================================
# INÍCIO DA APLICAÇÃO
# =========================================================
inicializar_estado()

st.title("📝 Questão 02 — Classe TextoSaída")
st.markdown(
    """
Aplicação em **Python + Streamlit** baseada no diagrama da classe **TextoSaida**.

Ela permite:
- cadastrar configurações de texto
- visualizar os registros salvos
- editar e excluir registros
- renderizar o texto como **label**, **edit** ou **memo**
"""
)

cores_disponiveis = ["preto", "branco", "azul", "amarelo", "cinza"]
tipos_componentes = ["label", "edit", "memo"]

aba1, aba2, aba3 = st.tabs(
    ["Cadastro", "Listagem e Gerenciamento", "Visualização"]
)


# =========================================================
# ABA 1 - CADASTRO
# =========================================================
with aba1:
    st.subheader("Cadastrar novo TextoSaida")

    with st.form("form_cadastro", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            conteudo = st.text_area("Conteúdo", height=120)
            tamanho_letra = st.slider("Tamanho da letra", min_value=8, max_value=48, value=16)

        with col2:
            cor_fonte = st.selectbox("Cor da fonte", cores_disponiveis)
            cor_fundo = st.selectbox("Cor do fundo", cores_disponiveis, index=1)
            tipo_componente = st.selectbox("Tipo do componente", tipos_componentes)

        salvar = st.form_submit_button("Cadastrar")

        if salvar:
            if not conteudo.strip():
                st.error("Informe um conteúdo para o texto.")
            else:
                novo_objeto = criar_objeto_texto(
                    conteudo=conteudo.strip(),
                    tamanho_letra=tamanho_letra,
                    cor_fonte=cor_fonte,
                    cor_fundo=cor_fundo,
                    tipo_componente=tipo_componente,
                )
                adicionar_objeto(novo_objeto)
                st.success("TextoSaida cadastrado com sucesso.")

    st.markdown("---")
    st.subheader("Pré-visualização rápida")

    preview = criar_objeto_texto(
        conteudo="Exemplo de visualização",
        tamanho_letra=18,
        cor_fonte="azul",
        cor_fundo="amarelo",
        tipo_componente="label",
    )
    st.components.v1.html(preview.exibir(), height=100, scrolling=False)


# =========================================================
# ABA 2 - LISTAGEM E GERENCIAMENTO
# =========================================================
with aba2:
    st.subheader("Textos cadastrados")

    df = listar_objetos_dataframe()

    if df.empty:
        st.info("Nenhum registro cadastrado até o momento.")
    else:
        st.dataframe(df, use_container_width=True)

        st.markdown("---")
        st.subheader("Editar ou excluir")

        opcoes = {
            f'ID {item["id"]} - {item["tipoComponente"]} - {item["conteudo"][:30]}': item["id"]
            for item in st.session_state.objetos_texto
        }

        selecionado = st.selectbox("Selecione um registro", list(opcoes.keys()))
        objeto_id = opcoes[selecionado]
        objeto = obter_objeto_por_id(objeto_id)

        if objeto:
            with st.form("form_edicao"):
                col1, col2 = st.columns(2)

                with col1:
                    novo_conteudo = st.text_area("Conteúdo", value=objeto["conteudo"], height=120)
                    novo_tamanho = st.slider(
                        "Tamanho da letra",
                        min_value=8,
                        max_value=48,
                        value=int(objeto["tamanhoLetra"]),
                        key=f"tam_{objeto_id}",
                    )

                with col2:
                    nova_cor_fonte = st.selectbox(
                        "Cor da fonte",
                        cores_disponiveis,
                        index=cores_disponiveis.index(objeto["corFonte"]),
                        key=f"cf_{objeto_id}",
                    )
                    nova_cor_fundo = st.selectbox(
                        "Cor do fundo",
                        cores_disponiveis,
                        index=cores_disponiveis.index(objeto["corFundo"]),
                        key=f"cb_{objeto_id}",
                    )
                    novo_tipo = st.selectbox(
                        "Tipo do componente",
                        tipos_componentes,
                        index=tipos_componentes.index(objeto["tipoComponente"]),
                        key=f"tp_{objeto_id}",
                    )

                col_btn1, col_btn2 = st.columns(2)
                btn_salvar = col_btn1.form_submit_button("Salvar alterações")
                btn_excluir = col_btn2.form_submit_button("Excluir registro")

                if btn_salvar:
                    if not novo_conteudo.strip():
                        st.error("Informe um conteúdo para o texto.")
                    else:
                        obj_editado = criar_objeto_texto(
                            conteudo=novo_conteudo.strip(),
                            tamanho_letra=novo_tamanho,
                            cor_fonte=nova_cor_fonte,
                            cor_fundo=nova_cor_fundo,
                            tipo_componente=novo_tipo,
                        )
                        atualizar_objeto(objeto_id, obj_editado)
                        st.success("Registro atualizado com sucesso.")
                        st.rerun()

                if btn_excluir:
                    excluir_objeto(objeto_id)
                    st.success("Registro excluído com sucesso.")
                    st.rerun()


# =========================================================
# ABA 3 - VISUALIZAÇÃO
# =========================================================
with aba3:
    st.subheader("Visualizar componente")

    if not st.session_state.objetos_texto:
        st.info("Cadastre um texto para visualizar.")
    else:
        opcoes_visualizacao = {
            f'ID {item["id"]} - {item["tipoComponente"]}': item["id"]
            for item in st.session_state.objetos_texto
        }

        item_escolhido = st.selectbox(
            "Escolha um registro para renderizar",
            list(opcoes_visualizacao.keys()),
        )

        item_id = opcoes_visualizacao[item_escolhido]
        item = obter_objeto_por_id(item_id)

        if item:
            texto_saida = TextoSaida(
                conteudo=item["conteudo"],
                tamanho_letra=item["tamanhoLetra"],
                cor_fonte=item["corFonte"],
                cor_fundo=item["corFundo"],
                tipo_componente=item["tipoComponente"],
            )

            st.write("### Dados do objeto")
            st.write(f'**Conteúdo:** {item["conteudo"]}')
            st.write(f'**Tamanho da letra:** {item["tamanhoLetra"]}')
            st.write(f'**Cor da fonte:** {item["corFonte"]}')
            st.write(f'**Cor do fundo:** {item["corFundo"]}')
            st.write(f'**Tipo do componente:** {item["tipoComponente"]}')

            st.markdown("---")
            st.write("### Resultado do método exibir()")
            altura = 120 if item["tipoComponente"] != "memo" else 240
            st.components.v1.html(texto_saida.exibir(), height=altura, scrolling=False)