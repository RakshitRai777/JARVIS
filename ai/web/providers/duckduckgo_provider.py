from ai.web.search.duckduckgo_search import DuckDuckGoSearch
from ai.web.web_provider import WebProvider
from ai.web.web_result import WebResult


class DuckDuckGoProvider(WebProvider):
    """
    DuckDuckGo implementation of WebProvider.
    """

    def __init__(self):

        self.search_engine = DuckDuckGoSearch()

    ##########################################################

    def search(
        self,
        query: str
    ) -> list[WebResult]:

        return self.search_engine.search(query)