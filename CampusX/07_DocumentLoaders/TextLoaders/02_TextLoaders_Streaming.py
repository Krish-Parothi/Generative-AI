from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    max_tokens=1024
)

prompt = PromptTemplate(
    template="Write a summary for the following {text}",
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

# print(docs)
# print(type(docs))
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

result = ""


for chunks in chain.stream({'text':docs[0].page_content}):
    for ch in chunks:
        result += ch
        print(ch, end="", flush=True)
