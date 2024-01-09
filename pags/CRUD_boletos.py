import pandas as pd
from streamlit_option_menu import option_menu
from pags.home import fundo
from pags.adicionar import adicionar_boleto
from pags.deletar import deletar_boleto
from pags.editar import editar_boleto

acoes = ['Adicionar', 'Editar', 'Deletar']
icons = ['bi bi-file-earmark-plus', "bi bi-pencil-square","bi bi-file-earmark-x"]


with pd.ExcelFile('boletos_jampa.xlsx') as xls:
        opcs = list(pd.read_excel(xls).NOME_CLIENTE.unique())


def opcoes():
    selected = option_menu(
            menu_title=None,  # required
            options=acoes,
            icons=icons,
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
    return selected


def main():
    # fundo()
    
    escolha = opcoes()
    
    if escolha == acoes[0]:
        adicionar_boleto()
        
    if escolha == acoes[1]:
        editar_boleto()
    
    if escolha == acoes[2]:
        deletar_boleto()
