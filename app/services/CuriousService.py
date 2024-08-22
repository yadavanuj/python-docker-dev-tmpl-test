import google.generativeai as genai
from app.config import settings


genai.configure(api_key=str(settings.GEMINI_KEY))
model = genai.GenerativeModel('gemini-1.5-flash')

async def ask(que: str) -> str:
    return model.generate_content(que).text

