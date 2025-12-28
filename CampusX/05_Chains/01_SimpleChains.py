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

)

prompt = PromptTemplate(
    template="Generate 5 Interesting Facts About {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic":"Indian Food"})

print(result)

chain.get_graph().print_ascii()
# You can visualize your Chain Procedure here, By using this function.