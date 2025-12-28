# In Structured Output Parser We tell LLM about the kind of Schema We Wanted.
# This Was the Difference Between StructuredOutputParser and JSONOutputParser.

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
import os


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

# In ResponseSchema we send a list of ResponseSchema Objects

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 About the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 About the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 About the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 Facts About {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions': parser.get_format_instructions}
)

chain = template | model | parser


result = chain.invoke({"topic":"Black Hole"})


print(result)

# Output: 

# {'fact_1': 'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape once it crosses the event horizon.', 

# 'fact_2': "The size of a black hole's event horizon, called the Schwarzschild radius, is directly proportional to its mass; a black hole with the mass of the Sun would have a radius of about 3 kilometers.", 

# 'fact_3': 'Black holes can emit radiation, known as Hawking radiation, due to quantum effects near the event horizon, causing them to lose mass over extremely long timescales.'}


## Draw Back of Structured Output Parser is We cannot do Data Validation.