from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import os


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,

)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a Fictional Person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

# result = chain.invoke()
# #   File "C:\Users\Krish\OneDrive\Desktop\GITHUB\Generative AI\Generative-AI\CampusX\04_OutputParsers\04_JSONOutputParsers.py", line 27, in <module>
#     result = chain.invoke()
# TypeError: RunnableSequence.invoke() missing 1 required positional argument: 'input'

# This Error will come when you dont put any input variable in prompt template, if you dont ahve any input variable then inside invoke function send a empty Dictionary.

result = chain.invoke({})
print(result)


# Draw Back of JSONOutputParsers: 
# Json Object Banwa lete ho LLM but aap koi schema enforce nahi kr skte.