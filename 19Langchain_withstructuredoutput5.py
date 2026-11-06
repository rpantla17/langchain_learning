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
structured_llm = llm.with_structured_output(Person)
text = input(
 "Enter information about a person: "
)
result = structured_llm.invoke(text)
print("\n--------------------------------")
print("COMPLETE PYDANTIC OBJECT")
print("--------------------------------")
print(result)
print("\n--------------------------------")
print("OBJECT TYPE")
print("--------------------------------")
print(type(result))
print("\n--------------------------------")
print("INDIVIDUAL FIELDS")
print("--------------------------------")
print("Name :", result.name)
print("Profession :", result.profession)
print("Experience :", result.experience)
print("Skills :", result.skills)
print("\n--------------------------------")
print("PYTHON DICTIONARY")
print("--------------------------------")
print(result.model_dump())
print("\n--------------------------------")
print("JSON STRING")
print("--------------------------------")
print(result.model_dump_json())




