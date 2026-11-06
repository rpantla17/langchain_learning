import os
from pydantic import BaseModel,ValidationError,Field
class Employee(BaseModel):
    name:str = Field(
        description = "Name Of the  Employee"
    )
    technology:str = Field(
        description = "Primary Technology of the employee"
    )
    experience:int  = Field(
        description = "Years of experience of the employee"
    )
from langchain_openai import ChatOpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
    )
structured_llm = llm.with_structured_output(Employee)
text = input("enter employee information:\n")
employee=structured_llm.invoke(text)
print("\nEmployee Details")
print("------------------")
print("Name....",employee.name)
print("Technology....",employee.technology)
print("Experience:",employee.experience)
