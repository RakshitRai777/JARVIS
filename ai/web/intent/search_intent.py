from enum import Enum


class SearchIntent(Enum):
    """
    Types of web searches.

    The intent determines how the query
    should be expanded.
    """

    PERSON = "person"

    NEWS = "news"

    PRODUCT = "product"

    ENCYCLOPEDIA = "encyclopedia"

    TUTORIAL = "tutorial"

    SHOPPING = "shopping"

    MEDICAL = "medical"

    PROGRAMMING = "programming"

    GENERAL = "general"