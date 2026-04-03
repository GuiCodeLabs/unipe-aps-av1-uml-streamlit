import sqlite3
from pathlib import Path
from datetime import date, datetime

import pandas as pd
import streamlit as st


# =========================================================
# CONFIGURAÇÃO INICIAL
# =========================================================
st.set_page_config(
    page_title="Questão 05 - Gastos Diários",
    page_icon=":money_with_wings:",
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
            CREATE TABLE IF NOT EXISTS tipos_gasto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS formas_pagamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_gasto TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo_id INTEGER NOT NULL,
                forma_pagamento_id INTEGER NOT NULL,
                FOREIGN KEY (tipo_id) REFERENCES tipos_gasto(id),
                FOREIGN KEY (forma_pagamento_id) REFERENCES formas_pagamento(id)
            )
        """)

        conn.commit()


def popular_dados_iniciais():
    tipos_padrao = [
        "Remédio",
        "Roupa",
        "Refeição",
        "Transporte",
        "Lazer",
        "Mercado"
    ]

    formas_padrao = [
        "Dinheiro",
        "Cartão de Crédito",
        "Cartão de Débito",
        "Ticket Alimentação",
        "Vale Refeição",
        "PIX"
    ]

    with conectar() as conn:
        cursor = conn.cursor()

        for tipo in tipos_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO tipos_gasto (descricao) VALUES (?)",
                (tipo,)
            )

        for forma in formas_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO formas_pagamento (descricao) VALUES (?)",
                (forma,)
            )

        conn.commit()


# =========================================================
# FUNÇÕES DE CONSULTA
# =========================================================
def listar_tipos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao FROM tipos_gasto ORDER BY descricao")
        return cursor.fetchall()


def listar_formas_pagamento():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao FROM formas_pagamento ORDER BY descricao")
        return cursor.fetchall()


def adicionar_tipo(descricao):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tipos_gasto (descricao) VALUES (?)",
            (descricao.strip(),)
        )
        conn.commit()


def adicionar_forma_pagamento(descricao):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO formas_pagamento (descricao) VALUES (?)",
            (descricao.strip(),)
        )
        conn.commit()


def cadastrar_gasto(data_gasto, valor, tipo_id, forma_pagamento_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO gastos (data_gasto, valor, tipo_id, forma_pagamento_id)
            VALUES (?, ?, ?, ?)
        """, (data_gasto.isoformat(), float(valor), int(tipo_id), int(forma_pagamento_id)))
        conn.commit()


def listar_gastos():
    with conectar() as conn:
        query = """
            SELECT
                g.id,
                g.data_gasto,
                g.valor,
                t.descricao AS tipo,
                f.descricao AS forma_pagamento,
                g.tipo_id,
                g.forma_pagamento_id
            FROM gastos g
            INNER JOIN tipos_gasto t ON g.tipo_id = t.id
            INNER JOIN formas_pagamento f ON g.forma_pagamento_id = f.id
            ORDER BY g.data_gasto DESC, g.id DESC
        """
        df = pd.read_sql_query(query, conn)
        return df


def obter_gasto_por_id(gasto_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                id,
                data_gasto,
                valor,
                tipo_id,
                forma_pagamento_id
            FROM gastos
            WHERE id = ?
        """, (gasto_id,))
        return cursor.fetchone()


def atualizar_gasto(gasto_id, data_gasto, valor, tipo_id, forma_pagamento_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE gastos
            SET data_gasto = ?, valor = ?, tipo_id = ?, forma_pagamento_id = ?
            WHERE id = ?
        """, (
            data_gasto.isoformat(),
            float(valor),
            int(tipo_id),
            int(forma_pagamento_id),
            int(gasto_id)
        ))
        conn.commit()


