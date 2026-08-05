import re
from urllib.parse import urlparse

from ai.conversation.entity_extraction.entity_extractor import EntityExtractor
from ai.embeddings.embedding_model import EmbeddingModel
from ai.embeddings.similarity import cosine_similarity
from ai.web.ranking.chunk_scorer import ChunkScore
from ai.web.ranking.entity_matcher import EntityMatcher


class HybridRanker:
    """
    Production-quality Hybrid Ranker.

    Ranking Factors
    ---------------
    • Semantic Similarity
    • Keyword Overlap
    • Entity Match
    • Title Relevance
    • Domain Authority
    • Freshness (future)
    """

    ############################################################

    TRUSTED_DOMAINS = {

        "python.org": 1.00,
        "docs.python.org": 1.00,

        "wikipedia.org": 0.98,

        "developer.mozilla.org": 0.95,

        "learn.microsoft.com": 0.95,

        "github.com": 0.90,

        "stackoverflow.com": 0.88,

        "realpython.com": 0.85,

        "geeksforgeeks.org": 0.82,

        "pythoninstitute.org": 0.80,

    }

    ############################################################

    def __init__(self):

        self.entity_extractor = EntityExtractor()

        self.entity_matcher = EntityMatcher()

    ############################################################

    def tokenize(self, text: str):

        return set(

            re.findall(

                r"[a-zA-Z0-9_]+",

                text.lower()

            )

        )

    ############################################################

    def domain_score(self, url: str):

        domain = urlparse(url).netloc.lower()

        for trusted, score in self.TRUSTED_DOMAINS.items():

            if trusted in domain:

                return score

        return 0.30

    ############################################################

    def rank(

        self,

        question: str,

        chunks,

        top_results: int = 5,

    ):

        ########################################################

        if not chunks:

            return []

        ########################################################
        # Embed chunks
        ########################################################

        EmbeddingModel.embed_chunks(chunks)

        ########################################################
        # Embed question
        ########################################################

        question_vector = EmbeddingModel.encode(question)

        question_words = self.tokenize(question)

        ########################################################
        # Extract query entities ONCE
        ########################################################

        extraction = self.entity_extractor.extract(question)

        query_entities = extraction.entities

        ########################################################
        # Score every chunk
        ########################################################

        for chunk in chunks:

            ####################################################
            # Semantic
            ####################################################

            semantic = cosine_similarity(

                question_vector,

                chunk.embedding

            )

            ####################################################
            # Keyword
            ####################################################

            body_words = self.tokenize(chunk.text)

            keyword_overlap = len(

                question_words & body_words

            )

            keyword_score = keyword_overlap / max(

                len(question_words),

                1

            )

            ####################################################
            # Entity
            ####################################################

            entity_score = self.entity_matcher.score(

                query_entities,

                chunk.text,

            )

            ####################################################
            # Title
            ####################################################

            title_words = self.tokenize(chunk.title)

            title_overlap = len(

                question_words & title_words

            )

            title_score = title_overlap / max(

                len(question_words),

                1

            )

            ####################################################
            # Authority
            ####################################################

            authority = self.domain_score(

                chunk.source

            )

            ####################################################
            # Final Chunk Score
            ####################################################

            score = ChunkScore(

                semantic=semantic,

                keyword=keyword_score,

                entity=entity_score,

                title=title_score,

                authority=authority,

                freshness=0.0,

            )

            chunk.score = score.total

            ####################################################
            # Debug
            ####################################################

            print(

                f"[Score] "

                f"S={score.semantic:.3f} "

                f"K={score.keyword:.3f} "

                f"E={score.entity:.3f} "

                f"T={score.title:.3f} "

                f"A={score.authority:.3f} "

                f"F={score.freshness:.3f} "

                f"TOTAL={chunk.score:.3f}"

            )

        ########################################################
        # Sort
        ########################################################

        chunks.sort(

            key=lambda c: c.score,

            reverse=True,

        )

        ########################################################

        return chunks[:top_results]