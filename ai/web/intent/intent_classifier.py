import re

from ai.web.intent.search_intent import SearchIntent


class IntentClassifier:
    """
    Classifies the user's search intent.

    Responsibilities
    ----------------
    • Detect what the user is looking for
    • Help QueryExpander choose better searches

    Current Version
    ---------------
    Rule-based

    Future
    -------
    Small ML model
    LLM classifier
    """

    ############################################################

    def classify(
        self,
        query: str
    ) -> SearchIntent:

        query = query.lower().strip()

        ########################################################
        # NEWS
        ########################################################

        if any(word in query for word in [

            "latest",
            "today",
            "news",
            "recent",
            "breaking",
            "update",
            "updates"

        ]):

            return SearchIntent.NEWS

        ########################################################
        # PERSON
        ########################################################

        if re.search(

            r"\b(who|creator|inventor|founder|developed|created|made)\b",

            query

        ):

            return SearchIntent.PERSON

        ########################################################
        # SHOPPING
        ########################################################

        if any(word in query for word in [

            "buy",
            "price",
            "cheap",
            "best",
            "under",
            "cost",
            "deal"

        ]):

            return SearchIntent.SHOPPING

        ########################################################
        # PRODUCT
        ########################################################

        if any(word in query for word in [

            "review",
            "benchmark",
            "spec",
            "specification",
            "specifications",
            "vs",
            "comparison"

        ]):

            return SearchIntent.PRODUCT

        ########################################################
        # TUTORIAL
        ########################################################

        if any(word in query for word in [

            "tutorial",
            "guide",
            "learn",
            "course",
            "example",
            "documentation",
            "docs"

        ]):

            return SearchIntent.TUTORIAL

        ########################################################
        # MEDICAL
        ########################################################

        if any(word in query for word in [

            "symptom",
            "symptoms",
            "medicine",
            "disease",
            "treatment",
            "doctor",
            "health"

        ]):

            return SearchIntent.MEDICAL

        ########################################################
        # PROGRAMMING
        ########################################################

        if any(word in query for word in [

            "python",
            "java",
            "c++",
            "c#",
            "javascript",
            "programming",
            "algorithm",
            "coding",
            "code"

        ]):

            return SearchIntent.PROGRAMMING

        ########################################################
        # ENCYCLOPEDIA
        ########################################################

        if any(word in query for word in [

            "history",
            "meaning",
            "definition",
            "what is",
            "explain"

        ]):

            return SearchIntent.ENCYCLOPEDIA

        ########################################################
        # DEFAULT
        ########################################################

        return SearchIntent.GENERAL