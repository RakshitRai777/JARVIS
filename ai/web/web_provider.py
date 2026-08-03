from abc import ABC
from abc import abstractmethod

from ai.web.web_result import WebResult


class WebProvider(ABC):
    """
    Base interface for all web providers.

    Examples:
    - DuckDuckGo
    - Google
    - Brave
    - Bing
    """

    @abstractmethod
    def search(self, query: str) -> list[WebResult]:
        """
        Search the web.

        Returns a list of WebResult objects.
        """
        pass