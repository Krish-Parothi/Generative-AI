from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict
import os 

load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

#Schema
class Review(TypedDict):
    summary:str
    sentiment: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke('''I Brought that product at home but cpu was working fine but gpu was working very bad i think i have done mistake buying this product.''')

print(result)