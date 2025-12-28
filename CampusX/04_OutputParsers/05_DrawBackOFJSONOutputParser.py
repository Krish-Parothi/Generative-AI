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
    template="Give me 5 Facts About {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'Black Hole'})
print(result)


# Draw Back of JSONOutputParsers: 
# Json Object Banwa lete ho LLM but aap koi schema enforce nahi kr skte.
# There is no Gurantee that the llm will give u a Json Output as you wanted.

# Output:
# {'facts': ["A black hole's event horizon is the point of no return; once any matter or light crosses it, escape is impossible.", 'Black holes can be classified by mass: stellar‑mass (a few to tens of solar masses), intermediate‑mass (hundreds to thousands of solar masses), and supermassive (millions to billions of solar masses).', 'Time runs slower near a black hole due to extreme gravitational time dilation; an observer far away would see processes near the event horizon appear to slow down dramatically.', 'Hawking radiation, a quantum effect predicted by Stephen Hawking, allows black holes to emit particles and slowly lose mass over incredibly long timescales.', 'The first image of a black hole’s shadow was captured in 2019 by the Event Horizon Telescope, revealing the silhouette of the supermassive black hole in galaxy M87.']}