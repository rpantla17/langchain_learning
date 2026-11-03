import os
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
response = llm.invoke("What is Python?,Explain in One Sentense")
print(type(response))
print(response)
print("Input tokens is",response.usage_metadata['input_tokens'])
print("Output tokens is",response.usage_metadata['output_tokens'])
print('total tokens is',response.usage_metadata['total_tokens'])
print("model is",response.response_metadata['model_name'])


