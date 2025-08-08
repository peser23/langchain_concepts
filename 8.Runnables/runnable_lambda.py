from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def count_joke_words(text):
    return len(text.split())

model = ChatOpenAI(temperature=1.5)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a joke abount {topic}",
    input_variables=["topic"]
)

joke_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(count_joke_words)  
})

chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = chain.invoke({'topic': 'AI in 2025'})

print("Joke:", result['joke'])
print("Word Count:", result['word_count'])