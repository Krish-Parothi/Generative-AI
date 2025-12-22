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

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


if st.button("Summarize"):
    placeholder = st.empty()
    full_text = ""

    user_input = f"""
    Explain the research paper titled "{paper_input}".

    Explanation style: {style_input}
    Explanation length: {length_input}
    """

    for chunk in model.stream(user_input):
        if chunk.content:
            full_text += chunk.content
            placeholder.markdown(full_text)