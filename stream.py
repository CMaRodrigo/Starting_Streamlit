import streamlit as st

#Teste

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#----------

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#--------------

genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

#---------

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
