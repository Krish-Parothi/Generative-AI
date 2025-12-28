from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

# 1st Prompt
template1 = PromptTemplate(
    template="Write a Detailed Report on {topic}",
    input_variables=['topic']
)
# 2nd Prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:  {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({"topic":"Blackhole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content})

result1 = model.invoke(prompt2)

print(result1.content)