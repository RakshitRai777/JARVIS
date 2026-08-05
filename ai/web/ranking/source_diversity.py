from collections import defaultdict


class SourceDiversity:
    """
    Ensures the final retrieved context is not dominated
    by a single website.

    Example

    Before

    Wikipedia
    Wikipedia
    Wikipedia
    Python.org
    Python.org

    After

    Wikipedia
    Python.org
    RealPython
    Docs
    """

    ############################################################

    def diversify(

        self,

        chunks,

        max_per_source: int = 1,

        top_k: int = 5,

    ):

        final = []

        counter = defaultdict(int)

        ########################################################

        for chunk in chunks:

            source = chunk.source

            if counter[source] >= max_per_source:

                continue

            final.append(chunk)

            counter[source] += 1

            if len(final) >= top_k:

                break

        ########################################################

        print(

            f"[SourceDiversity] "

            f"{len(chunks)} -> {len(final)} chunks"

        )

        return final