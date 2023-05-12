import streamlit as st
import pandas as pd

st.title('Read a file using Pandas')

# Allow the user to select a file from their local file system
file = st.file_uploader("Choose a file")

# If the user selected a file and clicked the "Read" button
if st.button('Read'):
    try:
        # Read the file using Pandas
        df = pd.read_excel(file)
        # Display the DataFrame using Streamlit
        st.write(df)
    except AttributeError:
        st.write('No file selected')
    except Exception as e:
        st.write(f'Error reading file: {e}')
