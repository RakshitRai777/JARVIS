from urllib.parse import urlparse


class DomainRanker:
    """
    Assigns priority to search results.

    Higher priority sources are downloaded first.
    """

    ############################################################

    TIER_1 = {

        "python.org",
        "docs.python.org",

    }

    TIER_2 = {

        "wikipedia.org",

    }

    TIER_3 = {

        "developer.mozilla.org",

        "learn.microsoft.com",

        "github.com",

    }

    TIER_4 = {

        "realpython.com",

        "geeksforgeeks.org",

        "pythoninstitute.org",

        "computerhistory.org",

        "edu",

        "gov",

    }

    ############################################################

    @classmethod
    def priority(cls, url: str):

        domain = urlparse(url).netloc.lower()

        for d in cls.TIER_1:
            if d in domain:
                return 100

        for d in cls.TIER_2:
            if d in domain:
                return 90

        for d in cls.TIER_3:
            if d in domain:
                return 80

        for d in cls.TIER_4:
            if d in domain:
                return 70

        return 20

    ############################################################

    @classmethod
    def rank(cls, results):

        return sorted(

            results,

            key=lambda r: cls.priority(r.url),

            reverse=True

        )