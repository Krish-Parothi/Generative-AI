import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_classic.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_classic.document_loaders import YoutubeLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

api = YouTubeTranscriptApi()

video_id = "JxgmHe2NyeY"

try:
    transcript_list = api.fetch(
        video_id=video_id,
        languages=["en"]
    )
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("Captions are disabled for this video")

except NoTranscriptFound:
    print("No English captions found")

except VideoUnavailable:
    print("Video is unavailable")

except Exception as e:
    print(f"Unexpected error: {e}")



# Text Splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

# Embeddings
embeddings = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.index_to_docstore_id

# Retreival
retreiver = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":4})

# retreiver.invoke("lasso in regression?")


# Augumentation
llm =  ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.8,

)

prompt = PromptTemplate(
    template="""
You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the content is insufficient, just say you don't know

{context}

Question: {question}

""",
input_variables=['content','question']
)



question = "Tell the Whole Concept of Support Vector Machine Discussed in this video."

retreived_docs = retreiver.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retreived_docs)
# jo docs mile the unko join kiya hai


final_prompt = prompt.invoke({"context":context_text, "question":question})



answer = llm.invoke(final_prompt)


def format_docs(final_prompt):
    context_text = "\n\n".join(doc.page_content for doc in retreived_docs)
    return context_text

parallel_chain = RunnableParallel({
    "context" : retreiver | RunnableLambda(format_docs),
    "question" : RunnablePassthrough()
})


# parallel_chain.invoke('What is SVM in detail?')


parser = StrOutputParser()


main_chain = parallel_chain | prompt | llm | parser

main_chain.invoke("Can you summarize the SVM from the video?")