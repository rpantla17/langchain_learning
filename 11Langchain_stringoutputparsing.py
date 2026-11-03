import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
llm=ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
parser=StrOutputParser()
response=llm.invoke('what is python ?.. explain in one sentense')
output=parser.invoke(response)
print(output)
print(type(output))
print(response.content)
print(type(response))
