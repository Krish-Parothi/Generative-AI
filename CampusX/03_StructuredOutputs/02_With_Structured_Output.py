from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import os 

load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

#Schema
class Review(TypedDict):


    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list."]
    summary:Annotated[str, "A Brief Summaary of the Review"]
    sentiment: Annotated[str,"Return Sentiment of the Review whether Positive, Negative or Neutral"]
    pros: Annotated[Optional[list[str]],"Write Down all the pros inside the list."]
    cons: Annotated[Optional[list[str]],"Write Down all the cons inside the list."]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke('''I Brought that product at home but cpu was working fine but gpu was working very bad i think i have done mistake buying this product.''')

print(result)
print(result['summary'])
print(result['sentiment'])