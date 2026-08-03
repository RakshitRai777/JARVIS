from ddgs import DDGS

from ai.web.web_result import WebResult


class DuckDuckGoSearch:
    """
    Performs web searches using DuckDuckGo.

    This class only searches.

    It does NOT download webpages.
    """

    def __init__(
        self,
        max_results: int = 5,
        region: str = "wt-wt",
        safesearch: str = "moderate"
    ):

        self.max_results = max_results
        self.region = region
        self.safesearch = safesearch

    ##########################################################

    def search(
        self,
        query: str
    ) -> list[WebResult]:

        results = []

        try:

            with DDGS() as ddgs:

                response = ddgs.text(
                    query,
                    max_results=self.max_results,
                    region=self.region,
                    safesearch=self.safesearch
                )

                for item in response:

                    results.append(

                        WebResult(

                            success=True,

                            title=item.get("title", ""),

                            url=item.get("href", ""),

                            snippet=item.get("body", ""),

                            source="DuckDuckGo"

                        )

                    )

        except Exception as e:

            results.append(

                WebResult(

                    success=False,

                    error=str(e),

                    source="DuckDuckGo"

                )

            )

        return results