from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='File_Directory',
    glob="*.pdf", # Sabhi pdf files ko load karo.
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
# print(docs[324].page_content)
# print(docs[324].metadata)

