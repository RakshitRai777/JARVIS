from dataclasses import dataclass
from datetime import datetime

from ai.memory.memory_type import MemoryType


@dataclass
class Memory:

    ############################################################

    memory_type: MemoryType

    ############################################################

    content: str

    ############################################################

    created_at: datetime

    ############################################################

    metadata: dict | None = None

    ############################################################
    # Semantic embedding
    ############################################################

    embedding: list[float] | None = None

    ############################################################
    # Structured memory
    ############################################################

    subject: str | None = None

    value: str | None = None

    category: str | None = None