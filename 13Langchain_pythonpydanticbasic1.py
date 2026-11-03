from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age: int
    course: str

student=Student(name = "Ravi",age=44,course="Java")
print(student)
