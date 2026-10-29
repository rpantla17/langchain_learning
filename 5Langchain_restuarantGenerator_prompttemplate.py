import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
)
template = PromptTemplate.from_template(
  """
   You are a creative restaurant branding expert with a deep understanding of food culture, cuisine, and business naming.

Your task is to suggest a unique, memorable, and catchy restaurant name based on the following inputs:

Cuisine Type: {cuisine_type}
Restaurant Location: {location}
Restaurant Theme: {restaurant_theme}
Target Audience: {target_audience}
Instructions:

Generate 5 creative restaurant name suggestions.
Make each name relevant to the specified cuisine, theme, and target audience.
Keep the names short, memorable, and easy to pronounce.
Provide a brief explanation of why each name suits the restaurant.
Suggest 3 signature dishes for the best name.
Recommend the single best restaurant name and explain why it stands out.
Avoid generic or overly common names.
Format your response clearly using headings and numbered lists.

Remember: These are creative suggestions. Do not claim that a name is legally available or that its domain name is available.

  """
 )
cuisine_type = input("Enter Cuisine Type:")
location= input("Enter location:")
restaurant_theme = input("Enter Restuarant Theme:")
target_audience = input("enter the type of target audience")
prompt = template.invoke(
 {
  "cuisine_type" : cuisine_type,
  "location" : location,
  "restaurant_theme" : restaurant_theme,
  "target_audience" : target_audience

 }
)
response=llm.invoke(prompt)
print("\nRestuarant Name suggestions")
print(response.content)