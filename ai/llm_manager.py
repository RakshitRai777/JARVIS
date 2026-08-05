from ai.providers.groq_provider import GroqProvider


class LLMManager:
    """
    Central entry point for all LLM interactions.
    """

    ############################################################

    def __init__(self):

        self.provider = GroqProvider()

    ############################################################

    def generate(
        self,
        prompt: str,
    ) -> str:

        if not isinstance(prompt, str):

            raise TypeError("Prompt must be a string.")

        messages = [

            {

                "role": "user",

                "content": prompt,

            }

        ]

        return self.provider.generate(messages)