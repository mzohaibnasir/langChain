#  integrate our code with openAI API
import os
import langchain
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st


os.environ["OPENAI_API_KEY"] = openai_key
# streamlit framework

st.title("Langchain DEmo with openai API")

input_text = st.text_input("Search the topic you want")

# openai  llms

llm = OpenAI(temprature=0.8)


if input_text:
    st.write(llm(input_text))


# streamlit run main.py
