from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="Ypu are a Helpful {domain} assistant"),
#     HumanMessage(content="Explain in Simple Terms, What is {topic}")
# ])
# If You Use this above technique thw output will be little weird so better to use the one given below.


chat_template = ChatPromptTemplate([
    ("system","You are a Helpful {domain} expert"),
    ("human","Explain in simple terms, what is {topic}")
])

# Use this Above on eonly as per langchain documentation.
# or You can use this below one, both will give same answer

# chat_template = ChatPromptTemplate.from_messages([
#     ("system","You are a Helpful {domain} expert"),
#     ("human","Explain in simple terms, what is {topic}")
# ])

prompt = chat_template.invoke({"domain":"Cricket", "topic":"Strike Rate"})

print(prompt)