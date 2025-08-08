from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="write a joke abount {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI(temperature=1.5)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explaing the folloiwng joke - {text}",
    input_variables=["text"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({'topic': 'python programming'})

print(result)