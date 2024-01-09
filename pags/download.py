import streamlit as st

def generate_boleto_file():
    file_name = 'boletos_jampa.xlsx'
    with open(file_name, "rb") as template_file:
        template_byte = template_file.read()

        st.download_button(label="Click to Download Template File",
                           data=template_byte,
                           file_name="boleto_jampa.xlsx",
                           mime='application/octet-stream')

def main():
    generate_boleto_file()