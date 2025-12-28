from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal, Optional
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("NEW_GROQ_API_KEY"),
    temperature=0,
)

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give the Sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into posivite or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2 

result = classifier_chain.invoke({"feedback":"This is a Terrible Smart Phone"})

# print(result.sentiment)
# output: negative
# print(result.sentiment) ki jagah print(result) bhi likh skte but uske liye classifier_chain.invoke({}).sentiment  likhna hoga.

print(result)