import streamlit as st

st.title('Hi, Streamlit')

st.info("파이참 어려워")
agree = st.checkbox("Do you agree?")
if agree:
    st.write("Me, too!")