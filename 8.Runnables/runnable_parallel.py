from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI(temperature=1.5)

prompt1 = PromptTemplate(
    template="Generate a funny tweet about topic - {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a funny linkedin post about topic - {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin_post": RunnableSequence(prompt2, model, parser)   
})

result = chain.invoke({'topic': 'AI in 2025'})

print("Tweet:", result['tweet'])
print("LinkedIn Post:", result['linkedin_post'])


