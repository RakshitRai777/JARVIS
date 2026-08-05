from sentence_transformers import CrossEncoder


class CrossEncoderRanker:
    """
    Production Cross-Encoder Re-ranker.

    Pipeline
    --------
    Hybrid Rank
        ↓
    CrossEncoder Score
        ↓
    Normalize Scores
        ↓
    Hybrid + CrossEncoder Fusion
        ↓
    Final Ranking

    The CrossEncoder deeply understands the relationship
    between the user's question and each retrieved chunk.
    """

    ############################################################

    MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    HYBRID_WEIGHT = 0.35

    CROSS_WEIGHT = 0.65

    ############################################################

    def __init__(self):

        print("[CrossEncoder] Loading model...")

        self.model = CrossEncoder(

            self.MODEL_NAME

        )

        print("[CrossEncoder] Model loaded.")

    ############################################################

    def rerank(

        self,

        question: str,

        chunks,

        top_k: int = 5,

    ):

        ########################################################

        if not chunks:

            return []

        ########################################################
        # Build (question, chunk) pairs
        ########################################################

        pairs = [

            (

                question,

                chunk.text

            )

            for chunk in chunks

        ]

        ########################################################
        # Predict CrossEncoder scores
        ########################################################

        cross_scores = self.model.predict(

            pairs

        )

        ########################################################
        # Normalize scores to [0, 1]
        ########################################################

        minimum = float(min(cross_scores))

        maximum = float(max(cross_scores))

        scale = maximum - minimum

        if scale == 0:

            scale = 1.0

        ########################################################
        # Combine scores
        ########################################################

        for chunk, raw_score in zip(

            chunks,

            cross_scores

        ):

            normalized = (

                float(raw_score) - minimum

            ) / scale

            chunk.cross_score = normalized

            hybrid_score = getattr(

                chunk,

                "score",

                0.0

            )

            final_score = (

                self.HYBRID_WEIGHT * hybrid_score

                +

                self.CROSS_WEIGHT * normalized

            )

            chunk.final_score = final_score

            ####################################################
            # Debug
            ####################################################

            print(

                f"[CrossEncoder] "

                f"H={hybrid_score:.3f} "

                f"C={normalized:.3f} "

                f"F={final_score:.3f} "

                f"| {chunk.title}"

            )

        ########################################################
        # Sort using fused score
        ########################################################

        chunks.sort(

            key=lambda c: c.final_score,

            reverse=True,

        )

        ########################################################
        # Return top chunks
        ########################################################

        return chunks[:top_k]