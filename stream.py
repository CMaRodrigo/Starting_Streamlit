import streamlit as st
import pandas as pd
import openpyxl
import tempfile
import os

st.title('Read a file using Openpyxl')

# Allow the user to select a file from their local file system
file = st.file_uploader("Choose a file")

# If the user selected a file and clicked the "Read" button
if st.button('Read'):
    try:
        # Save the file to a temporary location
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(file.read())
        temp_file.close()
        # Load the workbook using Openpyxl
        wb = openpyxl.load_workbook(temp_file.name)
        # Select the sheet to read
        sheet = wb['seguro']
        # Read the sheet into a list of lists
        rows = sheet.values
        data = []
        for row in rows:
            data.append(list(row))
        # Create a Pandas dataframe from the data
        df = pd.DataFrame(data[1:], columns=data[0])
        # Display the dataframe using Streamlit
        st.write(df)
        # Delete the temporary file
        os.unlink(temp_file.name)
    except AttributeError:
        st.write('No file selected')
    except Exception as e:
        st.write(f'Error reading file: {e}')
