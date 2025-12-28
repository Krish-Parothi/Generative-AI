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

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a Detailed Report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 Pointer Summary from the following text \n {text}",
    input_variables=["text"]
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = ""

for chunk in chain.stream({"topic": "Indian Food"}):
    for ch in chunk:
        result += ch
        print(ch, end="", flush=True)


chain.get_graph().print_ascii()