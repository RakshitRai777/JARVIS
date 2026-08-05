import numpy as np


def cosine_similarity(a, b):

    return float(np.dot(a, b))


def top_k(scores, k):
    return sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:k]