from ai.planner.decision import Decision
from ai.planner.planner_action import PlannerAction

from ai.planner.knowledge_classifier import (
    KnowledgeClassifier,
    KnowledgeSource,
)

from ai.tools.intent.tool_intent_classifier import (
    ToolIntentClassifier,
)

from ai.tools.intent.tool_intent import (
    ToolIntent,
)


class Planner:
    """
    Decides what should happen with the user's request.

    Priority
    --------
    1. System commands
    2. Tool intent
    3. Explicit memory commands
    4. Knowledge classification
    """

    ############################################################

    def __init__(self):

        self.knowledge_classifier = KnowledgeClassifier()

        self.tool_intent_classifier = ToolIntentClassifier()

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
        # Tool Intent
        ########################################################

        tool_intent = self.tool_intent_classifier.classify(
            text
        )

        if tool_intent != ToolIntent.NONE:

            return Decision(

                action=PlannerAction.TOOL,

                reason=(
                    f"Tool intent detected "
                    f"({tool_intent.value})."
                ),

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

        source = self.knowledge_classifier.classify(
            text
        )

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