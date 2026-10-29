import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
llm = ChatOpenAI(
model="gpt-4o-mini",
api_key=os.getenv("OPENAI_API_KEY")
)
template = ChatPromptTemplate.from_messages(
[
(
"system",
"You are an experienced technical interviewer."
),
(
"human",
"""
Generate {count} {difficulty} interview questions
for a {level} candidate
on {technology}.
For every question:
- Give the question
- Give a simple answer
- Give one small example
"""
)
]
)
technology = input("Enter technology: ")
level = input("Enter candidate level: ")
count = input("Enter number of questions: ")
difficulty = input("Enter difficulty: ")
prompt = template.invoke(
{
"technology": technology,
"level": level,
"count": count,
"difficulty": difficulty
}
)
response = llm.invoke(prompt)
print("\nInterview Preparation:")
print(response.content)