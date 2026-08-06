from ai.memory.memory_context import MemoryContext
from ai.memory.memory_service import MemoryService


class MemoryRetriever:
    """
    Retrieves memories relevant to the current request.
    """

    ############################################################

    def __init__(self):

        self.memory_service = MemoryService()

    ############################################################

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> MemoryContext:

        ########################################################
        # Create context
        ########################################################

        context = MemoryContext(

            query=query,

        )

        ########################################################
        # Retrieve memories
        ########################################################

        memories = self.memory_service.find(

            query,

        )

        ########################################################

        for memory in memories[:top_k]:

            context.add(

                memory,

            )

        ########################################################

        return context