import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader, SeleniumURLLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5,
)

prompt = PromptTemplate(
    template="Anwer the following Question \n {question} from the following text \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=12&t=2287s"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = ""

for chunks in chain.stream({'question':'What is the Lecture is about?','text':docs[0].page_content}):
    for ch in chunks:
        result += ch
        print(ch, end="", flush=True)


chain.get_graph().print_ascii()