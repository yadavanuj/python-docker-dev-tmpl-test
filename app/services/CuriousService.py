from google import genai
from app.config import settings

# Configure the genai client with the API key
client = genai.Client(api_key=str(settings.GEMINI_KEY))

async def ask(que: str) -> str:
    response = await client.aio.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=que
    )
    return response.text or ''

