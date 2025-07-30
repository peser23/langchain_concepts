from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

def main():
    # Example usage of the OpenAI model
    response = llm("What is the capital of France?")
    print(response) 

print("name:", __name__)
if __name__ == "__main__":
    main()
