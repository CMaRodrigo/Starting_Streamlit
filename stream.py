import streamlit as st

def base():
    option = st.selectbox(
        'What database are you working on?',
        ('Sicredi', 'Banrisul', 'Cotrirosa', 'Circulo', 'São José'))
    st.write('You selected:', option)

