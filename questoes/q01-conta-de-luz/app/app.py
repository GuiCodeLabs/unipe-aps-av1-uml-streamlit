import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Questão 01 - Conta de Luz",
    page_icon=":bulb:",
    layout="wide"
)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def inicializar_estado():
    if "contas_luz" not in st.session_state:
        st.session_state.contas_luz = []


def gerar_id():
    if not st.session_state.contas_luz:
        return 1
    return max(conta["id"] for conta in st.session_state.contas_luz) + 1


def obter_mes_referencia(data_leitura):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return f"{meses[data_leitura.month - 1]}/{data_leitura.year}"


def calcular_media_consumo(kw_gasto):
    # Considerando média diária aproximada em 30 dias
    return round(kw_gasto / 30, 2)


def adicionar_conta(data_leitura, numero_leitura, kw_gasto, valor_pagar, data_pagamento):
    conta = {
        "id": gerar_id(),
        "mesReferencia": obter_mes_referencia(data_leitura),
        "dataLeitura": data_leitura,
        "numeroLeitura": numero_leitura,
        "kwGasto": float(kw_gasto),
        "valorPagar": float(valor_pagar),
        "dataPagamento": data_pagamento,
        "mediaConsumo": calcular_media_consumo(kw_gasto),
    }
    st.session_state.contas_luz.append(conta)


def atualizar_conta(conta_id, data_leitura, numero_leitura, kw_gasto, valor_pagar, data_pagamento):
    for conta in st.session_state.contas_luz:
        if conta["id"] == conta_id:
            conta["mesReferencia"] = obter_mes_referencia(data_leitura)
            conta["dataLeitura"] = data_leitura
            conta["numeroLeitura"] = numero_leitura
            conta["kwGasto"] = float(kw_gasto)
            conta["valorPagar"] = float(valor_pagar)
            conta["dataPagamento"] = data_pagamento
            conta["mediaConsumo"] = calcular_media_consumo(kw_gasto)
            break


def excluir_conta(conta_id):
    st.session_state.contas_luz = [
        conta for conta in st.session_state.contas_luz
        if conta["id"] != conta_id
    ]


def contas_para_dataframe():
    if not st.session_state.contas_luz:
        return pd.DataFrame()

    dados = []
    for conta in st.session_state.contas_luz:
        dados.append({
            "ID": conta["id"],
            "Mês de Referência": conta["mesReferencia"],
            "Data da Leitura": conta["dataLeitura"].strftime("%d/%m/%Y"),
            "Nº da Leitura": conta["numeroLeitura"],
            "KW Gasto": conta["kwGasto"],
            "Valor a Pagar (R$)": f'{conta["valorPagar"]:.2f}',
            "Data do Pagamento": conta["dataPagamento"].strftime("%d/%m/%Y"),
            "Média de Consumo": conta["mediaConsumo"],
        })
    return pd.DataFrame(dados)


def obter_conta_por_id(conta_id):
    for conta in st.session_state.contas_luz:
        if conta["id"] == conta_id:
            return conta
    return None


def obter_menor_consumo():
    if not st.session_state.contas_luz:
        return None
    return min(st.session_state.contas_luz, key=lambda conta: conta["kwGasto"])


def obter_maior_consumo():
    if not st.session_state.contas_luz:
        return None
    return max(st.session_state.contas_luz, key=lambda conta: conta["kwGasto"])


# =========================================================
# INÍCIO
# =========================================================
inicializar_estado()

st.title(":bulb: Questão 01 — Conta de Luz")
st.markdown(
    """
Aplicação desenvolvida em **Python + Streamlit** para controle de contas de luz,
com cadastro mensal, listagem dos registros e consulta de **menor** e **maior consumo**.
"""
)

# Dados iniciais para facilitar testes
if not st.session_state.contas_luz:
    adicionar_conta(date(2005, 7, 4), 4166, 460, 206.43, date(2005, 7, 15))
    adicionar_conta(date(2005, 8, 2), 4201, 350, 157.07, date(2005, 8, 15))


aba1, aba2, aba3 = st.tabs(
    ["Cadastro", "Listagem e Gerenciamento", "Consultas"]
)


