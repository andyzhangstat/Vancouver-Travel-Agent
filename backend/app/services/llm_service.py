from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.GPT_API_KEY)

def call_gpt(prompt: str):
    """
    Call GPT model and return the assistant's reply as string.
    """
    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
