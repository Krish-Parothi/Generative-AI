from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv")

docs = loader.load()

print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)
print(docs[1].metadata)
print(docs[1].page_content)