# =========================================================
# ABA 1 - CADASTRO
# =========================================================
with aba1:
    st.subheader("Cadastrar nova conta de luz")

    with st.form("form_cadastro_conta", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            data_leitura = st.date_input(
                "Data da leitura",
                value=date.today()
            )
            numero_leitura = st.number_input(
                "Nº da leitura",
                min_value=0,
                step=1
            )
            kw_gasto = st.number_input(
                "KW gasto no mês",
                min_value=0.0,
                step=1.0,
                format="%.2f"
            )

        with col2:
            valor_pagar = st.number_input(
                "Valor a pagar (R$)",
                min_value=0.0,
                step=0.01,
                format="%.2f"
            )
            data_pagamento = st.date_input(
                "Data do pagamento",
                value=date.today()
            )

        enviado = st.form_submit_button("Cadastrar conta")

        if enviado:
            if numero_leitura <= 0:
                st.error("Informe um número de leitura válido.")
            elif kw_gasto <= 0:
                st.error("Informe a quantidade de KW gasto.")
            elif valor_pagar <= 0:
                st.error("Informe o valor a pagar.")
            else:
                adicionar_conta(
                    data_leitura=data_leitura,
                    numero_leitura=int(numero_leitura),
                    kw_gasto=kw_gasto,
                    valor_pagar=valor_pagar,
                    data_pagamento=data_pagamento
                )
                st.success("Conta de luz cadastrada com sucesso!")


# =========================================================
# ABA 2 - LISTAGEM E GERENCIAMENTO
# =========================================================
with aba2:
    st.subheader("Contas cadastradas")

    df = contas_para_dataframe()

    if df.empty:
        st.info("Nenhuma conta cadastrada até o momento.")
    else:
        st.dataframe(df, use_container_width=True)

        st.markdown("---")
        st.subheader("Editar ou excluir conta")

        opcoes = {
            f'ID {conta["id"]} - {conta["mesReferencia"]}': conta["id"]
            for conta in st.session_state.contas_luz
        }

        registro_escolhido = st.selectbox(
            "Selecione uma conta",
            options=list(opcoes.keys())
        )

        conta_id = opcoes[registro_escolhido]
        conta = obter_conta_por_id(conta_id)

        if conta:
            with st.form("form_edicao_conta"):
                col1, col2 = st.columns(2)

                with col1:
                    nova_data_leitura = st.date_input(
                        "Data da leitura",
                        value=conta["dataLeitura"],
                        key=f"edit_data_leitura_{conta_id}"
                    )
                    novo_numero_leitura = st.number_input(
                        "Nº da leitura",
                        min_value=0,
                        step=1,
                        value=int(conta["numeroLeitura"]),
                        key=f"edit_numero_leitura_{conta_id}"
                    )
                    novo_kw_gasto = st.number_input(
                        "KW gasto no mês",
                        min_value=0.0,
                        step=1.0,
                        format="%.2f",
                        value=float(conta["kwGasto"]),
                        key=f"edit_kw_gasto_{conta_id}"
                    )

                with col2:
                    novo_valor_pagar = st.number_input(
                        "Valor a pagar (R$)",
                        min_value=0.0,
                        step=0.01,
                        format="%.2f",
                        value=float(conta["valorPagar"]),
                        key=f"edit_valor_pagar_{conta_id}"
                    )
                    nova_data_pagamento = st.date_input(
                        "Data do pagamento",
                        value=conta["dataPagamento"],
                        key=f"edit_data_pagamento_{conta_id}"
                    )

                col_btn1, col_btn2 = st.columns(2)
                salvar = col_btn1.form_submit_button("Salvar alterações")
                remover = col_btn2.form_submit_button("Excluir conta")

                if salvar:
                    if novo_numero_leitura <= 0:
                        st.error("Informe um número de leitura válido.")
                    elif novo_kw_gasto <= 0:
                        st.error("Informe a quantidade de KW gasto.")
                    elif novo_valor_pagar <= 0:
                        st.error("Informe o valor a pagar.")
                    else:
                        atualizar_conta(
                            conta_id=conta_id,
                            data_leitura=nova_data_leitura,
                            numero_leitura=int(novo_numero_leitura),
                            kw_gasto=novo_kw_gasto,
                            valor_pagar=novo_valor_pagar,
                            data_pagamento=nova_data_pagamento
                        )
                        st.success("Conta atualizada com sucesso!")
                        st.rerun()

                if remover:
                    excluir_conta(conta_id)
                    st.success("Conta removida com sucesso!")
                    st.rerun()


# =========================================================
# ABA 3 - CONSULTAS
# =========================================================
with aba3:
    st.subheader("Consultas de consumo")

    if not st.session_state.contas_luz:
        st.info("Cadastre contas para visualizar as consultas.")
    else:
        menor = obter_menor_consumo()
        maior = obter_maior_consumo()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Menor consumo",
                value=f'{menor["kwGasto"]:.2f} KW'
            )
            st.write(f'**Mês de referência:** {menor["mesReferencia"]}')
            st.write(f'**Nº da leitura:** {menor["numeroLeitura"]}')
            st.write(f'**Valor a pagar:** R$ {menor["valorPagar"]:.2f}')
            st.write(f'**Média de consumo:** {menor["mediaConsumo"]:.2f}')

        with col2:
            st.metric(
                label="Maior consumo",
                value=f'{maior["kwGasto"]:.2f} KW'
            )
            st.write(f'**Mês de referência:** {maior["mesReferencia"]}')
            st.write(f'**Nº da leitura:** {maior["numeroLeitura"]}')
            st.write(f'**Valor a pagar:** R$ {maior["valorPagar"]:.2f}')
            st.write(f'**Média de consumo:** {maior["mediaConsumo"]:.2f}')

        st.markdown("---")
        st.subheader("Resumo geral")

        total_contas = len(st.session_state.contas_luz)
        consumo_medio = sum(conta["kwGasto"] for conta in st.session_state.contas_luz) / total_contas
        valor_medio = sum(conta["valorPagar"] for conta in st.session_state.contas_luz) / total_contas

        col3, col4, col5 = st.columns(3)
        col3.metric("Total de contas", total_contas)
        col4.metric("Consumo médio", f"{consumo_medio:.2f} KW")
        col5.metric("Valor médio", f"R$ {valor_medio:.2f}")