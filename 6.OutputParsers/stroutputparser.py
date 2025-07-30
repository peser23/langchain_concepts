from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

#1st prompt
template1 = PromptTemplate(
    template="write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)
prompt1 = template1.invoke({"topic": "Black hole" })
result1 = model.invoke(prompt1)

#2nd prompt
template2 = PromptTemplate(
    template="write a 5 line summary on the following text. \n {text}",
    input_variables=["text"]
)
prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print(result2.content)

