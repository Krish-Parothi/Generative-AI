import streamlit as st
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.5,
    streaming=True,
    max_tokens=65533 # 65536 is limit of max_tokens
)
st.header("Research Tool")

user_input = st.text_input("Enter Your Prompt")

if st.button("Summarize"):
    placeholder = st.empty()
    full_text = ""

    for chunk in model.stream(user_input):
        if chunk.content:
            full_text += chunk.content
            placeholder.markdown(full_text)