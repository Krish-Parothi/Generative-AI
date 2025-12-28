# PydanticOutputParsers are the Strucured Output Parsers in Langchain that uses Pydantic Models to enforce schema Validation when processing LLM Responses.

# Why to Use PydanticOutputParser?

# Strict Schema Enforcement - Ensures that LLM responses follow a well-defined structure.
# Type Safety - Automatically converts LLM Outputs into Python Objects.
# Easy Validation - UsesPydantic's Built-in Validation to Catch incorrect or missing data
# Seamless Integration - Works Well with other Langchain Components.



from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
import os


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

# Person Class Inherit from BaseModel
class Person(BaseModel): 
    name: str = Field(description="Name of the Person")
    age: int = Field(gt=18, description="Age of the Person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# text='Generate the name, age and city of a fictional indian person \n The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Name of the Person", "title": "Name", "type": "string"}, "age": {"description": "Age of the Person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"}, "city": {"description": "Name of the city the person belongs to", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'


# This Part is done by parser: 
# The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Name of the Person", "title": "Name", "type": "string"}, "age": {"description": "Age of the Person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"}, "city": {"description": "Name of the city the person belongs to", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'

prompt = template.invoke({'place':"indian"})

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

# Output: name='Arjun Mehta' age=29 city='Jaipur'