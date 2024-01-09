import streamlit as st
from pags.dados import get_clientes, get_infos_cliente, deletar_linha_excel, get_datas, get_valores

def deletar_boleto():
    st.markdown("## Deletar Boleto")

    # Obter a lista de clientes existentes
    clientes = get_clientes()

    # Selecionar um cliente existente
    st.markdown('#### Nome do Cliente:')
    nome_cliente = st.selectbox("", clientes, key='nome_cliente', index=None)

    # Obter informações adicionais sobre o cliente selecionado
    mercados, _ = get_infos_cliente(nome_cliente)

    # Preencher as informações do boleto a ser deletado
    st.markdown('#### Nome do Mercado:')
    nome_mercado = st.selectbox("", mercados, key='nome_mercado', index=None)

    st.markdown("#### Valor:")
    valores = get_valores(nome_cliente)
    valor = st.selectbox("", valores,key='valor2', index=None)

    st.markdown("#### Data de Vencimento:")
    datas = get_datas(nome_cliente)
    data_vencimento = st.selectbox("", datas,key='data_vencimento', index=None)

    # Verificar se todos os campos obrigatórios foram preenchidos
    if nome_cliente and nome_mercado and valor and data_vencimento:
        if st.button("Deletar Boleto"):
            if deletar_linha_excel(nome_cliente, nome_mercado, valor, data_vencimento):
                st.markdown("### Boleto deletado com sucesso.")
            else:
                st.markdown("### Boleto não encontrado.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de deletar o boleto.")
