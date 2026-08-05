import re

from ai.memory.intent.memory_intent import MemoryIntent


class MemoryIntentClassifier:
    """
    Determines what kind of memory operation the user wants.

    STORE
        Remember my birthday.

    RECALL
        What is my birthday?

    UPDATE
        Change my birthday.

    DELETE
        Forget my birthday.
    """

    ############################################################

    STORE_PREFIXES = [

        "remember",

        "remember that",

        "save",

        "store",

        "note that",

        "keep in mind",

    ]

    ############################################################

    RECALL_PREFIXES = [

        "what is my",

        "what's my",

        "who am i",

        "where do i",

        "when is my",

        "do you remember",

        "tell me my",

        "recall",

    ]

    ############################################################

    UPDATE_PREFIXES = [

        "change my",

        "update my",

        "replace my",

        "correct my",

    ]

    ############################################################

    DELETE_PREFIXES = [

        "forget",

        "delete my",

        "remove my",

        "erase my",

    ]

    ############################################################

    def classify(
        self,
        message: str,
    ) -> MemoryIntent:

        text = message.lower().strip()

        ########################################################

        if any(
            text.startswith(prefix)
            for prefix in self.STORE_PREFIXES
        ):
            return MemoryIntent.STORE

        ########################################################

        if any(
            text.startswith(prefix)
            for prefix in self.RECALL_PREFIXES
        ):
            return MemoryIntent.RECALL

        ########################################################

        if any(
            text.startswith(prefix)
            for prefix in self.UPDATE_PREFIXES
        ):
            return MemoryIntent.UPDATE

        ########################################################

        if any(
            text.startswith(prefix)
            for prefix in self.DELETE_PREFIXES
        ):
            return MemoryIntent.DELETE

        ########################################################

        return MemoryIntent.UNKNOWN