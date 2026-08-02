
import os
from dotenv import load_dotenv
from google import genai

# Load hidden environment variables
load_dotenv()

# Pass the key safely
client = genai.Client(api_key=os.getenv("GCP_API_KEY"))