from ai.llm_manager import LLMManager
from ai.rag.context_budget import ContextBudget
from ai.rag.prompt_builder import PromptBuilder


class AnswerGenerator:
    """
    Generates grounded answers from retrieved knowledge.

    Pipeline
    --------
    Question
        ↓
    Context Budget
        ↓
    PromptBuilder
        ↓
    LLM
        ↓
    Final Answer
    """

    ############################################################

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        self.context_budget = ContextBudget()

        self.llm = LLMManager()

    ############################################################

    def generate(

        self,

        question: str,

        chunks,

    ) -> str:

        ########################################################

        if not chunks:

            return (
                "I couldn't find enough reliable information "
                "to answer that question."
            )

        ########################################################
        # Context Budget
        ########################################################

        chunks = self.context_budget.limit(chunks)

        ########################################################
        # Prompt
        ########################################################

        messages = self.prompt_builder.build(

            question=question,

            chunks=chunks,

        )

        ########################################################

        return self.llm.generate(messages)