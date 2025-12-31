from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='File_Directory',
    glob="*.pdf", # Sabhi pdf files ko load karo.
    loader_cls=PyPDFLoader
)

# "**/*.txt" --> All .txt files in all subfolders
# "*.pdf" --> All .pdf files in the root directory.
# "data/*.csv" --> All .csv files in the data/ folder
# "**/*" --> All files (any type, all folders)
# ** = recursive search through subfolders


docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
print(docs[324].page_content)
print(docs[324].metadata)


# Some Important Things to Notice: 

# 1) since there are 3 PDF in folder so it is taking too much time to load about 10-12 seconds. 

# What if there are 100 pdfs then?? It will take too much time to load.

# 2nd Problem: We are loading these pdfs in RAM for the operations to be performed. but if there are 100 or 500 PDFs then unko ek sath load krna bhi possible nahi hai RAM mein.

# For these problem we have Lazy Loading.