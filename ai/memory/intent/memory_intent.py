from enum import Enum


class MemoryIntent(Enum):

    STORE = "store"

    RECALL = "recall"

    UPDATE = "update"

    DELETE = "delete"

    UNKNOWN = "unknown"