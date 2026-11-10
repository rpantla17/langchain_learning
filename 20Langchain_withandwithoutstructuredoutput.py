
import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class Student(BaseModel):
    name:str 
    age:int
    course:str  
llm = ChatOpenAI(
 model="gpt-4o",
 api_key=os.getenv("OPENAI_API_KEY")
)
structured_llm = llm.with_structured_output(Student)

normal_result = llm.invoke(
    "Explain Python in One sentence"
)
strcutured_result = structured_llm.invoke(
    "Ravi is 25 years old and learning python"
)
print("Normal Result Type:")
print(type(normal_result))
print("\n Normal result:")
print(normal_result.content)
print("\nStructured Result Type")
print(type(strcutured_result))
print("\n Structures Result:")
print(strcutured_result)