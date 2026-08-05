from ai.knowledge.knowledge_result import KnowledgeResult
from ai.knowledge.knowledge_source import KnowledgeSource

from ai.planner.knowledge_classifier import (
    KnowledgeClassifier,
    KnowledgeSource as PlannerKnowledgeSource,
)


class KnowledgeRouter:
    """
    Determines where knowledge should come from.

    The routing decision is delegated entirely to the
    KnowledgeClassifier so that the Planner and Router
    always agree.
    """

    ############################################################

    def __init__(self):

        self.classifier = KnowledgeClassifier()

    ############################################################

    def route(
        self,
        message: str,
    ) -> KnowledgeResult:

        source = self.classifier.classify(message)

        ########################################################
        # Memory
        ########################################################

        if source == PlannerKnowledgeSource.MEMORY:

            return KnowledgeResult(

                source=KnowledgeSource.MEMORY,

                reason="Knowledge classifier selected memory.",

            )

        ########################################################
        # Web
        ########################################################

        if source == PlannerKnowledgeSource.WEB:

            return KnowledgeResult(

                source=KnowledgeSource.WEB,

                reason="Knowledge classifier selected web.",

            )

        ########################################################
        # LLM
        ########################################################

        return KnowledgeResult(

            source=KnowledgeSource.LLM,

            reason="Knowledge classifier selected LLM.",

        )