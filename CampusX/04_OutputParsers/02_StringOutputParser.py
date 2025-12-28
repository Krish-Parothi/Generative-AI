from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser() # result se string output nikala Since LLM Meta Data Bhi de deta hai isilye stroutputparsers use krte hai and next step mein pass kr diya.
# Parsers are well related with chains in langchain

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"black hole"})

print(result)