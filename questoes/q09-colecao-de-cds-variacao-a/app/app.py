import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Questão 09 - Coleção de CDs (Variação A)",
    page_icon=":cd:",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def formatar_duracao(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:02d}"


def duracao_para_segundos(minutos, segundos):
    return int(minutos) * 60 + int(segundos)


# =========================================================
# BANCO DE DADOS
# =========================================================
def conectar():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar_banco():
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano_lancamento INTEGER NOT NULL,
                coletanea INTEGER NOT NULL DEFAULT 0,
                duplo INTEGER NOT NULL DEFAULT 0
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS musicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS musicas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cd_musicos (
                cd_id INTEGER NOT NULL,
                musico_id INTEGER NOT NULL,
                PRIMARY KEY (cd_id, musico_id),
                FOREIGN KEY (cd_id) REFERENCES cds(id) ON DELETE CASCADE,
                FOREIGN KEY (musico_id) REFERENCES musicos(id) ON DELETE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faixas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cd_id INTEGER NOT NULL,
                musica_id INTEGER NOT NULL,
                numero INTEGER NOT NULL,
                duracao_segundos INTEGER NOT NULL,
                UNIQUE (cd_id, numero),
                FOREIGN KEY (cd_id) REFERENCES cds(id) ON DELETE CASCADE,
                FOREIGN KEY (musica_id) REFERENCES musicas(id) ON DELETE CASCADE
            )
        """)

        conn.commit()


def inserir_dados_iniciais():
    with conectar() as conn:
        cursor = conn.cursor()

        musicos_padrao = [
            "Legião Urbana",
            "Marisa Monte",
            "Titãs",
            "Cássia Eller",
            "Caetano Veloso"
        ]

        musicas_padrao = [
            "Tempo Perdido",
            "Ainda Lembro",
            "Epitáfio",
            "Malandragem",
            "Sozinho"
        ]

        for nome in musicos_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO musicos (nome) VALUES (?)",
                (nome,)
            )

        for titulo in musicas_padrao:
            cursor.execute(
                "INSERT OR IGNORE INTO musicas (titulo) VALUES (?)",
                (titulo,)
            )

        conn.commit()


# =========================================================
# CADASTROS BÁSICOS
# =========================================================
def listar_musicos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM musicos ORDER BY nome")
        return cursor.fetchall()


def listar_musicas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo FROM musicas ORDER BY titulo")
        return cursor.fetchall()


def cadastrar_musico(nome):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO musicos (nome) VALUES (?)",
            (nome.strip(),)
        )
        conn.commit()


def cadastrar_musica(titulo):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO musicas (titulo) VALUES (?)",
            (titulo.strip(),)
        )
        conn.commit()


# =========================================================
# CDS E FAIXAS
# =========================================================
def cadastrar_cd(titulo, ano_lancamento, coletanea, duplo, musicos_ids):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cds (titulo, ano_lancamento, coletanea, duplo)
            VALUES (?, ?, ?, ?)
        """, (titulo.strip(), int(ano_lancamento), int(coletanea), int(duplo)))

        cd_id = cursor.lastrowid

        for musico_id in musicos_ids:
            cursor.execute(
                "INSERT INTO cd_musicos (cd_id, musico_id) VALUES (?, ?)",
                (cd_id, int(musico_id))
            )

        conn.commit()


def listar_cds():
    with conectar() as conn:
        query = """
            SELECT
                c.id,
                c.titulo,
                c.ano_lancamento,
                c.coletanea,
                c.duplo,
                COALESCE(GROUP_CONCAT(DISTINCT m.nome), '') AS musicos,
                COUNT(DISTINCT f.id) AS qtd_faixas
            FROM cds c
            LEFT JOIN cd_musicos cm ON c.id = cm.cd_id
            LEFT JOIN musicos m ON cm.musico_id = m.id
            LEFT JOIN faixas f ON c.id = f.cd_id
            GROUP BY c.id, c.titulo, c.ano_lancamento, c.coletanea, c.duplo
            ORDER BY c.titulo ASC
        """
        return pd.read_sql_query(query, conn)


def obter_cd_por_id(cd_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, titulo, ano_lancamento, coletanea, duplo
            FROM cds
            WHERE id = ?
        """, (int(cd_id),))
        return cursor.fetchone()


def listar_musicos_do_cd(cd_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.id, m.nome
            FROM musicos m
            INNER JOIN cd_musicos cm ON m.id = cm.musico_id
            WHERE cm.cd_id = ?
            ORDER BY m.nome
        """, (int(cd_id),))
        return cursor.fetchall()


