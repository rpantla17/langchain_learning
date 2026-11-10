import os
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Student(BaseModel):
    name: str = Field(
        description="Name of the student"
    )

    age: int | None = Field(
        default=None,
        description="Student age if explicitly provided"
    )

    technology: str | None = Field(
        default=None,
        description="Technology the student is learning"
    )

    experience: int | None = Field(
        default=None,
        description="Experience in years if explicitly provided"
    )

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)

structured_llm = llm.with_structured_output(
    Student,
    include_raw=True
)

text = input("Enter information: ")

prompt = f"""
Extract student information.

Rules:
1. Use only the supplied text.
2. Do not invent information.
3. If optional information is unavailable, use null.

Text:
{text}
"""

result = structured_llm.invoke(prompt)
if result["parsing_error"] is None and result['parsed'] is not None:
    student=result["parsed"]
    print("\nParsing Successful")

    print("\nName:")
    print(student.name)

    print("\nAge:")
    print(student.age)

    print("\nTechnology:")
    print(student.technology)

    print("\nExperience:")
    print(student.experience)

    print("\nDictionary:")
    print(student.model_dump())
else:
    print("\nParsing Failed")
    print(result["parsing_error"])
    print("\nRaw Model Response:")
    print(result["raw"])
