from ai.embeddings.embedding_model import EmbeddingModel
from ai.embeddings.similarity import cosine_similarity
from ai.embeddings.similarity import top_k


class SemanticRanker:

    def rank(

        self,

        question,

        chunks,

        top_results=5

    ):

        # No chunks to rank
        if not chunks:
            return []

        # Generate embeddings only once
        if chunks[0].embedding is None:
            EmbeddingModel.embed_chunks(chunks)

        # Embed the user's question
        question_vector = EmbeddingModel.encode(question)

        scores = []

        # Compute similarity for every chunk
        for chunk in chunks:
            score = cosine_similarity(
                question_vector,
                chunk.embedding
            )

            # Store score inside the chunk
            chunk.score = score

            scores.append(score)

        # Get indices of top scoring chunks
        best = top_k(
            scores,
            top_results
        )

        # Return ranked chunks
        return [
            chunks[i]
            for i in best
        ]