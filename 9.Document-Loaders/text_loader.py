from langchain_community.document_loaders import TextLoader

loader = TextLoader("files/cricket.txt", encoding="utf-8")
docs = loader.load()

print(type(docs))

print(docs[0].page_content)

print(type(docs[0].metadata))



