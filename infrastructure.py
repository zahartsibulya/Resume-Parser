# infrastructure.py
import json
from groq import Groq
from dotenv import load_dotenv
from domain import SYSTEM_PROMPT

load_dotenv()

client = Groq()

def parse_cv(text: str) -> dict:
    """Парсить текст резюме через LLM та повертає DTO кандидата"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.1
    )
    return json.loads(response.choices[0].message.content)
