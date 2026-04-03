import sqlite3
from pathlib import Path
from datetime import date, datetime

import pandas as pd
import streamlit as st


# =========================================================
# CONFIGURAÇÃO INICIAL
# =========================================================
st.set_page_config(
    page_title="Questão 07 - Lista de Compras",
    page_icon=":shopping_cart:",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"


# =========================================================
# BANCO DE DADOS
# =========================================================
def conectar():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_banco():
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unidades_compra (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                sigla TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS listas_mensais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                UNIQUE (mes, ano)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_lista (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lista_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                unidade_id INTEGER NOT NULL,
                quantidade_mes REAL NOT NULL,
                quantidade_compra REAL NOT NULL,
                preco_estimado REAL NOT NULL,
                FOREIGN KEY (lista_id) REFERENCES listas_mensais(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id),
                FOREIGN KEY (unidade_id) REFERENCES unidades_compra(id)
            )
        """)

        conn.commit()


def popular_dados_iniciais():
    produtos_padrao = [
        "Arroz",
        "Feijão",
        "Açúcar",
        "Carne",
        "Macarrão",
        "Leite"
    ]

    unidades_padrao = [
        ("Quilograma", "Kg"),
        ("Litro", "L"),
        ("Unidade", "Un"),
        ("Pacote", "Pct"),
        ("Caixa", "Cx")
    ]

    with conectar() as conn:
        cursor = conn.cursor()

        for produto in produtos_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO produtos (nome) VALUES (?)",
                (produto,)
            )

        for descricao, sigla in unidades_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO unidades_compra (descricao, sigla) VALUES (?, ?)",
                (descricao, sigla)
            )

        conn.commit()


# =========================================================
# FUNÇÕES DE DADOS
# =========================================================
def obter_ou_criar_lista(mes, ano):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM listas_mensais WHERE mes = ? AND ano = ?",
            (int(mes), int(ano))
        )
        registro = cursor.fetchone()

        if registro:
            return int(registro["id"])

        cursor.execute(
            "INSERT INTO listas_mensais (mes, ano) VALUES (?, ?)",
            (int(mes), int(ano))
        )
        conn.commit()
        return int(cursor.lastrowid)


def listar_produtos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM produtos ORDER BY nome")
        return cursor.fetchall()


def listar_unidades():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, sigla FROM unidades_compra ORDER BY descricao")
        return cursor.fetchall()


def adicionar_produto(nome):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome) VALUES (?)",
            (nome.strip(),)
        )
        conn.commit()


def adicionar_unidade(descricao, sigla):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO unidades_compra (descricao, sigla) VALUES (?, ?)",
            (descricao.strip(), sigla.strip())
        )
        conn.commit()


def adicionar_item(lista_id, produto_id, unidade_id, quantidade_mes, quantidade_compra, preco_estimado):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO itens_lista (
                lista_id,
                produto_id,
                unidade_id,
                quantidade_mes,
                quantidade_compra,
                preco_estimado
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            int(lista_id),
            int(produto_id),
            int(unidade_id),
            float(quantidade_mes),
            float(quantidade_compra),
            float(preco_estimado),
        ))
        conn.commit()


def listar_itens_da_lista(lista_id):
    with conectar() as conn:
        query = """
            SELECT
                i.id,
                p.nome AS produto,
                u.sigla AS unidade,
                i.quantidade_mes,
                i.quantidade_compra,
                i.preco_estimado,
                ROUND(i.quantidade_compra * i.preco_estimado, 2) AS subtotal,
                i.produto_id,
                i.unidade_id
            FROM itens_lista i
            INNER JOIN produtos p ON i.produto_id = p.id
            INNER JOIN unidades_compra u ON i.unidade_id = u.id
            WHERE i.lista_id = ?
            ORDER BY p.nome ASC, i.id ASC
        """
        return pd.read_sql_query(query, conn, params=(int(lista_id),))


def obter_item_por_id(item_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                id,
                lista_id,
                produto_id,
                unidade_id,
                quantidade_mes,
                quantidade_compra,
                preco_estimado
            FROM itens_lista
            WHERE id = ?
        """, (int(item_id),))
        return cursor.fetchone()


def atualizar_item(item_id, produto_id, unidade_id, quantidade_mes, quantidade_compra, preco_estimado):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE itens_lista
            SET produto_id = ?,
                unidade_id = ?,
                quantidade_mes = ?,
                quantidade_compra = ?,
                preco_estimado = ?
            WHERE id = ?
        """, (
            int(produto_id),
            int(unidade_id),
            float(quantidade_mes),
            float(quantidade_compra),
            float(preco_estimado),
            int(item_id)
        ))
        conn.commit()


def excluir_item(item_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM itens_lista WHERE id = ?", (int(item_id),))
        conn.commit()


def calcular_total_lista(lista_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COALESCE(SUM(quantidade_compra * preco_estimado), 0)
            FROM itens_lista
            WHERE lista_id = ?
        """, (int(lista_id),))
        valor = cursor.fetchone()[0]
        return float(valor or 0)


