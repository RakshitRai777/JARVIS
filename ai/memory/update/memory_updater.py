from ai.embeddings.embedding_model import EmbeddingModel
from ai.embeddings.similarity import cosine_similarity


class MemoryUpdater:
    """
    Finds the most relevant memory and updates it.
    """

    ############################################################

    def update(
        self,
        memories,
        new_memory,
        threshold=0.70,
    ):

        if not memories:
            return None

        ########################################################

        query_embedding = new_memory.embedding

        best = None
        best_score = 0.0

        ########################################################

        for memory in memories:

            if memory.embedding is None:
                continue

            score = cosine_similarity(

                query_embedding,

                memory.embedding,

            )

            if score > best_score:

                best_score = score

                best = memory

        ########################################################

        print()

        print(
            f"[MemoryUpdate] "
            f"Best={best_score:.3f}"
        )

        ########################################################

        if best_score < threshold:

            return None

        ########################################################

        best.content = new_memory.content

        best.embedding = new_memory.embedding

        return best