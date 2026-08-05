from ai.tools.tool import Tool
from ai.tools.tool_registry import ToolRegistry

from ai.tools.intent.tool_intent import ToolIntent


class ToolResolver:
    """
    Resolves the best tool for a user's request.

    The ToolIntentClassifier determines the
    high-level intent.

    The ToolResolver asks every registered tool
    how confident it is, then selects the
    highest-scoring tool.
    """

    ############################################################

    def __init__(
        self,
        registry: ToolRegistry,
    ):

        self.registry = registry

    ############################################################

    def resolve(
        self,
        command: str,
        intent: ToolIntent,
    ) -> Tool | None:

        ########################################################
        # Ignore non-tool requests
        ########################################################

        if intent == ToolIntent.NONE:

            return None

        ########################################################
        # Find best matching tool
        ########################################################

        best_tool = None

        best_score = 0

        for tool in self.registry.all():

            try:

                score = tool.match_score(command)

            except Exception:

                score = 0

            if score > best_score:

                best_score = score

                best_tool = tool

        ########################################################

        return best_tool