import os
from pydantic import BaseModel,ValidationError,Field
class Product(BaseModel):
    name:str = Field(
        description = "Name Of the  Product"
    )
    category:str = Field(
        description = "Product category"   )
    price:int  = Field(
        description = "Price Of the Product"
    )
from langchain_openai import ChatOpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
    )

## create a model wrapper  that should return output matching Student schema 
structred_llm = llm.with_structured_output(Product)
text = input("Enter product information:")
product = structred_llm.invoke(text)
print("\nProduct Object")
print(product)
print("------------------")
print("Name....",product.name)
print("category....",product.category)
print("price:",product.price)
print("\n As Dictionary")
print(product.model_dump())
print("\n As json")
print(product.model_dump_json())
