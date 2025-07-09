import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found. Please check your .env file.")

# Configure the API key
genai.configure(api_key=api_key)

# Use a valid model name (try 'gemini-1.5-flash' to avoid hitting quota too fast)
model = genai.GenerativeModel('gemini-1.5-flash')

# Make a request
response = model.generate_content("Explain quantum computing in simple terms.")
print(response.text)


