from runtime.base_service import BaseService

from ai.embeddings.embedding_model import EmbeddingModel
from ai.memory.memory_manager import MemoryManager


class MemoryService(BaseService):

    ############################################################

    def __init__(self):

        super().__init__("Memory")

        self.manager = MemoryManager()

    ############################################################

    def remember(self, memory):

        ########################################################
        # Generate embedding automatically
        ########################################################

        if memory.embedding is None:

            memory.embedding = EmbeddingModel.encode(

                memory.content,

            ).tolist()

        ########################################################
        # Prevent duplicates
        ########################################################

        if self.manager.exists(memory):

            return False

        ########################################################
        # Store memory
        ########################################################

        self.manager.add(memory)

        return True

    ############################################################

    def update(self, memory):

        ########################################################
        # Generate embedding automatically
        ########################################################

        if memory.embedding is None:

            memory.embedding = EmbeddingModel.encode(

                memory.content,

            ).tolist()

        ########################################################

        return self.manager.update(memory)

    ############################################################

    def get_all(self):

        return self.manager.get_all()

    ############################################################

    def find(self, query):

        return self.manager.find(query)

    ############################################################

    def clear(self):

        self.manager.clear()

    ############################################################

    def count(self):

        return self.manager.count()