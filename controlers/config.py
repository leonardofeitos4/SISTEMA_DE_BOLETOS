import streamlit as st

def set_page_configuration():
    st.set_page_config(
        page_title="Jampa Chinelos",
        page_icon="🩴",
        layout="wide",
        initial_sidebar_state="auto"
    )

def show_title():
    st.title('Sistema Jampa')