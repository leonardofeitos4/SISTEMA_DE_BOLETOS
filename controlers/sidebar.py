import streamlit as st
from streamlit_option_menu  import option_menu
import os

opcoes = ['Home', 'Boletos', 'Download']
icons = ["house", "bi bi-folder2", "bi bi-download"]

def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=opcoes,
            icons=icons,
            menu_icon="cast",
            default_index=0,
        )
    return selected



def sidebar_content():
    # Verificar se os arquivos de imagem existem
    
    logo_nossa_path = "./assets/logo_nossa.png"

    # Criar duas colunas na sidebar
    col1, col2 = st.sidebar.columns(2)

    # Adicionar a primeira imagem à primeira coluna
    

    # Adicionar a segunda imagem à segunda coluna
    col2.image(logo_nossa_path, width=150)
    
    st.sidebar.markdown('#### Desenvolvido por Leonardo Feitosa, Lucas vicinius, Gabriel Batista, Nercino Neto')

