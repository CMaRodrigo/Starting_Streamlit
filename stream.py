import streamlit as st
import pandas as pd

st.title('Read a CSV file using Pandas')

# Prompt the user to enter a file path
file_path = st.text_input('Enter the path to the CSV file')

# If the user entered a file path and clicked the "Read CSV" button
if st.button('Read CSV'):
    try:
        # Read the CSV file using Pandas
        df = pd.read_csv(file_path)
        # Display the DataFrame using Streamlit
        st.write(df)
    except FileNotFoundError:
        st.write(f"File '{file_path}' not found")
