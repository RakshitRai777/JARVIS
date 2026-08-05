from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from ai.embeddings.chunk import Chunk


@dataclass
class CacheEntry:
    """
    Represents one cached webpage.

    Stores:
    • URL
    • Page title
    • Processed chunks
    • Cache version
    • Creation time
    • Last access time
    """

    ############################################################

    url: str

    title: str

    chunks: List[Chunk]

    ############################################################
    # Cache metadata
    ############################################################

    version: int = 1

    created_at: datetime = field(default_factory=datetime.utcnow)

    last_accessed: datetime = field(default_factory=datetime.utcnow)

    ############################################################

    def touch(self):
        """
        Update the last access timestamp.
        """

        self.last_accessed = datetime.utcnow()