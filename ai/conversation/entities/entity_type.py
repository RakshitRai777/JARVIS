from enum import Enum


class EntityType(Enum):
    PERSON = "person"

    ORGANIZATION = "organization"

    COMPANY = "company"

    PRODUCT = "product"

    PROGRAMMING_LANGUAGE = "programming_language"

    COUNTRY = "country"

    CITY = "city"

    PLACE = "place"

    BOOK = "book"

    MOVIE = "movie"

    EVENT = "event"

    UNKNOWN = "unknown"