from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
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
    template="write a 5 line summary on the following text. \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({
    'topic': "Black hole"
})

print(result)