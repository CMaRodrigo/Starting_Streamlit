import streamlit as st
import pandas as pd

option = st.selectbox(
    'What database are you working on?',
    ('Sicredi', 'Banrisul', 'Cotrirosa', 'Circulo', 'São José', 'Sinoserra'))

col1 = st.columns(2)

with col1:
    text_input = st.text_input(
        "Digite o Caminho do Arquivo (C:/) 👇"
    )
    if text_input:
        st.write("You entered: ", text_input)




df = pd.read_excel("T:/Dados/Analytics/1. Projetos/18. Sicredi/Picsel/Precificação da carteira/consolidada.xlsx")
st.dataframe(df)  