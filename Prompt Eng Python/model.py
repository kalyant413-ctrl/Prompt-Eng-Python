# Model
from google import genai
import os

# config API key
api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

# API Model
def gemini_model(prompt):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )
    return response.text