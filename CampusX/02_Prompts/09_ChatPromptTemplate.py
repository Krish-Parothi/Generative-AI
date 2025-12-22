from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

chat_template = ChatPromptTemplate([
    ("system","You are a Helpful customer support Agent."),
    MessagesPlaceholder(variable_name="Chat_History"),
    ("Human","{query}")
])


chat_history = []
with open('Chat_History.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)


prompt = chat_template.invoke({"chat_history": chat_history, "query": "Where is my Refund?"})

print(prompt)