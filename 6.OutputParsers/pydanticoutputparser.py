from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(temperature=1.5)

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Provide the name, age, and city of a fictional {place} person. \n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"place": "Indian"})
#print(prompt)
result = model.invoke(prompt)
parsed_result = parser.parse(result.content)
print(parsed_result)


