import streamlit as st
from streamlit_option_menu import option_menu
from pags.dados import adicionar_linha_excel, get_data
import phonenumbers as phone
import pandas as pd
from pags.dados import get_clientes, get_infos_cliente
from numpy import nan

def formatar_telefone(telefone):
    try:
        parsed_telefone = phone.parse(telefone, "BR")
        telefone_formatado = phone.format_number(parsed_telefone, phone.PhoneNumberFormat.NATIONAL)
        if len(telefone_formatado) != 15:
            return "Número de telefone inválido"
        return telefone_formatado
    except:
        return "Número de telefone inválido"


def cliente_novo():
    st.markdown("#### Nome do Cliente:")
    nome_cliente = st.text_input("", key='nome_cliente')
    
    st.markdown("#### Nome do Mercado:")
    nome_mercado = st.text_input("",key='nome_mercado')

    # Campo de entrada formatado para telefone usando componente personalizado
    st.markdown("#### Telefone:")
    telefone_input = st.text_input("", key='telefone')

    # Formata o telefone e exibe no campo de entrada
    telefone_formatado = formatar_telefone(telefone_input)
    st.markdown(f"##### Telefone formatado: {telefone_formatado}")

    st.markdown("#### Valor:")
    valor = st.number_input("", key='valor')
    
    st.markdown("#### Situação do Boleto:")
    situacao = st.selectbox("", ["ABERTO", "PAGO"], key='situacao_boleto')

    # Marca
    st.markdown("#### Marca:")
    marca = st.selectbox("", ["JAMPA", "HAVAIANA"], key='marca')

    # Campo para a data de vencimento
    st.markdown("#### Data de Vencimento:")
    data_vencimento = st.date_input("", key='data_vencimento')

    
  # Verificar se todos os campos obrigatórios foram preenchidos
    if nome_cliente and nome_mercado and valor and data_vencimento:
        if st.button("Adicionar"):
            cadastrar_boleto(nome_cliente, nome_mercado, data_vencimento, telefone_input, valor, situacao, marca,)
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de adicionar o boleto.")


def cliente_antigo(clientes):
    st.markdown('#### Nome do Cliente:')
    nome_cliente = st.selectbox("", clientes, key='nome_cliente', index=None)
    
    mercados, telefones = get_infos_cliente(nome_cliente)
    
    st.markdown('#### Nome do Mercado:')
    nome_mercado = st.selectbox("", mercados,key='nome_mercado:')

    st.markdown('#### Telefone:')
    telefone_input = st.selectbox("", telefones, key='telefone')
    
    st.markdown("#### Valor:")
    valor = st.number_input("", key='valor')
    
    st.markdown("#### Situação do Boleto:")
    situacao = st.selectbox("", ["ABERTO", "PAGO"], key='situacao_boleto')

    # Marca
    st.markdown("#### Marca:")
    marca = st.selectbox("", ["JAMPA", "HAVAIANA"], key='marca')

    # Campo para a data de vencimento
    st.markdown("#### Data de Vencimento:")
    data_vencimento = st.date_input("", key='data_vencimento')

  # Verificar se todos os campos obrigatórios foram preenchidos
    if nome_cliente and nome_mercado and valor and data_vencimento:
        if st.button("Adicionar"):
            cadastrar_boleto(nome_cliente, nome_mercado, data_vencimento, telefone_input, valor, situacao, marca,)
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de adicionar o boleto.")




def adicionar_boleto():
    clientes = get_clientes()
    
    st.markdown("## Cadastro de Boletos")
    st.markdown("#### É um novo cliente?")

    existe_cliente_novo = cliente_existe()

    if existe_cliente_novo:
        cliente_novo()
    else:
        cliente_antigo(clientes)
        

    
def cadastrar_boleto(nome_cliente, nome_mercado, data_vencimento, telefone_input, valor, situacao, marca,):
    adicionar_linha_excel([nome_cliente, nome_mercado, data_vencimento, telefone_input, valor, situacao, marca,])
    
    st.markdown('### Boleto Cadastrado com Sucesso!')

def cliente_existe():
    selected = option_menu(
        menu_title='',  # required
        options=["Sim", "Não"],  # required
        icons=["bi bi-check", "bi bi-x-lg"],
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    
    
    return selected == "Sim"