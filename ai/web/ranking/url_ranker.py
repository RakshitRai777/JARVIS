from urllib.parse import urlparse

from ai.web.web_result import WebResult


class URLRanker:
    """
    Scores search results BEFORE downloading them.

    This avoids downloading dozens of poor-quality pages.

    Score =
        Domain Authority
      + Query Match
      + Title Quality
    """

    TRUSTED = {

        "wikipedia.org": 100,

        "python.org": 98,

        "docs.python.org": 98,

        "developer.mozilla.org": 96,

        "learn.microsoft.com": 96,

        "oracle.com": 95,

        "docs.oracle.com": 95,

        "openai.com": 95,

        "anthropic.com": 95,

        "github.com": 92,

        "stackoverflow.com": 90,

        "reuters.com": 90,

        "bbc.com": 90,

        "techcrunch.com": 88,

        "arstechnica.com": 88,

        "wired.com": 86,

        "realpython.com": 86,

        "geeksforgeeks.org": 84,

        "tutorialspoint.com": 80,

        "baeldung.com": 80,

    }

    ############################################################

    def _domain_score(self, url: str):

        domain = urlparse(url).netloc.lower()

        for trusted, score in self.TRUSTED.items():

            if trusted in domain:
                return score

        return 40

    ############################################################

    def _title_score(
        self,
        title: str,
        query: str
    ):

        title = title.lower()

        words = query.lower().split()

        score = 0

        for word in words:

            if word in title:
                score += 5

        return score

    ############################################################

    def rank(
        self,
        query: str,
        results: list[WebResult]
    ) -> list[WebResult]:

        for result in results:

            score = 0

            score += self._domain_score(result.url)

            score += self._title_score(
                result.title,
                query
            )

            result.rank_score = score

        results.sort(

            key=lambda r: getattr(r, "rank_score", 0),

            reverse=True

        )

        return results