def resumo_por_produto(lista_id):
    with conectar() as conn:
        query = """
            SELECT
                p.nome AS Produto,
                u.sigla AS Unidade,
                ROUND(i.quantidade_mes, 2) AS "Qtd. Mês",
                ROUND(i.quantidade_compra, 2) AS "Qtd. Compra",
                ROUND(i.preco_estimado, 2) AS "Preço Estimado",
                ROUND(i.quantidade_compra * i.preco_estimado, 2) AS Subtotal
            FROM itens_lista i
            INNER JOIN produtos p ON i.produto_id = p.id
            INNER JOIN unidades_compra u ON i.unidade_id = u.id
            WHERE i.lista_id = ?
            ORDER BY p.nome ASC
        """
        return pd.read_sql_query(query, conn, params=(int(lista_id),))


def produtos_maior_subtotal(lista_id):
    with conectar() as conn:
        query = """
            SELECT
                p.nome AS Produto,
                ROUND(i.preco_estimado, 2) AS "Preço Estimado",
                ROUND(i.quantidade_compra, 2) AS "Qtd. Compra",
                ROUND(i.quantidade_compra * i.preco_estimado, 2) AS Subtotal
            FROM itens_lista i
            INNER JOIN produtos p ON i.produto_id = p.id
            WHERE i.lista_id = ?
            ORDER BY Subtotal DESC, Produto ASC
            LIMIT 5
        """
        return pd.read_sql_query(query, conn, params=(int(lista_id),))


# =========================================================
# FORMATAÇÃO
# =========================================================
def formatar_moeda(valor):
    return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_numero(valor):
    return f"{float(valor):.2f}".replace(".", ",")


# =========================================================
# INICIALIZAÇÃO
# =========================================================
inicializar_banco()
popular_dados_iniciais()

st.title(":shopping_cart: Questão 07 — Lista de Compras")
st.markdown(
    """
Aplicação desenvolvida em **Python + Streamlit + SQLite** para controle de uma
**lista de compras mensal**, permitindo cadastro de itens, edição, exclusão e
cálculo automático do **subtotal por item** e do **total da lista**.
"""
)

# =========================================================
# FILTRO DO MÊS/ANO
# =========================================================
meses = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12
}

hoje = date.today()

st.sidebar.header("Lista mensal")
mes_nome = st.sidebar.selectbox(
    "Selecione o mês",
    options=list(meses.keys()),
    index=hoje.month - 1
)
ano = st.sidebar.number_input(
    "Selecione o ano",
    min_value=2000,
    max_value=2100,
    value=hoje.year,
    step=1
)

mes = meses[mes_nome]
lista_id = obter_ou_criar_lista(mes, int(ano))

st.sidebar.markdown("---")
st.sidebar.write(f"**Lista ativa:** {mes_nome}/{int(ano)}")

aba1, aba2, aba3 = st.tabs(
    ["Cadastro", "Listagem e Gerenciamento", "Resumo Mensal"]
)

# Carregamento das opções atuais
produtos = listar_produtos()
unidades = listar_unidades()

mapa_produtos = {item["nome"]: item["id"] for item in produtos}
mapa_unidades = {
    f'{item["descricao"]} ({item["sigla"]})': item["id"]
    for item in unidades
}


