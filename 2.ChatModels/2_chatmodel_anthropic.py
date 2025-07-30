from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Anthropic model
model = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.5)

response = model.invoke("What is the capital of France?")

print(response.content)