import os
from pydantic import BaseModel,ValidationError,Field
class Book(BaseModel):
    title:str = Field(
        description = "Title Of The Book"
    )
    author:str = Field(
        description = "Author Of The Book"   )
    category:str  = Field(
        description = "Category or genre of the book"
    )
from langchain_openai import ChatOpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
    )
structured_llm = llm.with_structured_output(Book)
result = structured_llm.invoke("Give Information about Atomic Habits")
print("\nProduct Object")
print(result)
print("------------------")
print("Title....",result.title)
print("category....",result.category)
print("Author:",result.author)
