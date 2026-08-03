from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def generate(self, messages: list) -> str:
        """
        Generate a response from the provider.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass