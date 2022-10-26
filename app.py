import streamlit as st

st.title('Hello World!')

st.info("숨고숨고")
agree = st.checkbox("I agree")
if agree:
    st.write("Great")