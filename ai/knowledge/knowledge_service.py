from ai.knowledge.memory_knowledge import MemoryKnowledge
from ai.knowledge.web_knowledge import WebKnowledge


class KnowledgeService:
    """
    Unified interface for every knowledge source.

    Brain never talks directly to:

        WebPipeline
        Memory
        PDFs
        Vector DB

    It only talks to this service.
    """

    ##########################################################

    def __init__(self):

        self.web = WebKnowledge()

        self.memory = MemoryKnowledge()

    ##########################################################

    def search_web(
        self,
        question: str,
    ):

        return self.web.search(question)

    ##########################################################

    def search_memory(
        self,
        query: str,
    ):

        return self.memory.search(query)