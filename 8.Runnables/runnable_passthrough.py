from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI(temperature=1.5)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a joke abount {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explaing the folloiwng joke - {text}",
    input_variables=["text"]
)

joke_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = chain.invoke({'topic': 'python programming'})

print("Joke:", result['joke'])
print("Explanation:", result['explanation'])