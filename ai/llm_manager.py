from ai.providers.groq_provider import GroqProvider


class LLMManager:

    def __init__(self):

        self.provider = GroqProvider()

    def generate(self, messages):

        return self.provider.generate(messages)