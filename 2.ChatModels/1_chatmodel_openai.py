from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(model="gpt-4")

response = model.invoke("What is the capital of France?")

print(response.content)