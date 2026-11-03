import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)
parser=StrOutputParser()

template =ChatPromptTemplate.from_messages(
    [
    ('system','You are helpful {subject} teacher,Explain Everything in simple english '),
    ('human',"Explain {topic} with an example"),
    ]
)
# print(type(template))
# print(template)

subject = input("enter the subject:\n")
topic=input("enter the topic:\n")
# print(template.input_variables)
prompt= template.invoke(
    {
        "subject" : subject,
        "topic" : topic   }
)
response = llm.invoke(prompt)
result = parser.invoke(response)
print(result)
print(type(result))




