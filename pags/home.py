import pandas as pd
import streamlit as st
from datetime import datetime, date
from babel.numbers import format_currency
import base64

def fundo():
    local_image_path = "assets/fundo.jpg"

    with open(local_image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    data_url = f"data:image/jpeg;base64,{base64_image}"

    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("{data_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: local;
            width: 100vw;
            height: 100vh;
        }}

        [data-testid="stSidebar"] > div:first-child {{
        background-image: url("../assets/fundo2.jpg");
        background-position: center;
        margin-left: 0;
        background-repeat: no-repeat;
        background-size: contain;
        background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}

        [data-testid="stToolbar"] {{
        right: 2rem;
        }}
        <style>
    """


    st.markdown(page_bg_img, unsafe_allow_html=True)

def read_data(file_path):
    with pd.ExcelFile(file_path) as xls:
        return pd.read_excel(xls)

def filter_by_name(data, term):
    return data[(data['NOME_MERCADO'].str.contains(term, case=False)) |
                (data['NOME_CLIENTE'].str.contains(term, case=False))]

def filter_by_status_and_date(data, status, start_date, end_date):
    return data[(data['SITUACAO'].isin(status)) &
                (data['DATA_VENCIMENTO'].between(start_date, end_date))]

def display_data(data, title):
    st.write(f"Exibindo dados {title}")
    st.dataframe(data)

def display_total_value(data, status):
    total_value = data['VALOR'].sum()
    formatted_total_value = format_currency(total_value, 'BRL', locale='pt_BR')
    st.write(f"Valor Total {status}: {formatted_total_value}")

def main():
    fundo()
    planilha_path = "boletos_TESTES.xlsx"
    dados = read_data(planilha_path)

    sele = st.sidebar.selectbox(
        'Buscar',
        ('Nome', 'Situação'))

    if sele == 'Nome':
        termo_busca = st.sidebar.text_input('Buscar por:', 'Cliente').upper()
        dados_filtrados = filter_by_name(dados, termo_busca)
        display_data(dados_filtrados, f"do cliente ou mercado {termo_busca}")

        for status in ['ABERTO', 'PAGO']:
            display_total_value(dados_filtrados[dados_filtrados['SITUACAO'] == status], status)

        display_total_value(dados_filtrados, f"para {termo_busca}")

    elif sele == 'Situação':
        options = st.sidebar.multiselect(
            'Selecione a situação',
            ['ABERTO', 'PAGO'],
            ['ABERTO', 'PAGO'])

        today = datetime.now()
        Ano_atual = today.year 
        jan_1 = date(Ano_atual, 1, 1)
        dec_31 = date(Ano_atual, 12, 31)

        d = st.sidebar.date_input(
            "Selecione a data",
            (jan_1, date(Ano_atual, 1, 7)),
            jan_1,
            dec_31,
            format="DD.MM.YYYY",
        )

        if len(d) == 2:
            start_date_str = d[0].strftime("%Y-%m-%d")
            end_date_str = d[1].strftime("%Y-%m-%d")
            st.write(f"Data de inicio: {start_date_str}, Data final: {end_date_str}, Opção selecionada: {options}")
            
            dados_filtrados = filter_by_status_and_date(dados, options, start_date_str, end_date_str)
            display_data(dados_filtrados, f"por situação: {options}")
            display_total_value(dados_filtrados, options)

        else:
            st.warning("Selecione um intervalo de datas para filtrar.")
        
