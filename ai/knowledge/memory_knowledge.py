from runtime.runtime import runtime


class MemoryKnowledge:
    """
    Handles retrieval from the memory system.
    """

    def search(

        self,

        query: str,

    ):

        memory = runtime.services.get("memory")

        if memory is None:

            return []

        return memory.find(query)