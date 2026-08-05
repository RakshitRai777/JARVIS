from abc import ABC, abstractmethod

from ai.web.web_result import WebResult


class SearchProvider(ABC):
    """
    Base interface for every web search provider.

    DuckDuckGo
    Brave
    Tavily
    Google
    Bing
    etc.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def search(
        self,
        query: str,
    ) -> list[WebResult]:
        ...