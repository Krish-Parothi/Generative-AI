import streamlit as st
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.5,
    streaming=True,
    max_tokens=65533
)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
Explain the research paper titled "{paper_input}".

Explanation style: {style_input}
Explanation length: {length_input}

Provide a clear, structured explanation.
"""
)

if st.button("Summarize"):
    prompt = template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )

    placeholder = st.empty()
    full_text = ""

    for chunk in model.stream(prompt):
        if chunk.content:
            full_text += chunk.content
            placeholder.markdown(full_text)
