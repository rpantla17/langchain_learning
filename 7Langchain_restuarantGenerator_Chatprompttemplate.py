import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY
)
template=ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert restaurant naming consultant
        and creative branding specialist.

        Generate 5 unique, catchy, memorable restaurant
        names based on the user's requirements.

        Rules:
        1. Make names relevant to the cuisine, location,
           restaurant theme, and target audience.
        2. Keep names easy to pronounce and remember.
        3. Explain the inspiration behind each name.
        4. Recommend the best name and explain why.
        5. Suggest 3 signature dishes for the recommended
           restaurant.
        6. Do not claim legal or domain availability.
        7. Use a clear, structured format.
        """
    ),
    (
        "human",
        """
        Generate restaurant name ideas using these details:

        Cuisine Type: {cuisine_type}
        Location: {location}
        Restaurant Theme: {restaurant_theme}
        Target Audience: {target_audience}

        Provide 5 names with explanations, recommend the
        best name, and suggest 3 signature dishes.
        """
    )
])
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