from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict
import os 

load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.5,
    streaming=True,
    max_tokens=65533
)

model.invoke("")