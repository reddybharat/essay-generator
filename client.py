from urllib import response
import requests
import streamlit as st

# def get_ollama_response(input_openai):
#     response = requests.post(
#         "http://localhost:8000/poem/invoke",
#         json = {'input':{'topic':input_openai}}
#     )
#     return response.json()['output']['content']


def get_ollama_response(input_ollama):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json = {'input':{'topic':input_ollama}}
    )
    return response.json()['output']

# Streamlit f/w
st.title('Langchain App with LLAMA3 API')
input_ollama = st.text_input("Write an essay on")

if input_ollama :
    st.write(get_ollama_response(input_ollama))