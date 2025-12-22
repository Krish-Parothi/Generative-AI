from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq.chat_models import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.5,
    streaming=True,
    max_tokens=65533
)

messages = [

    SystemMessage(content="You are a Helpful Assistant"),
    HumanMessage(content="Tell me About Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(result.content))

print(messages)