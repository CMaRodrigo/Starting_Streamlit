import streamlit as st

option = st.selectbox(
    'What database are you working on?',
    ('Sicredi', 'Banrisul', 'Cotrirosa', 'Circulo', 'São José', 'Sinoserra'))

st.write('You selected:', option)

