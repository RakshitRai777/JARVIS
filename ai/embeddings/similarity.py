import numpy as np


def cosine_similarity(a, b):

    return float(np.dot(a, b))


def top_k(scores, k):

    order = np.argsort(scores)[::-1]

    return order[:k]