def atualizar_cd(cd_id, titulo, ano_lancamento, coletanea, duplo, musicos_ids):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE cds
            SET titulo = ?, ano_lancamento = ?, coletanea = ?, duplo = ?
            WHERE id = ?
        """, (titulo.strip(), int(ano_lancamento), int(coletanea), int(duplo), int(cd_id)))

        cursor.execute("DELETE FROM cd_musicos WHERE cd_id = ?", (int(cd_id),))

        for musico_id in musicos_ids:
            cursor.execute(
                "INSERT INTO cd_musicos (cd_id, musico_id) VALUES (?, ?)",
                (int(cd_id), int(musico_id))
            )

        conn.commit()


def excluir_cd(cd_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cds WHERE id = ?", (int(cd_id),))
        conn.commit()


def cadastrar_faixa(cd_id, numero, musica_id, duracao_segundos):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO faixas (cd_id, numero, musica_id, duracao_segundos)
            VALUES (?, ?, ?, ?)
        """, (int(cd_id), int(numero), int(musica_id), int(duracao_segundos)))
        conn.commit()


def listar_faixas_do_cd(cd_id):
    with conectar() as conn:
        query = """
            SELECT
                f.id,
                f.numero,
                mu.titulo AS musica,
                f.duracao_segundos
            FROM faixas f
            INNER JOIN musicas mu ON f.musica_id = mu.id
            WHERE f.cd_id = ?
            ORDER BY f.numero ASC
        """
        return pd.read_sql_query(query, conn, params=(int(cd_id),))


def obter_faixa_por_id(faixa_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, cd_id, numero, musica_id, duracao_segundos
            FROM faixas
            WHERE id = ?
        """, (int(faixa_id),))
        return cursor.fetchone()


def atualizar_faixa(faixa_id, numero, musica_id, duracao_segundos):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE faixas
            SET numero = ?, musica_id = ?, duracao_segundos = ?
            WHERE id = ?
        """, (int(numero), int(musica_id), int(duracao_segundos), int(faixa_id)))
        conn.commit()


