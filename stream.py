import streamlit as st
import pandas as pd

option = st.selectbox(
    'What database are you working on?',
    ('Sicredi', 'Banrisul', 'Cotrirosa', 'Circulo', 'São José', 'Sinoserra')
)

col1, _ = st.columns(2)

with col1:
    text_input = st.text_input(
        "Digite o Caminho do Arquivo (C:/) 👇"
    )
    if text_input:
        st.write("You entered: ", text_input)
        
    if st.button('Load data'):
        df = pd.read_excel(text_input)
        st.dataframe(df)
