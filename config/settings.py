import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini Model
GEMINI_MODEL = "models/gemini-2.5-flash"

# App Settings
APP_TITLE = "AI Resume ATS Analyzer"
APP_ICON = "📄"
LAYOUT = "wide"

# File Upload Settings
ALLOWED_FILE_TYPES = ["pdf"]
MAX_FILE_SIZE_MB = 10