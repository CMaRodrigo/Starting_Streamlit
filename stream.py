import streamlit as st

option = st.selectbox(
    'What database are you working on?',
    ('Sicredi', 'Banrisul', 'Cotrirosa', 'Circulo', 'São José', 'Sinoserra'))

col1, col2 = st.columns(2)

with col2:
    text_input = st.text_input(
        "Digite o Caminho do Arquivo (C://) 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    if text_input:
        st.write("You entered: ", text_input)


