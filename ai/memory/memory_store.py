from abc import ABC
from abc import abstractmethod


class MemoryStore(ABC):
    """
    Abstract storage backend for memories.
    """

    @abstractmethod
    def add(self, memory):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def clear(self):
        pass