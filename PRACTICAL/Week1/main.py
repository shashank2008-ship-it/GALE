from dotenv import load_dotenv
from google import genai
import os

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain machine learning in simple words"
)

print("\nLLM Response:")
print(response.text)