def excluir_gasto(gasto_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM gastos WHERE id = ?", (int(gasto_id),))
        conn.commit()


def obter_periodo_relatorio(mes, ano):
    data_inicio = date(ano, mes, 1)
    if mes == 12:
        data_fim = date(ano + 1, 1, 1)
    else:
        data_fim = date(ano, mes + 1, 1)
    return data_inicio.isoformat(), data_fim.isoformat()


def listar_gastos_do_mes(mes, ano):
    data_inicio, data_fim = obter_periodo_relatorio(mes, ano)

    with conectar() as conn:
        query = """
            SELECT
                g.id AS ID,
                strftime('%d/%m/%Y', g.data_gasto) AS Data,
                t.descricao AS Tipo,
                f.descricao AS "Forma de Pagamento",
                ROUND(g.valor, 2) AS Valor
            FROM gastos g
            INNER JOIN tipos_gasto t ON g.tipo_id = t.id
            INNER JOIN formas_pagamento f ON g.forma_pagamento_id = f.id
            WHERE g.data_gasto >= ? AND g.data_gasto < ?
            ORDER BY g.data_gasto ASC, g.id ASC
        """
        df = pd.read_sql_query(query, conn, params=(data_inicio, data_fim))
        return df


def total_mensal(mes, ano):
    data_inicio, data_fim = obter_periodo_relatorio(mes, ano)

    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COALESCE(SUM(valor), 0)
            FROM gastos
            WHERE data_gasto >= ? AND data_gasto < ?
        """, (data_inicio, data_fim))
        return float(cursor.fetchone()[0] or 0)


def agrupar_por_tipo(mes, ano):
    data_inicio, data_fim = obter_periodo_relatorio(mes, ano)

    with conectar() as conn:
        query = """
            SELECT
                t.descricao AS Tipo,
                ROUND(SUM(g.valor), 2) AS Total
            FROM gastos g
            INNER JOIN tipos_gasto t ON g.tipo_id = t.id
            WHERE g.data_gasto >= ? AND g.data_gasto < ?
            GROUP BY t.descricao
            ORDER BY Total DESC, Tipo ASC
        """
        return pd.read_sql_query(query, conn, params=(data_inicio, data_fim))


def agrupar_por_forma_pagamento(mes, ano):
    data_inicio, data_fim = obter_periodo_relatorio(mes, ano)

    with conectar() as conn:
        query = """
            SELECT
                f.descricao AS "Forma de Pagamento",
                ROUND(SUM(g.valor), 2) AS Total
            FROM gastos g
            INNER JOIN formas_pagamento f ON g.forma_pagamento_id = f.id
            WHERE g.data_gasto >= ? AND g.data_gasto < ?
            GROUP BY f.descricao
            ORDER BY Total DESC, f.descricao ASC
        """
        return pd.read_sql_query(query, conn, params=(data_inicio, data_fim))


# =========================================================
# INICIALIZAÇÃO
# =========================================================
inicializar_banco()
popular_dados_iniciais()

st.title(":money_with_wings: Questão 05 — Gastos Diários")
st.markdown(
    """
Aplicação desenvolvida em **Python + Streamlit + SQLite** para controle de gastos diários,
permitindo cadastro, listagem, edição, exclusão e geração de **relatórios mensais**
agrupados por **tipo de gasto** e **forma de pagamento**.
"""
)

aba1, aba2, aba3 = st.tabs(
    ["Cadastro", "Listagem e Gerenciamento", "Relatório Mensal"]
)

tipos = listar_tipos()
formas = listar_formas_pagamento()

mapa_tipos = {item["descricao"]: item["id"] for item in tipos}
mapa_formas = {item["descricao"]: item["id"] for item in formas}


# =========================================================
# ABA 1 - CADASTRO
# =========================================================
with aba1:
    st.subheader("Cadastrar novo gasto")

    col_a, col_b = st.columns(2)

    with col_a:
        with st.expander("Adicionar novo tipo de gasto"):
            with st.form("form_tipo_gasto", clear_on_submit=True):
                novo_tipo = st.text_input("Descrição do tipo")
                btn_tipo = st.form_submit_button("Salvar tipo")

                if btn_tipo:
                    if not novo_tipo.strip():
                        st.error("Informe a descrição do tipo.")
                    else:
                        try:
                            adicionar_tipo(novo_tipo)
                            st.success("Tipo de gasto cadastrado com sucesso!")
                            st.rerun()
                        except sqlite3.IntegrityError:
                            st.warning("Esse tipo de gasto já existe.")

    with col_b:
        with st.expander("Adicionar nova forma de pagamento"):
            with st.form("form_forma_pagamento", clear_on_submit=True):
                nova_forma = st.text_input("Descrição da forma de pagamento")
                btn_forma = st.form_submit_button("Salvar forma")

                if btn_forma:
                    if not nova_forma.strip():
                        st.error("Informe a descrição da forma de pagamento.")
                    else:
                        try:
                            adicionar_forma_pagamento(nova_forma)
                            st.success("Forma de pagamento cadastrada com sucesso!")
                            st.rerun()
                        except sqlite3.IntegrityError:
                            st.warning("Essa forma de pagamento já existe.")

    st.markdown("---")

    with st.form("form_cadastro_gasto", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            data_gasto = st.date_input("Data do gasto", value=date.today())
            tipo_escolhido = st.selectbox("Tipo do gasto", options=list(mapa_tipos.keys()))

        with col2:
            valor = st.number_input(
                "Valor do gasto (R$)",
                min_value=0.0,
                step=0.01,
                format="%.2f"
            )
            forma_escolhida = st.selectbox(
                "Forma de pagamento",
                options=list(mapa_formas.keys())
            )

        enviar = st.form_submit_button("Cadastrar gasto")

        if enviar:
            if valor <= 0:
                st.error("Informe um valor maior que zero.")
            else:
                cadastrar_gasto(
                    data_gasto=data_gasto,
                    valor=valor,
                    tipo_id=mapa_tipos[tipo_escolhido],
                    forma_pagamento_id=mapa_formas[forma_escolhida]
                )
                st.success("Gasto cadastrado com sucesso!")


# =========================================================
# ABA 2 - LISTAGEM E GERENCIAMENTO
# =========================================================
with aba2:
    st.subheader("Gastos cadastrados")

    df_gastos = listar_gastos()

    if df_gastos.empty:
        st.info("Nenhum gasto cadastrado até o momento.")
    else:
        df_exibicao = df_gastos.copy()
        df_exibicao["data_gasto"] = pd.to_datetime(df_exibicao["data_gasto"]).dt.strftime("%d/%m/%Y")
        df_exibicao["valor"] = df_exibicao["valor"].map(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        df_exibicao = df_exibicao.rename(columns={
            "id": "ID",
            "data_gasto": "Data",
            "valor": "Valor",
            "tipo": "Tipo",
            "forma_pagamento": "Forma de Pagamento"
        })

        st.dataframe(
            df_exibicao[["ID", "Data", "Tipo", "Forma de Pagamento", "Valor"]],
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("Editar ou excluir gasto")

        opcoes_gastos = {
            f'ID {row["id"]} - {row["tipo"]} - R$ {row["valor"]:.2f}': int(row["id"])
            for _, row in df_gastos.iterrows()
        }

        gasto_selecionado = st.selectbox(
            "Selecione um gasto",
            options=list(opcoes_gastos.keys())
        )

        gasto_id = opcoes_gastos[gasto_selecionado]
        gasto = obter_gasto_por_id(gasto_id)

        if gasto:
            tipo_id_atual = gasto["tipo_id"]
            forma_id_atual = gasto["forma_pagamento_id"]

            lista_tipos = listar_tipos()
            lista_formas = listar_formas_pagamento()

            nomes_tipos = [item["descricao"] for item in lista_tipos]
            nomes_formas = [item["descricao"] for item in lista_formas]

            indice_tipo = next(
                (i for i, item in enumerate(lista_tipos) if item["id"] == tipo_id_atual),
                0
            )
            indice_forma = next(
                (i for i, item in enumerate(lista_formas) if item["id"] == forma_id_atual),
                0
            )

            with st.form("form_edicao_gasto"):
                col1, col2 = st.columns(2)

                with col1:
                    nova_data = st.date_input(
                        "Data do gasto",
                        value=datetime.strptime(gasto["data_gasto"], "%Y-%m-%d").date()
                    )
                    novo_tipo = st.selectbox(
                        "Tipo do gasto",
                        options=nomes_tipos,
                        index=indice_tipo
                    )

                with col2:
                    novo_valor = st.number_input(
                        "Valor do gasto (R$)",
                        min_value=0.0,
                        step=0.01,
                        format="%.2f",
                        value=float(gasto["valor"])
                    )
                    nova_forma = st.selectbox(
                        "Forma de pagamento",
                        options=nomes_formas,
                        index=indice_forma
                    )

                col_btn1, col_btn2 = st.columns(2)
                salvar = col_btn1.form_submit_button("Salvar alterações")
                remover = col_btn2.form_submit_button("Excluir gasto")

                if salvar:
                    if novo_valor <= 0:
                        st.error("Informe um valor maior que zero.")
                    else:
                        atualizar_gasto(
                            gasto_id=gasto_id,
                            data_gasto=nova_data,
                            valor=novo_valor,
                            tipo_id={item["descricao"]: item["id"] for item in lista_tipos}[novo_tipo],
                            forma_pagamento_id={item["descricao"]: item["id"] for item in lista_formas}[nova_forma]
                        )
                        st.success("Gasto atualizado com sucesso!")
                        st.rerun()

                if remover:
                    excluir_gasto(gasto_id)
                    st.success("Gasto excluído com sucesso!")
                    st.rerun()


# =========================================================
# ABA 3 - RELATÓRIO MENSAL
# =========================================================
with aba3:
    st.subheader("Relatório mensal")

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

    col1, col2 = st.columns(2)
    with col1:
        mes_nome = st.selectbox("Selecione o mês", options=list(meses.keys()), index=hoje.month - 1)
    with col2:
        ano = st.number_input("Selecione o ano", min_value=2000, max_value=2100, value=hoje.year, step=1)

    mes = meses[mes_nome]

    df_mes = listar_gastos_do_mes(mes, int(ano))
    total = total_mensal(mes, int(ano))
    df_tipo = agrupar_por_tipo(mes, int(ano))
    df_forma = agrupar_por_forma_pagamento(mes, int(ano))

    st.markdown("### Resumo do mês")
    col3, col4 = st.columns(2)
    col3.metric("Total de gastos no mês", f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    col4.metric("Quantidade de lançamentos", len(df_mes))

    st.markdown("---")
    st.markdown("### Gastos do mês")

    if df_mes.empty:
        st.info("Não há gastos cadastrados para o período selecionado.")
    else:
        df_mes_exibicao = df_mes.copy()
        df_mes_exibicao["Valor"] = df_mes_exibicao["Valor"].map(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )
        st.dataframe(df_mes_exibicao, use_container_width=True)

    st.markdown("---")
    col5, col6 = st.columns(2)

    with col5:
        st.markdown("### Total por tipo de gasto")
        if df_tipo.empty:
            st.info("Sem dados para agrupar por tipo.")
        else:
            df_tipo_exibicao = df_tipo.copy()
            df_tipo_exibicao["Total"] = df_tipo_exibicao["Total"].map(
                lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            )
            st.dataframe(df_tipo_exibicao, use_container_width=True)

    with col6:
        st.markdown("### Total por forma de pagamento")
        if df_forma.empty:
            st.info("Sem dados para agrupar por forma de pagamento.")
        else:
            df_forma_exibicao = df_forma.copy()
            df_forma_exibicao["Total"] = df_forma_exibicao["Total"].map(
                lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            )
            st.dataframe(df_forma_exibicao, use_container_width=True)