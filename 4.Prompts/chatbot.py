from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        print("Exiting the chatbot.")
        break
    model_response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=model_response.content))
    print(f"Chatbot: {model_response.content}")

print(f"Chat_history: {chat_history}")