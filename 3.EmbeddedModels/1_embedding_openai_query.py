from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_query("Paris is the capital of France.")

print(str(result))



