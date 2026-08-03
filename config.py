import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "Gemini API key not found! Please check your .env file."
    )

# Create Gemini Client
client = genai.Client(api_key=API_KEY)

# Model
MODEL_NAME = "gemini-3.5-flash"