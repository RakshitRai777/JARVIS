import requests

from config.settings import settings
from ai.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        })

    @property
    def name(self):

        return "Groq"

    def generate(self, messages):

        payload = {
            "model": settings.MODEL_NAME,
            "messages": messages,
            "temperature": 0.4
        }

        response = self.session.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]