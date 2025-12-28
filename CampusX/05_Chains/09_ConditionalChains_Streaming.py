from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
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

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback'],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback'],
)



classifier_chain = prompt1 | model | parser2 


# We can do if else with chains using runnable branch.
# In RunnableBranch we Put Multiple Tuples and in that tuple we have a condition and if that condition is true then uske side mein ek aur parametetr rehta hai jo ki ek chain hai, vo execute hoga. 
# If no condition met then last mein default chain run krte ho.
branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x:"Could Not Find Sentiment")
)
# Here is x is (sentiment = 'positive')
# Since we dont have default chain so we will run simple lambda function i.e lambda x: "could not find sentiment" but this is not chain, so we have to convert it into runnable by using runnablelambda.

chain = classifier_chain | branch_chain # final chain

# chain.invoke({"feedback":"This is a Terrible phone"})

result = ""

for chunks in chain.stream({"feedback":"This is a Terrible phone"}):
    for ch in chunks:
        result += ch
        print(ch, end="", flush=True)

chain.get_graph().print_ascii()