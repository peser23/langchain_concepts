from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch


load_dotenv()

model = ChatOpenAI(temperature=1.5)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following report - {text}",
    input_variables=["text"]
)

report_generation_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    )

chain = RunnableSequence(report_generation_chain, branch_chain)

result = chain.invoke({'topic': 'GPT-5'})  

print(result)