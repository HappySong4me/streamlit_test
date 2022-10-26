import streamlit as st

st.title('PYTHON & Streamlit')
st.header('Hi')
agree = st.checkbox('a or b')
if agree:
    st.write('Good!!')
