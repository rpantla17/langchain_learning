import os
from langchain_openai import ChatOpenAI
api_key=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(
    api_key=api_key,
    model = "gpt-4o"
    )

question= input("enter your question:")

response=llm.invoke(question)
print(response.content)