import re


class SentenceSplitter:
    """
    Splits text into sentences.

    Keeps punctuation attached to the sentence.
    """

    ##########################################################

    def split(
        self,
        text: str,
    ) -> list[str]:

        if not text.strip():
            return []

        ######################################################
        # Split after . ! ?
        ######################################################

        sentences = re.split(

            r"(?<=[.!?])\s+",

            text.strip()

        )

        ######################################################

        return [

            s.strip()

            for s in sentences

            if s.strip()

        ]