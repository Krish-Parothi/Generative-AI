"""
Farmers were working hard in the fields, preparing the soil and planting seeds for 
the next season. The sun was bright, and the air smelled of earth and fresh grass. 
The Indian Premier League (IPL) is the biggest cricket league in the world. People 
all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates 
fear in cities and villages. When such attacks happen, they leave behind pain and 
sadness. To fight terrorism, we need strong laws, alert security forces, and support 
from people who care about peace and safety.

"""

"""
    In the first paragraph there is two different topics. And in 2nd paragraph there is a single topic.

    When we use semantic meaning based text splitter, the approach is all text should be seperate sentence by sentence.

    e.g: 1st sentence: "Farmers were working hard in the fields, preparing the soil and planting seeds for the next season."
    2nd sentence: "The sun was bright, and the air smelled of earth and fresh grass."

    3rd sentence: "The Indian Premier League (IPL) is the biggest cricket league in the world."

    4th sentence: "People all over the world watch the matches and cheer for their favourite teams."
    
    5th sentence: "Terrorism is a big danger to peace and safety."

    6th sentence: "It causes harm to people and creates fear in cities and villages."

    7th sentence: "When such attacks happen, they leave behind pain and sadness."

    8th sentence: "To fight terrorism, we need strong laws, alert security forces, and support 
from people who care about peace and safety."




Now we Use Embedding Model e.g Open AI Embedding Model.

Then Ye sentences ko one by one embedding model mein bhej ke unke embedding vectors generate/form krdo.

Then Sentence 1 ko compare kro sentence 2 and Sentence 3 to Sentence 4 se and so on..., then cosine similarity nikalo. If both sentences talk about same topic then dono ke beech mein similarity high hogi. for similarity we use: Cosine Similarity"

Sematic Meaning Based Text Splitter Uses Sliding Window Approach (comparison between sentences).
 
This is very latest text splitter.
"""

from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)

