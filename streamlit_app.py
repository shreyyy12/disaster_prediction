import streamlit as st
import requests

def register_user(username, email, password):
    url = 'http://localhost:5000/register'
    data = {'username': username, 'email': email, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

st.title('User Registration')

username = st.text_input('Username')
email = st.text_input('Email')
password = st.text_input('Password', type='password')

if st.button('Register'):
    if username and email and password:
        result = register_user(username, email, password)
        st.success(result['message'])
    else:
        st.error('Please fill in all fields.')
