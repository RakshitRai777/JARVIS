from ai.web.query_expander.query_expander import QueryExpander
from ai.web.ranking.url_ranker import URLRanker
from ai.web.search.domain_filter import DomainFilter
from ai.web.search.domain_ranker import DomainRanker
from ai.web.search.duckduckgo_search import DuckDuckGoSearch
from ai.web.search_cache.search_cache import SearchCache
from ai.web.intent.intent_classifier import IntentClassifier
from ai.web.ranking.intent_ranker import IntentRanker

class SearchManager:
    """
    Production Search Manager.

    Pipeline
    --------
    Query
        ↓
    Query Expansion
        ↓
    Search
        ↓
    Merge
        ↓
    Remove Duplicates
        ↓
    Domain Filter
        ↓
    URL Ranking
        ↓
    Domain Ranking
        ↓
    Cache
    """

    ##########################################################

    MAX_RESULTS = 8

    ##########################################################

    def __init__(self):

        self.provider = DuckDuckGoSearch()

        self.cache = SearchCache()

        self.expander = QueryExpander()

        self.url_ranker = URLRanker()

        self.intent_classifier = IntentClassifier()

        self.intent_ranker = IntentRanker()

    ##########################################################

    @property
    def provider_name(self):

        return self.provider.name

    ##########################################################

    def search(self, query: str):

        ######################################################
        # Cache
        ######################################################

        cached = self.cache.load(query)

        if cached is not None:

            print(
                f"[SearchManager] Returning "
                f"{len(cached.results)} cached search results."
            )

            return cached.results

        ######################################################
        # Expand Query
        ######################################################

        expanded = self.expander.expand(query)


        ######################################################
        # Detect Intent
        ######################################################

        intent = self.intent_classifier.classify(query)

        print()

        print(f"[Intent] {intent.value}")

        print()
        print("========== QUERY EXPANSION ==========")

        for q in expanded.queries:
            print("-", q)

        print("=====================================")

        ######################################################
        # Search
        ######################################################

        all_results = []

        seen = set()

        for q in expanded.queries:

            print()

            print(f"[SearchManager] Searching: {q}")

            results = self.provider.search(q)

            for result in results:

                if not result.success:
                    continue

                url = result.url.lower()

                if url in seen:
                    continue

                seen.add(url)

                all_results.append(result)

        ######################################################
        # Filter
        ######################################################

        all_results = DomainFilter.filter_results(
            all_results
        )

        ######################################################
        # URL Ranking 
        ######################################################

        all_results = self.url_ranker.rank(
            query=query,
            results=all_results
        )

        ######################################################
        # Intent Ranking
        ######################################################

        all_results = self.intent_ranker.rank(
            intent=intent,
            results=all_results
        )

        ######################################################
        # Domain Ranking
        ######################################################

        all_results = DomainRanker.rank(
            all_results
        )

        ######################################################
        # Keep only best URLs
        ######################################################

        all_results = all_results[:self.MAX_RESULTS]

        ######################################################
        # Debug
        ######################################################

        print()
        print("========== URL RANKING ==========")

        for i, result in enumerate(all_results, 1):

            print(
                f"{i}. "
                f"{result.title} "
                f"({getattr(result, 'rank_score', 0)})"
            )

        print("=================================")

        ######################################################
        # Cache
        ######################################################

        self.cache.save(
            query=query,
            results=all_results
        )

        return all_results