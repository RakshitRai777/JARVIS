from urllib.parse import urlparse


class DomainFilter:
    """
    Filters and deduplicates search results.
    """

    BLOCKED_DOMAINS = {

        "linkedin.",
        "facebook.",
        "instagram.",
        "twitter.",
        "x.com",
        "reddit.",
        "quora.",
        "brainly.",
        "quizlet.",
        "medium.",
        "pinterest.",
        "tiktok.",

    }

    ##########################################################

    @classmethod
    def is_blocked(cls, url: str) -> bool:

        domain = urlparse(url).netloc.lower()

        return any(

            blocked in domain

            for blocked in cls.BLOCKED_DOMAINS

        )

    ##########################################################

    @classmethod
    def filter_results(cls, results):

        filtered = []

        seen = set()

        for result in results:

            if cls.is_blocked(result.url):
                continue

            if result.url in seen:
                continue

            seen.add(result.url)

            filtered.append(result)

        return filtered