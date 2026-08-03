from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class Chunk:
    """
    Represents one semantic chunk of knowledge.

    This object travels through the entire RAG pipeline.

    It stores:
    - text
    - embedding
    - source information
    - retrieval score
    - metadata
    """

    # Original text
    text: str

    # Semantic embedding
    embedding: np.ndarray | None = None

    # Source URL
    source: str = ""

    # Page title
    title: str = ""

    # Similarity score
    score: float = 0.0

    # Future metadata
    metadata: dict[str, Any] = field(default_factory=dict)