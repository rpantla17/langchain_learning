from langchain_openai import ChatOpenAI
import os
from pydantic import BaseModel, Field
from typing import Literal
class SupportTicket(BaseModel):
    #category,priority,severity
    category: Literal[
        "billing",
        "technical",
        "account",
        "other"
    ] = Field(
        description="Main category of the customer issue"
    )
    priority: Literal[
        "low",
        "medium",
        "high"
    ]= Field(
description="Priority level of the issue"
)
    severity:int =Field(
    ge=1,
    le=5,
    description="severity from 1 to 5"
)
    summary:str = Field(
    description="Very short summary about customer issue"
)
llm = ChatOpenAI(
model="gpt-5.6-luna",
api_key=os.getenv("OPENAI_API_KEY")
)
structured_llm = llm.with_structured_output(
    SupportTicket
    )
text = input(
"Enter customer issue: "
)
result = structured_llm.invoke(text)
print("\nSUPPORT TICKET")
print("------------------")
print("Category :", result.category)
print("Priority :", result.priority)
print("Severity :", result.severity)
print("Summary :", result.summary)


 
