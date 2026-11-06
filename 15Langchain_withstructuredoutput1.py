import os
from pydantic import BaseModel,ValidationError,Field
from langchain_openai import ChatOpenAI
class Student(BaseModel):
    name:str 
    age:int 
    course:str 
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-5.6",
    api_key=OPENAI_API_KEY
    )
## create a model wrapper that matches return output matching student schema 
structured_llm=llm.with_structured_output(Student)

text = input("Enter student information")

result = structured_llm.invoke(text)
#print(type(result))
print("\n Completes result")
print(result)
print(result.name)
print(result.age)
print(result.course)



