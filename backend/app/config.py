import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GPT_API_KEY: str = os.getenv("GPT_API_KEY", "")
    MODEL_NAME: str = "gpt-4.1-mini"   # Use GPT free-tier or cheap-tier
    DEBUG: bool = True

settings = Settings()
