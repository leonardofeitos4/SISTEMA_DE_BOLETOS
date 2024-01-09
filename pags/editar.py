import streamlit as st
from streamlit_option_menu import option_menu
from pags.dados import get_clientes, get_infos_cliente, get_valores, get_datas, get_situacao, editar_linha_excel


def editar_boleto():
    st.markdown("## Editar Boleto")

    # Obter a lista de clientes existentes
    clientes = get_clientes()

    # Selecionar um cliente existente
    st.markdown('#### Nome do Cliente:')
    nome_cliente = st.selectbox("", clientes, key='nome_cliente', index=None)

    # Obter informações adicionais sobre o cliente selecionado
    mercados, _ = get_infos_cliente(nome_cliente)

    # Preencher as informações do boleto a ser editado
    st.markdown('#### Nome do Mercado:')
    nome_mercado = st.selectbox("", mercados, key='nome_mercado', index=None)

    st.markdown("#### Valor:")
    valores = get_valores(nome_cliente)
    valor = st.selectbox("", valores, key='valor', index=None)

    st.markdown("#### Data de Vencimento:")
    datas = get_datas(nome_cliente)
    data_vencimento = st.selectbox("", datas, key='data_vencimento', index=None)

    if nome_cliente and nome_mercado and valor and data_vencimento:

        # Adicionar campos de edição
        st.markdown("## Campos de Edição")
        situacao = get_situacao(nome_cliente, nome_mercado, valor, data_vencimento)
    
        st.markdown(f"### Situação Atual: {situacao}")
        nova_situacao = st.selectbox("Nova Situação:", ["ABERTO", "PAGO"])
    
        st.markdown(f"### Valor Atual do Boleto: {valor}")
        novo_valor = st.number_input("Novo valor", valor)
    
        st.markdown(f"### Data de Vencimento Atual: {data_vencimento}")
        nova_data_vencimento = st.date_input("Nova Data de Vencimento", key='data_vencimento_att')


        editar = [(3,nova_data_vencimento), (5,novo_valor), (6,nova_situacao)]

        if nova_situacao == 'PAGO':
            st.markdown(f"### Data de Pagamento do Boleto:")
            data_pagamento = st.date_input("", key='data_pagamento_att')
            editar.append((8,data_pagamento))
            
        
        dados_antigo = [nome_cliente, nome_mercado, data_vencimento, valor]
        if st.button("Editar Boleto"):
            if editar_linha_excel(dados_antigo, editar):
                st.markdown("### Boleto editado com sucesso.")
            else:
                st.markdown("### Boleto não encontrado.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de editar o boleto.")
    