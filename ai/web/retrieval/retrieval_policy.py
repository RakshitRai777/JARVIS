from dataclasses import dataclass

from ai.web.intent.search_intent import SearchIntent


@dataclass
class RetrievalConfig:

    max_pages: int

    top_chunks: int

    max_chunks_per_page: int


class RetrievalPolicy:
    """
    Decides how much information should be retrieved
    based on the user's intent.

    This makes Web RAG much faster while keeping
    answer quality high.
    """

    ###########################################################

    DEFAULT = RetrievalConfig(

        max_pages=5,

        top_chunks=5,

        max_chunks_per_page=10,

    )

    ###########################################################

    PERSON = RetrievalConfig(

        max_pages=3,

        top_chunks=5,

        max_chunks_per_page=8,

    )

    ###########################################################

    PROGRAMMING = RetrievalConfig(

        max_pages=4,

        top_chunks=6,

        max_chunks_per_page=10,

    )

    ###########################################################

    NEWS = RetrievalConfig(

        max_pages=8,

        top_chunks=8,

        max_chunks_per_page=6,

    )

    ###########################################################

    PRODUCT = RetrievalConfig(

        max_pages=6,

        top_chunks=7,

        max_chunks_per_page=8,

    )

    ###########################################################

    MEDICAL = RetrievalConfig(

        max_pages=6,

        top_chunks=7,

        max_chunks_per_page=8,

    )

    ###########################################################

    TABLE = {

        SearchIntent.PERSON: PERSON,

        SearchIntent.PROGRAMMING: PROGRAMMING,

        SearchIntent.NEWS: NEWS,

        SearchIntent.PRODUCT: PRODUCT,

        SearchIntent.MEDICAL: MEDICAL,

    }

    ###########################################################

    def get(

        self,

        intent: SearchIntent,

    ) -> RetrievalConfig:

        return self.TABLE.get(

            intent,

            self.DEFAULT,

        )