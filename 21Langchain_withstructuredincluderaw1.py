import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
class Person(BaseModel):
 name: str = Field(
 description="Name of the person"
 )
 profession: str = Field(
 description="Profession of the person"
 )
 experience: int | None = Field(
 default=None,
 description="Number of years of professional experience"
 )
 skills: list[str] = Field(
 description="Important professional skills"
 )
llm = ChatOpenAI(
 model="gpt-5.6",
 api_key=os.getenv("OPENAI_API_KEY")
)
structured_llm= llm.with_structured_output(Person,include_raw=True)
result=structured_llm.invoke("Viswa ia sre engineer and he has 20 years experience and he has skills aws and python")
print("\nResult Type:",type(result))
print(result)
print("\n------RAW----")
print(result['raw'])
print("\n----PARSED----")
print(result['parsed'])
print("\n----PARSING ERROR-----")
print(result['parsing_error'])
