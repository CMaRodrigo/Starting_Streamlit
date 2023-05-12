import streamlit as st
import pandas as pd
import openpyxl

st.title('Read a file using Pandas')

# Allow the user to select a file from their local file system
file = st.file_uploader("Choose a file")

# Load the workbook using Openpyxl
wb = openpyxl.load_workbook(file)

# Select the sheet to read
sheet = wb['seguro']

# Read the sheet into a list of lists
rows = sheet.values
data = []
for row in rows:
    data.append(list(row))

# Create a Pandas dataframe from the data
df = pd.DataFrame(data[1:], columns=data[0])
st.write(df)
#teste
