from enum import Enum


class QuestionPattern(Enum):
    """
    Represents the type of question being asked.

    This is separate from SearchIntent.

    Example:

        Intent      = PERSON

        Pattern     = CREATOR

        Expansion   = creator / inventor / history
    """

    GENERAL = "general"

    ####################################################
    # People
    ####################################################

    CREATOR = "creator"

    INVENTOR = "inventor"

    FOUNDER = "founder"

    CEO = "ceo"

    AUTHOR = "author"

    BIOGRAPHY = "biography"

    BIRTH = "birth"

    DEATH = "death"

    ####################################################
    # Technology
    ####################################################

    RELEASE = "release"

    DOCUMENTATION = "documentation"

    TUTORIAL = "tutorial"

    INSTALLATION = "installation"

    ####################################################
    # Products
    ####################################################

    REVIEW = "review"

    PRICE = "price"

    COMPARISON = "comparison"

    SPECIFICATIONS = "specifications"

    ####################################################
    # News
    ####################################################

    LATEST_NEWS = "latest_news"

    UPDATES = "updates"

    ####################################################
    # Medical
    ####################################################

    SYMPTOMS = "symptoms"

    TREATMENT = "treatment"

    CAUSES = "causes"