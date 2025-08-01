from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI()

#1st prompt
template1 = PromptTemplate(
    template="write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

#2nd prompt
template2 = PromptTemplate(
    template="Generate a 5 pointer summary on the following text. \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({
    'topic': 'football in texas'
})

print(result)