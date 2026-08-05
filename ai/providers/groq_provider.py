import requests

from config.settings import settings
from ai.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):
    """
    Groq provider using the OpenAI-compatible API.
    """

    ############################################################

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(

            {

                "Authorization": f"Bearer {settings.GROQ_API_KEY}",

                "Content-Type": "application/json",

            }

        )

    ############################################################

    @property
    def name(self):

        return "Groq"

    ############################################################

    def generate(
        self,
        messages: list,
    ) -> str:

        payload = {

            "model": settings.MODEL_NAME,

            "messages": messages,

            "temperature": 0.4,

        }

        response = self.session.post(

            "https://api.groq.com/openai/v1/chat/completions",

            json=payload,

            timeout=60,

        )

        ########################################################

        if not response.ok:

            raise RuntimeError(

                f"\nGroq API Error ({response.status_code})\n\n"

                f"{response.text}"

            )

        ########################################################

        data = response.json()

        ########################################################

        if "choices" not in data:

            raise RuntimeError(

                f"\nUnexpected Groq Response\n\n"

                f"{data}"

            )

        ########################################################

        return data["choices"][0]["message"]["content"]