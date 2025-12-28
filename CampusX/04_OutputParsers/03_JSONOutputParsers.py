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

# In JsonOutputParsers, During Making Prompts, We send Additional Instructions that what type of output we wanted. 

# User Wont give format_instruction in the promptTemplate, Runtime ke pehele hi vo variable ki place fill ho jaati hai. with the help of get_format_instruction() function call.

# That is why it is called as partial variable.

prompt = template.format()

print(prompt)

# Output: Give me the name, age and city of a Fictional Person 
 #        Return a JSON object.


result = model.invoke(prompt)

print(result)

# output: 
# content='```json\n{\n  "name": "Lena Marlowe",\n  "age": 34,\n  "city": "Cedarbrook"\n}\n```' additional_kwargs={'reasoning_content': 'The user asks: "Give me the name, age and city of a Fictional Person. Return a JSON object."\n\nWe can comply. Provide a fictional person with name, age, city. Provide JSON. No policy issues. Just produce JSON.'} response_metadata={'token_usage': {'completion_tokens': 93, 'prompt_tokens': 90, 'total_tokens': 183, 'completion_time': 0.191159019, 'completion_tokens_details': {'reasoning_tokens': 51}, 'prompt_time': 0.003326249, 'prompt_tokens_details': None, 'queue_time': 0.049603481, 'total_time': 0.194485268}, 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': 'fp_626f3fc5e0', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'} id='lc_run--019b6526-b23b-7610-a31b-63adf9ed6301-0' usage_metadata={'input_tokens': 90, 'output_tokens': 93, 'total_tokens': 183, 'output_token_details': {'reasoning': 51}}



print(result.content)

# Output: 
# ```json
# {
#   "name": "Lena Marlowe",
#   "age": 34,
#   "city": "Cedarbrook"
# }
# ```


final_result = parser.parse(result.content)

print(final_result)
print(type(final_result))

# Output: {'name': 'Lena Marlowe', 'age': 34, 'city': 'Cedarbrook'}
# <class 'dict'>
# Python JSON Objects Ko Dictionary k Jaise Treat Krta hai

print(final_result['name'])
# Output: Lena Marlowe