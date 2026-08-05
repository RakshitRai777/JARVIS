from ddgs import DDGS

from ai.web.search.search_provider import SearchProvider
from ai.web.web_result import WebResult
from ai.web.search.domain_filter import DomainFilter
from ai.web.search.domain_ranker import DomainRanker


class DuckDuckGoSearch(SearchProvider):
    """
    DuckDuckGo Search Provider

    Responsibilities
    ----------------
    • Search DuckDuckGo
    • Convert results into WebResult objects
    • Filter blocked domains
    • Rank trusted domains
    • Never return invalid results
    """

    ############################################################

    @property
    def name(self):

        return "DuckDuckGo"

    ############################################################

    def __init__(

        self,

        max_results: int = 8,

        region: str = "wt-wt",

        safesearch: str = "moderate",

    ):

        self.max_results = max_results

        self.region = region

        self.safesearch = safesearch

    ############################################################

    def search(

        self,

        query: str,

    ) -> list[WebResult]:

        print(f"[DuckDuckGo] Searching: {query}")

        results: list[WebResult] = []

        try:

            with DDGS() as ddgs:

                response = ddgs.text(

                    query,

                    max_results=self.max_results,

                    region=self.region,

                    safesearch=self.safesearch,

                )

                ####################################################
                # Convert results
                ####################################################

                for item in response:

                    url = (item.get("href") or "").strip()

                    title = (item.get("title") or "").strip()

                    snippet = (item.get("body") or "").strip()

                    ################################################
                    # Ignore invalid results
                    ################################################

                    if not url:
                        continue

                    if not url.startswith(("http://", "https://")):
                        continue

                    results.append(

                        WebResult(

                            success=True,

                            title=title,

                            url=url,

                            snippet=snippet,

                            source=self.name,

                        )

                    )

        except Exception as e:

            print(f"[DuckDuckGo] Search failed: {e}")

            return []

        ########################################################
        # Remove invalid entries
        ########################################################

        results = [

            r

            for r in results

            if r.success
            and r.url
            and r.url.startswith(("http://", "https://"))

        ]

        ########################################################
        # Filter domains
        ########################################################

        results = DomainFilter.filter_results(results)

        ########################################################
        # Rank domains
        ########################################################

        results = DomainRanker.rank(results)

        ########################################################
        # Debug
        ########################################################

        print()

        print("========== SEARCH RESULTS ==========")

        if not results:

            print("No valid search results.")

        else:

            for i, result in enumerate(results, start=1):

                print(f"{i}. {result.title}")

                print(f"   {result.url}")

                print()

        print("====================================")

        return results