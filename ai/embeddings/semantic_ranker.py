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

        if not chunks:

            return []

        # Embed chunks only once
        if chunks[0].embedding is None:

            EmbeddingModel.embed_chunks(chunks)

        question_vector = EmbeddingModel.encode(question)

        scores = []

        for chunk in chunks:

            scores.append(

                cosine_similarity(

                    question_vector,

                    chunk.embedding

                )

            )

        best = top_k(

            scores,

            top_results

        )

        return [

            chunks[i]

            for i in best

        ]