def excluir_faixa(faixa_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM faixas WHERE id = ?", (int(faixa_id),))
        conn.commit()


# =========================================================
# CONSULTAS
# =========================================================
def buscar_cds_por_musico(musico_id):
    with conectar() as conn:
        query = """
            SELECT
                c.titulo AS CD,
                c.ano_lancamento AS Ano,
                CASE WHEN c.coletanea = 1 THEN 'Sim' ELSE 'Não' END AS Coletânea,
                CASE WHEN c.duplo = 1 THEN 'Sim' ELSE 'Não' END AS Duplo
            FROM cds c
            INNER JOIN cd_musicos cm ON c.id = cm.cd_id
            WHERE cm.musico_id = ?
            ORDER BY c.titulo
        """
        return pd.read_sql_query(query, conn, params=(int(musico_id),))


def buscar_cds_por_musica(musica_id):
    with conectar() as conn:
        query = """
            SELECT DISTINCT
                c.titulo AS CD,
                c.ano_lancamento AS Ano,
                f.numero AS Faixa,
                printf('%02d:%02d', f.duracao_segundos / 60, f.duracao_segundos % 60) AS Duração
            FROM cds c
            INNER JOIN faixas f ON c.id = f.cd_id
            WHERE f.musica_id = ?
            ORDER BY c.titulo, f.numero
        """
        return pd.read_sql_query(query, conn, params=(int(musica_id),))


def listar_coletaneas():
    with conectar() as conn:
        query = """
            SELECT
                titulo AS CD,
                ano_lancamento AS Ano
            FROM cds
            WHERE coletanea = 1
            ORDER BY titulo
        """
        return pd.read_sql_query(query, conn)


def listar_cds_duplos():
    with conectar() as conn:
        query = """
            SELECT
                titulo AS CD,
                ano_lancamento AS Ano
            FROM cds
            WHERE duplo = 1
            ORDER BY titulo
        """
        return pd.read_sql_query(query, conn)


# =========================================================
# INICIALIZAÇÃO
# =========================================================
inicializar_banco()
inserir_dados_iniciais()

st.title(":cd: Questão 09 — Coleção de CDs (Variação A)")
st.markdown(
    """
Aplicação desenvolvida em **Python + Streamlit + SQLite** para gerenciar uma coleção de CDs,
incluindo **coletâneas**, **CDs duplos**, **músicos**, **músicas** e **faixas com duração**.
"""
)

aba1, aba2, aba3, aba4 = st.tabs(
    ["Cadastros Básicos", "CDs e Faixas", "Listagem e Gerenciamento", "Consultas"]
)

# =========================================================
# ABA 1 - CADASTROS BÁSICOS
# =========================================================
with aba1:
    st.subheader("Cadastrar músicos e músicas")

    col1, col2 = st.columns(2)

    with col1:
        with st.form("form_musico", clear_on_submit=True):
            st.markdown("### Novo músico")
            nome_musico = st.text_input("Nome do músico ou conjunto")
            salvar_musico = st.form_submit_button("Cadastrar músico")

            if salvar_musico:
                if not nome_musico.strip():
                    st.error("Informe o nome do músico.")
                else:
                    try:
                        cadastrar_musico(nome_musico)
                        st.success("Músico cadastrado com sucesso!")
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.warning("Esse músico já está cadastrado.")

    with col2:
        with st.form("form_musica", clear_on_submit=True):
            st.markdown("### Nova música")
            titulo_musica = st.text_input("Título da música")
            salvar_musica = st.form_submit_button("Cadastrar música")

            if salvar_musica:
                if not titulo_musica.strip():
                    st.error("Informe o título da música.")
                else:
                    try:
                        cadastrar_musica(titulo_musica)
                        st.success("Música cadastrada com sucesso!")
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.warning("Essa música já está cadastrada.")

    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Músicos cadastrados")
        dados_musicos = listar_musicos()
        if dados_musicos:
            st.dataframe(
                pd.DataFrame([{"ID": item["id"], "Nome": item["nome"]} for item in dados_musicos]),
                use_container_width=True
            )
        else:
            st.info("Nenhum músico cadastrado.")

    with col4:
        st.markdown("### Músicas cadastradas")
        dados_musicas = listar_musicas()
        if dados_musicas:
            st.dataframe(
                pd.DataFrame([{"ID": item["id"], "Título": item["titulo"]} for item in dados_musicas]),
                use_container_width=True
            )
        else:
            st.info("Nenhuma música cadastrada.")


# =========================================================
# ABA 2 - CDS E FAIXAS
# =========================================================
with aba2:
    st.subheader("Cadastrar CD")

    musicos = listar_musicos()
    musicas = listar_musicas()

    mapa_musicos = {item["nome"]: item["id"] for item in musicos}
    mapa_musicas = {item["titulo"]: item["id"] for item in musicas}

    with st.form("form_cd", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            titulo_cd = st.text_input("Título do CD")
            ano_lancamento = st.number_input(
                "Ano de lançamento",
                min_value=1900,
                max_value=2100,
                value=2000,
                step=1
            )

        with col2:
            coletanea = st.checkbox("É coletânea?")
            duplo = st.checkbox("É CD duplo?")
            musicos_selecionados = st.multiselect(
                "Músicos do CD",
                options=list(mapa_musicos.keys())
            )

        salvar_cd = st.form_submit_button("Cadastrar CD")

        if salvar_cd:
            if not titulo_cd.strip():
                st.error("Informe o título do CD.")
            elif not musicos_selecionados:
                st.error("Selecione pelo menos um músico para o CD.")
            else:
                cadastrar_cd(
                    titulo=titulo_cd,
                    ano_lancamento=int(ano_lancamento),
                    coletanea=coletanea,
                    duplo=duplo,
                    musicos_ids=[mapa_musicos[nome] for nome in musicos_selecionados]
                )
                st.success("CD cadastrado com sucesso!")
                st.rerun()

    st.markdown("---")
    st.subheader("Cadastrar faixa")

    df_cds = listar_cds()

    if df_cds.empty:
        st.info("Cadastre pelo menos um CD antes de adicionar faixas.")
    elif not mapa_musicas:
        st.info("Cadastre pelo menos uma música antes de adicionar faixas.")
    else:
        opcoes_cds = {f'ID {row["id"]} - {row["titulo"]}': int(row["id"]) for _, row in df_cds.iterrows()}

        with st.form("form_faixa", clear_on_submit=True):
            col1, col2 = st.columns(2)

            with col1:
                cd_escolhido = st.selectbox("CD", options=list(opcoes_cds.keys()))
                numero_faixa = st.number_input("Número da faixa", min_value=1, step=1, value=1)

            with col2:
                musica_escolhida = st.selectbox("Música", options=list(mapa_musicas.keys()))
                col_min, col_seg = st.columns(2)
                with col_min:
                    minutos = st.number_input("Minutos", min_value=0, max_value=59, value=3, step=1)
                with col_seg:
                    segundos = st.number_input("Segundos", min_value=0, max_value=59, value=0, step=1)

            salvar_faixa = st.form_submit_button("Cadastrar faixa")

            if salvar_faixa:
                duracao = duracao_para_segundos(minutos, segundos)
                if duracao <= 0:
                    st.error("Informe uma duração válida.")
                else:
                    try:
                        cadastrar_faixa(
                            cd_id=opcoes_cds[cd_escolhido],
                            numero=int(numero_faixa),
                            musica_id=mapa_musicas[musica_escolhida],
                            duracao_segundos=duracao
                        )
                        st.success("Faixa cadastrada com sucesso!")
                        st.rerun()
                    except sqlite3.IntegrityError:
                        st.warning("Já existe uma faixa com esse número para o CD selecionado.")


# =========================================================
# ABA 3 - LISTAGEM E GERENCIAMENTO
# =========================================================
with aba3:
    st.subheader("CDs cadastrados")

    df_cds = listar_cds()

    if df_cds.empty:
        st.info("Nenhum CD cadastrado até o momento.")
    else:
        df_exibicao = df_cds.copy()
        df_exibicao["coletanea"] = df_exibicao["coletanea"].map(lambda x: "Sim" if int(x) == 1 else "Não")
        df_exibicao["duplo"] = df_exibicao["duplo"].map(lambda x: "Sim" if int(x) == 1 else "Não")
        df_exibicao = df_exibicao.rename(columns={
            "id": "ID",
            "titulo": "Título",
            "ano_lancamento": "Ano",
            "coletanea": "Coletânea",
            "duplo": "Duplo",
            "musicos": "Músicos",
            "qtd_faixas": "Qtd. Faixas"
        })
        st.dataframe(df_exibicao, use_container_width=True)

        st.markdown("---")
        st.subheader("Editar ou excluir CD")

        opcoes_cd = {f'ID {row["id"]} - {row["titulo"]}': int(row["id"]) for _, row in df_cds.iterrows()}
        cd_escolhido = st.selectbox("Selecione um CD", options=list(opcoes_cd.keys()))
        cd_id = opcoes_cd[cd_escolhido]
        cd = obter_cd_por_id(cd_id)
        musicos_cd = listar_musicos_do_cd(cd_id)
        musicos = listar_musicos()
        mapa_musicos = {item["nome"]: item["id"] for item in musicos}
        nomes_musicos = list(mapa_musicos.keys())
        ids_musicos_cd = [item["id"] for item in musicos_cd]

        if cd:
            with st.form("form_editar_cd"):
                col1, col2 = st.columns(2)

                with col1:
                    novo_titulo = st.text_input("Título do CD", value=cd["titulo"])
                    novo_ano = st.number_input(
                        "Ano de lançamento",
                        min_value=1900,
                        max_value=2100,
                        value=int(cd["ano_lancamento"]),
                        step=1
                    )

                with col2:
                    nova_coletanea = st.checkbox("É coletânea?", value=bool(cd["coletanea"]))
                    novo_duplo = st.checkbox("É CD duplo?", value=bool(cd["duplo"]))
                    novos_musicos = st.multiselect(
                        "Músicos do CD",
                        options=nomes_musicos,
                        default=[nome for nome in nomes_musicos if mapa_musicos[nome] in ids_musicos_cd]
                    )

                col_btn1, col_btn2 = st.columns(2)
                salvar_cd = col_btn1.form_submit_button("Salvar alterações")
                remover_cd = col_btn2.form_submit_button("Excluir CD")

                if salvar_cd:
                    if not novo_titulo.strip():
                        st.error("Informe o título do CD.")
                    elif not novos_musicos:
                        st.error("Selecione pelo menos um músico para o CD.")
                    else:
                        atualizar_cd(
                            cd_id=cd_id,
                            titulo=novo_titulo,
                            ano_lancamento=int(novo_ano),
                            coletanea=nova_coletanea,
                            duplo=novo_duplo,
                            musicos_ids=[mapa_musicos[nome] for nome in novos_musicos]
                        )
                        st.success("CD atualizado com sucesso!")
                        st.rerun()

                if remover_cd:
                    excluir_cd(cd_id)
                    st.success("CD excluído com sucesso!")
                    st.rerun()

        st.markdown("---")
        st.subheader("Faixas do CD selecionado")

        df_faixas = listar_faixas_do_cd(cd_id)

        if df_faixas.empty:
            st.info("Esse CD ainda não possui faixas cadastradas.")
        else:
            df_faixas_exibicao = df_faixas.copy()
            df_faixas_exibicao["duracao_segundos"] = df_faixas_exibicao["duracao_segundos"].map(formatar_duracao)
            df_faixas_exibicao = df_faixas_exibicao.rename(columns={
                "id": "ID",
                "numero": "Faixa",
                "musica": "Música",
                "duracao_segundos": "Duração"
            })
            st.dataframe(df_faixas_exibicao, use_container_width=True)

            st.markdown("### Editar ou excluir faixa")
            opcoes_faixa = {
                f'ID {row["id"]} - Faixa {row["numero"]} - {row["musica"]}': int(row["id"])
                for _, row in df_faixas.iterrows()
            }
            faixa_escolhida = st.selectbox("Selecione uma faixa", options=list(opcoes_faixa.keys()))
            faixa_id = opcoes_faixa[faixa_escolhida]
            faixa = obter_faixa_por_id(faixa_id)

            musicas = listar_musicas()
            mapa_musicas = {item["titulo"]: item["id"] for item in musicas}
            nomes_musicas = list(mapa_musicas.keys())
            indice_musica = next(
                (i for i, nome in enumerate(nomes_musicas) if mapa_musicas[nome] == faixa["musica_id"]),
                0
            )

            minutos_padrao = int(faixa["duracao_segundos"]) // 60
            segundos_padrao = int(faixa["duracao_segundos"]) % 60

            with st.form("form_editar_faixa"):
                col1, col2 = st.columns(2)

                with col1:
                    novo_numero = st.number_input(
                        "Número da faixa",
                        min_value=1,
                        step=1,
                        value=int(faixa["numero"])
                    )
                    nova_musica = st.selectbox(
                        "Música",
                        options=nomes_musicas,
                        index=indice_musica
                    )

                with col2:
                    novo_min = st.number_input("Minutos", min_value=0, max_value=59, value=minutos_padrao, step=1)
                    novo_seg = st.number_input("Segundos", min_value=0, max_value=59, value=segundos_padrao, step=1)

                col_btn1, col_btn2 = st.columns(2)
                salvar_faixa = col_btn1.form_submit_button("Salvar faixa")
                remover_faixa = col_btn2.form_submit_button("Excluir faixa")

                if salvar_faixa:
                    nova_duracao = duracao_para_segundos(novo_min, novo_seg)
                    if nova_duracao <= 0:
                        st.error("Informe uma duração válida.")
                    else:
                        try:
                            atualizar_faixa(
                                faixa_id=faixa_id,
                                numero=int(novo_numero),
                                musica_id=mapa_musicas[nova_musica],
                                duracao_segundos=nova_duracao
                            )
                            st.success("Faixa atualizada com sucesso!")
                            st.rerun()
                        except sqlite3.IntegrityError:
                            st.warning("Já existe outra faixa com esse número neste CD.")

                if remover_faixa:
                    excluir_faixa(faixa_id)
                    st.success("Faixa excluída com sucesso!")
                    st.rerun()


# =========================================================
# ABA 4 - CONSULTAS
# =========================================================
with aba4:
    st.subheader("Consultas da coleção")

    musicos = listar_musicos()
    musicas = listar_musicas()

    mapa_musicos = {item["nome"]: item["id"] for item in musicos}
    mapa_musicas = {item["titulo"]: item["id"] for item in musicas}

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### CDs de um determinado músico")
        if mapa_musicos:
            musico_escolhido = st.selectbox("Selecione o músico", options=list(mapa_musicos.keys()))
            df_por_musico = buscar_cds_por_musico(mapa_musicos[musico_escolhido])

            if df_por_musico.empty:
                st.info("Nenhum CD encontrado para esse músico.")
            else:
                st.dataframe(df_por_musico, use_container_width=True)
        else:
            st.info("Nenhum músico cadastrado.")

    with col2:
        st.markdown("### Em quais CDs está uma determinada música")
        if mapa_musicas:
            musica_escolhida = st.selectbox("Selecione a música", options=list(mapa_musicas.keys()))
            df_por_musica = buscar_cds_por_musica(mapa_musicas[musica_escolhida])

            if df_por_musica.empty:
                st.info("Essa música não está associada a nenhum CD.")
            else:
                st.dataframe(df_por_musica, use_container_width=True)
        else:
            st.info("Nenhuma música cadastrada.")

    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### CDs marcados como coletânea")
        df_coletaneas = listar_coletaneas()
        if df_coletaneas.empty:
            st.info("Nenhum CD marcado como coletânea.")
        else:
            st.dataframe(df_coletaneas, use_container_width=True)

    with col4:
        st.markdown("### CDs marcados como duplos")
        df_duplos = listar_cds_duplos()
        if df_duplos.empty:
            st.info("Nenhum CD marcado como duplo.")
        else:
            st.dataframe(df_duplos, use_container_width=True)