# =========================================================
# ABA 1 - CADASTRO
# =========================================================
with aba1:
    st.subheader("Cadastrar item da lista")

    col_a, col_b = st.columns(2)

    with col_a:
        with st.expander("Adicionar novo produto"):
            with st.form("form_produto", clear_on_submit=True):
                novo_produto = st.text_input("Nome do produto")
                btn_produto = st.form_submit_button("Salvar produto")

                if btn_produto:
                    if not novo_produto.strip():
                        st.error("Informe o nome do produto.")
                    else:
                        try:
                            adicionar_produto(novo_produto)
                            st.success("Produto cadastrado com sucesso!")
                            st.rerun()
                        except sqlite3.IntegrityError:
                            st.warning("Esse produto já existe.")

    with col_b:
        with st.expander("Adicionar nova unidade de compra"):
            with st.form("form_unidade", clear_on_submit=True):
                descricao_unidade = st.text_input("Descrição da unidade")
                sigla_unidade = st.text_input("Sigla da unidade")
                btn_unidade = st.form_submit_button("Salvar unidade")

                if btn_unidade:
                    if not descricao_unidade.strip() or not sigla_unidade.strip():
                        st.error("Informe a descrição e a sigla da unidade.")
                    else:
                        try:
                            adicionar_unidade(descricao_unidade, sigla_unidade)
                            st.success("Unidade de compra cadastrada com sucesso!")
                            st.rerun()
                        except sqlite3.IntegrityError:
                            st.warning("Essa sigla de unidade já existe.")

    st.markdown("---")

    if not mapa_produtos or not mapa_unidades:
        st.info("Cadastre pelo menos um produto e uma unidade para começar.")
    else:
        with st.form("form_item_lista", clear_on_submit=True):
            col1, col2 = st.columns(2)

            with col1:
                produto_escolhido = st.selectbox(
                    "Produto",
                    options=list(mapa_produtos.keys())
                )
                unidade_escolhida = st.selectbox(
                    "Unidade de compra",
                    options=list(mapa_unidades.keys())
                )
                quantidade_mes = st.number_input(
                    "Quantidade prevista para o mês",
                    min_value=0.0,
                    step=0.5,
                    format="%.2f"
                )

            with col2:
                quantidade_compra = st.number_input(
                    "Quantidade que será comprada",
                    min_value=0.0,
                    step=0.5,
                    format="%.2f"
                )
                preco_estimado = st.number_input(
                    "Preço estimado por unidade (R$)",
                    min_value=0.0,
                    step=0.01,
                    format="%.2f"
                )

            enviar = st.form_submit_button("Cadastrar item")

            if enviar:
                if quantidade_mes <= 0:
                    st.error("Informe uma quantidade prevista maior que zero.")
                elif quantidade_compra <= 0:
                    st.error("Informe a quantidade de compra.")
                elif preco_estimado <= 0:
                    st.error("Informe o preço estimado.")
                else:
                    adicionar_item(
                        lista_id=lista_id,
                        produto_id=mapa_produtos[produto_escolhido],
                        unidade_id=mapa_unidades[unidade_escolhida],
                        quantidade_mes=quantidade_mes,
                        quantidade_compra=quantidade_compra,
                        preco_estimado=preco_estimado
                    )
                    st.success("Item cadastrado com sucesso!")
                    st.rerun()


