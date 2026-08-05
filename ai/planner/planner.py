from ai.planner.decision import Decision
from ai.planner.planner_action import PlannerAction

from ai.planner.knowledge_classifier import (
    KnowledgeClassifier,
    KnowledgeSource,
)


class Planner:
    """
    Decides what should happen with the user's request.

    Priority
    --------
    1. System commands
    2. Tool commands
    3. Explicit memory commands
    4. Knowledge classification
    """

    ############################################################

    def __init__(self):

        self.knowledge_classifier = KnowledgeClassifier()

        self.tool_keywords = {

            "open",
            "close",
            "shutdown",
            "restart",
            "search",
            "play",

        }

        self.system_commands = {

            "stop",
            "exit",
            "quit",

        }

    ############################################################

    def decide(
        self,
        message: str,
    ) -> Decision:

        text = message.lower().strip()

        ########################################################
        # System Commands
        ########################################################

        if text in self.system_commands:

            return Decision(

                action=PlannerAction.SYSTEM,

                reason="System command.",

            )

        ########################################################
        # Tool Commands
        ########################################################

        if any(
            text.startswith(word)
            for word in self.tool_keywords
        ):

            return Decision(

                action=PlannerAction.TOOL,

                reason="Tool command detected.",

            )

        ########################################################
        # Explicit Memory Storage
        ########################################################

        if text.startswith("remember"):

            return Decision(

                action=PlannerAction.MEMORY,

                reason="Memory storage requested.",

            )

        ########################################################
        # Knowledge Classification
        ########################################################

        source = self.knowledge_classifier.classify(text)

        if source == KnowledgeSource.MEMORY:

            return Decision(

                action=PlannerAction.MEMORY,

                reason="Knowledge classifier selected memory.",

            )

        if source == KnowledgeSource.WEB:

            return Decision(

                action=PlannerAction.LLM,

                reason="Knowledge classifier selected web.",

            )

        ########################################################
        # Default
        ########################################################

        return Decision(

            action=PlannerAction.LLM,

            reason="Knowledge classifier selected LLM.",

        )