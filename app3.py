import streamlit as st

st.header('display json')
st.json({'data': 'name'})
st.header('display code')
st.code('''
def sayHello():
    print('Hello Streamlit')
''', language='python')

col1, col2, col3 = st.columns(3)
col1.metric('Temperature', '70 F', '1.2 f')
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')

name = 'Jeong Song'
if st.button('Submit', key=1):
    st.write(f'Name: {name}')
if st.button('Submit', key=2):
    st.write(f'Full Name: {name}')
