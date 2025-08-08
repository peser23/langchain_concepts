from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Load all PDF files from a directory
loader = DirectoryLoader("files", glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()

print(f"Number of documents loaded: {len(docs)}")