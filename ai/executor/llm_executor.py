from ai.execution.execution_result import ExecutionResult

from ai.knowledge.knowledge_router import KnowledgeRouter
from ai.knowledge.knowledge_source import KnowledgeSource
from ai.knowledge.knowledge_service import KnowledgeService

from ai.llm_manager import LLMManager

from ai.rag.rag_manager import RAGManager


class LLMExecutor:
    """
    Executes LLM requests.

    Responsibilities
    ----------------
    • Decide the knowledge source
    • Perform web retrieval when required
    • Use RAG for grounded answers
    • Use the normal LLM otherwise

    IMPORTANT
    ---------
    Query rewriting is NOT performed here.

    The Brain rewrites the query once and stores:
        • context.original_query
        • context.search_query

    This executor simply consumes those values.
    """

    ############################################################

    def __init__(self):

        self.llm = LLMManager()

        self.router = KnowledgeRouter()

        self.knowledge = KnowledgeService()

        self.rag = RAGManager()

    ############################################################

    def execute(self, context):

        ########################################################
        # Queries from Context
        ########################################################

        original_query = context.original_query

        search_query = context.search_query

        if not search_query:

            return ExecutionResult(

                success=False,

                message="No search query found."

            )

        ########################################################
        # Decide Knowledge Source
        ########################################################

        route = self.router.route(
            search_query
        )

        print(
            f"[KnowledgeRouter] "
            f"Source={route.source.value} | "
            f"Reason={route.reason}"
        )

        ########################################################
        # WEB
        ########################################################

        if route.source == KnowledgeSource.WEB:

            print("[LLMExecutor] Using Web RAG...")

            chunks = self.knowledge.search_web(
                search_query
            )

            ####################################################
            # Fallback if nothing found
            ####################################################

            if not chunks:

                print("[LLMExecutor] No web results found.")
                print("[LLMExecutor] Falling back to normal LLM.")

                reply = self.llm.generate(
                    context.messages
                )

            ####################################################
            # RAG Answer
            ####################################################

            else:

                reply = self.rag.answer(

                    question=search_query,

                    chunks=chunks,

                )

        ########################################################
        # MEMORY (Future)
        ########################################################

        elif route.source == KnowledgeSource.MEMORY:

            print("[LLMExecutor] Memory routing not implemented.")
            print("[LLMExecutor] Falling back to normal LLM.")

            reply = self.llm.generate(
                context.messages
            )

        ########################################################
        # GENERAL LLM
        ########################################################

        else:

            print("[LLMExecutor] Using Normal LLM...")

            reply = self.llm.generate(
                context.messages
            )

        ########################################################

        return ExecutionResult(

            success=True,

            message=reply

        )