# =========================================================
# ABA 2 - LISTAGEM E GERENCIAMENTO
# =========================================================
with aba2:
    st.subheader(f"Itens cadastrados em {mes_nome}/{int(ano)}")

    df_itens = listar_itens_da_lista(lista_id)

    if df_itens.empty:
        st.info("Nenhum item cadastrado para a lista selecionada.")
    else:
        df_exibicao = df_itens.copy()
        df_exibicao["quantidade_mes"] = df_exibicao["quantidade_mes"].map(formatar_numero)
        df_exibicao["quantidade_compra"] = df_exibicao["quantidade_compra"].map(formatar_numero)
        df_exibicao["preco_estimado"] = df_exibicao["preco_estimado"].map(formatar_moeda)
        df_exibicao["subtotal"] = df_exibicao["subtotal"].map(formatar_moeda)

        df_exibicao = df_exibicao.rename(columns={
            "id": "ID",
            "produto": "Produto",
            "unidade": "Unidade",
            "quantidade_mes": "Qtd. Mês",
            "quantidade_compra": "Qtd. Compra",
            "preco_estimado": "Preço Estimado",
            "subtotal": "Subtotal"
        })

        st.dataframe(
            df_exibicao[["ID", "Produto", "Unidade", "Qtd. Mês", "Qtd. Compra", "Preço Estimado", "Subtotal"]],
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("Editar ou excluir item")

        opcoes_itens = {
            f'ID {row["id"]} - {row["produto"]} - {formatar_moeda(row["subtotal"])}': int(row["id"])
            for _, row in df_itens.iterrows()
        }

        item_selecionado = st.selectbox(
            "Selecione um item",
            options=list(opcoes_itens.keys())
        )

        item_id = opcoes_itens[item_selecionado]
        item = obter_item_por_id(item_id)

        if item:
            lista_produtos = listar_produtos()
            lista_unidades = listar_unidades()

            nomes_produtos = [registro["nome"] for registro in lista_produtos]
            nomes_unidades = [
                f'{registro["descricao"]} ({registro["sigla"]})'
                for registro in lista_unidades
            ]

            indice_produto = next(
                (i for i, registro in enumerate(lista_produtos) if registro["id"] == item["produto_id"]),
                0
            )
            indice_unidade = next(
                (i for i, registro in enumerate(lista_unidades) if registro["id"] == item["unidade_id"]),
                0
            )

            with st.form("form_edicao_item"):
                col1, col2 = st.columns(2)

                with col1:
                    novo_produto = st.selectbox(
                        "Produto",
                        options=nomes_produtos,
                        index=indice_produto
                    )
                    nova_unidade = st.selectbox(
                        "Unidade de compra",
                        options=nomes_unidades,
                        index=indice_unidade
                    )
                    nova_quantidade_mes = st.number_input(
                        "Quantidade prevista para o mês",
                        min_value=0.0,
                        step=0.5,
                        format="%.2f",
                        value=float(item["quantidade_mes"])
                    )

                with col2:
                    nova_quantidade_compra = st.number_input(
                        "Quantidade que será comprada",
                        min_value=0.0,
                        step=0.5,
                        format="%.2f",
                        value=float(item["quantidade_compra"])
                    )
                    novo_preco_estimado = st.number_input(
                        "Preço estimado por unidade (R$)",
                        min_value=0.0,
                        step=0.01,
                        format="%.2f",
                        value=float(item["preco_estimado"])
                    )

                col_btn1, col_btn2 = st.columns(2)
                salvar = col_btn1.form_submit_button("Salvar alterações")
                remover = col_btn2.form_submit_button("Excluir item")

                if salvar:
                    if nova_quantidade_mes <= 0:
                        st.error("Informe uma quantidade prevista maior que zero.")
                    elif nova_quantidade_compra <= 0:
                        st.error("Informe a quantidade de compra.")
                    elif novo_preco_estimado <= 0:
                        st.error("Informe o preço estimado.")
                    else:
                        mapa_produtos_edicao = {
                            registro["nome"]: registro["id"] for registro in lista_produtos
                        }
                        mapa_unidades_edicao = {
                            f'{registro["descricao"]} ({registro["sigla"]})': registro["id"]
                            for registro in lista_unidades
                        }

                        atualizar_item(
                            item_id=item_id,
                            produto_id=mapa_produtos_edicao[novo_produto],
                            unidade_id=mapa_unidades_edicao[nova_unidade],
                            quantidade_mes=nova_quantidade_mes,
                            quantidade_compra=nova_quantidade_compra,
                            preco_estimado=novo_preco_estimado
                        )
                        st.success("Item atualizado com sucesso!")
                        st.rerun()

                if remover:
                    excluir_item(item_id)
                    st.success("Item excluído com sucesso!")
                    st.rerun()


# =========================================================
# ABA 3 - RESUMO MENSAL
# =========================================================
with aba3:
    st.subheader(f"Resumo da lista de compras - {mes_nome}/{int(ano)}")

    df_resumo = resumo_por_produto(lista_id)
    total = calcular_total_lista(lista_id)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total da lista", formatar_moeda(total))
    col2.metric("Quantidade de itens", len(df_resumo))
    col3.metric(
        "Média por item",
        formatar_moeda(total / len(df_resumo)) if len(df_resumo) > 0 else "R$ 0,00"
    )

    st.markdown("---")
    st.markdown("### Subtotal por produto")

    if df_resumo.empty:
        st.info("Não há itens cadastrados para gerar o resumo.")
    else:
        df_resumo_exibicao = df_resumo.copy()
        df_resumo_exibicao["Qtd. Mês"] = df_resumo_exibicao["Qtd. Mês"].map(formatar_numero)
        df_resumo_exibicao["Qtd. Compra"] = df_resumo_exibicao["Qtd. Compra"].map(formatar_numero)
        df_resumo_exibicao["Preço Estimado"] = df_resumo_exibicao["Preço Estimado"].map(formatar_moeda)
        df_resumo_exibicao["Subtotal"] = df_resumo_exibicao["Subtotal"].map(formatar_moeda)

        st.dataframe(df_resumo_exibicao, use_container_width=True)

        st.markdown("---")
        st.markdown("### Maiores subtotais da lista")

        df_top = produtos_maior_subtotal(lista_id)
        if not df_top.empty:
            df_top_exibicao = df_top.copy()
            df_top_exibicao["Preço Estimado"] = df_top_exibicao["Preço Estimado"].map(formatar_moeda)
            df_top_exibicao["Qtd. Compra"] = df_top_exibicao["Qtd. Compra"].map(formatar_numero)
            df_top_exibicao["Subtotal"] = df_top_exibicao["Subtotal"].map(formatar_moeda)

            st.dataframe(df_top_exibicao, use_container_width=True)