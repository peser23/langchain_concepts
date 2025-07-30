from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Google GenAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.6)

response = model.invoke("What is the capital of France?")

print(response.content)