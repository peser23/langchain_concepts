from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI embeddings
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is a famous Indian cricketer known for his aggressive batting and leadership.",
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",   
    "Rohit Sharma is known for his explosive batting style.",
    "MS Dhoni is a former Indian cricket captain famous for his calm demeanor and finishing skills."   
]

query="Tell me about MS Dhoni"

# Embed the documents
doc_emneddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity between the query and each document   
scores = cosine_similarity([query_embedding], doc_emneddings)[0]

enumerated_docs = list(enumerate(scores))

index, score = sorted(enumerated_docs, key=lambda x: x[1])[-1]

print("query:", query)
print("Most similar document:", documents[index])
print("Score:", score)


