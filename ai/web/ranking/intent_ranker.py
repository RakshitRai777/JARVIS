from ai.web.intent.search_intent import SearchIntent
from ai.web.web_result import WebResult


class IntentRanker:
    """
    Applies intent-specific boosts to search results.

    This works AFTER URLRanker.

    Different search intents prefer different domains.
    """

    ############################################################

    PERSON = {

        "wikipedia.org": 30,
        "britannica.com": 28,
        "biography.com": 25,
        "ieee.org": 20,

    }

    ############################################################

    PROGRAMMING = {

        "python.org": 30,
        "docs.python.org": 30,

        "developer.mozilla.org": 28,

        "learn.microsoft.com": 28,

        "oracle.com": 28,
        "docs.oracle.com": 28,

        "github.com": 22,

        "stackoverflow.com": 20,

        "realpython.com": 18,

        "geeksforgeeks.org": 16,

    }

    ############################################################

    NEWS = {

        "reuters.com": 35,

        "apnews.com": 34,

        "bbc.com": 32,

        "techcrunch.com": 30,

        "theverge.com": 28,

        "wired.com": 28,

        "arstechnica.com": 28,

        "openai.com": 26,

        "anthropic.com": 26,

        "google.com": 24,

    }

    ############################################################

    PRODUCT = {

        "amazon.com": 25,

        "bestbuy.com": 24,

        "newegg.com": 24,

        "rtings.com": 30,

        "tomshardware.com": 28,

        "notebookcheck.net": 28,

    }

    ############################################################

    MEDICAL = {

        "nih.gov": 35,

        "who.int": 34,

        "mayoclinic.org": 33,

        "cdc.gov": 32,

        "nhs.uk": 30,

    }

    ############################################################

    TABLE = {

        SearchIntent.PERSON: PERSON,

        SearchIntent.PROGRAMMING: PROGRAMMING,

        SearchIntent.NEWS: NEWS,

        SearchIntent.PRODUCT: PRODUCT,

        SearchIntent.MEDICAL: MEDICAL,

    }

    ############################################################

    def rank(

        self,

        intent: SearchIntent,

        results: list[WebResult]

    ) -> list[WebResult]:

        boosts = self.TABLE.get(intent)

        if boosts is None:

            return results

        for result in results:

            url = result.url.lower()

            boost = 0

            for domain, score in boosts.items():

                if domain in url:

                    boost = score

                    break

            result.rank_score += boost

        results.sort(

            key=lambda r: r.rank_score,

            reverse=True

        )

        return results