import math
import re
from collections import Counter


class BM25PreFilter:
    """
    Lightweight BM25-style pre-ranking.

    Used BEFORE embeddings to reduce the number
    of chunks that need expensive semantic ranking.
    """

    k1 = 1.5
    b = 0.75

    ###########################################################

    def tokenize(self, text: str):

        return re.findall(
            r"[a-zA-Z0-9_]+",
            text.lower()
        )

    ###########################################################

    def score(self, query_tokens, document_tokens, avgdl):

        freq = Counter(document_tokens)

        score = 0.0

        doc_len = len(document_tokens)

        for token in query_tokens:

            if token not in freq:
                continue

            tf = freq[token]

            numerator = tf * (self.k1 + 1)

            denominator = (
                tf
                + self.k1
                * (
                    1
                    - self.b
                    + self.b * doc_len / max(avgdl, 1)
                )
            )

            score += numerator / denominator

        return score

    ###########################################################

    def filter(
        self,
        question,
        chunks,
        top_k=30,
    ):

        if len(chunks) <= top_k:
            return chunks

        query_tokens = self.tokenize(question)

        docs = [
            self.tokenize(chunk.text)
            for chunk in chunks
        ]

        avgdl = sum(len(d) for d in docs) / len(docs)

        scored = []

        for chunk, tokens in zip(chunks, docs):

            value = self.score(
                query_tokens,
                tokens,
                avgdl,
            )

            scored.append((value, chunk))

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        filtered = [

            chunk

            for _, chunk in scored[:top_k]

        ]

        print(

            f"[BM25] {len(chunks)} -> {len(filtered)} chunks"

        )

        return filtered