from click import prompt
from fastapi import FastAPI
import fastapi
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
# import streamlit as st
from dotenv import load_dotenv
load_dotenv()


# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAPI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# model_openai = ChatOpenAI()
model_llama3 = Ollama(model="llama3")

prompt = ChatPromptTemplate.from_template("Write an essay with approximately 100 words on the topic : {topic}")

# add_routes(
#     app,
#     prompt1|model_openai,
#     path="/essay"
# )

add_routes(
    app,
    prompt|model_llama3,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)