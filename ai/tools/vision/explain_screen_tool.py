from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.vision.vision_manager import VisionManager
from ai.tools.vision.vision_reasoner import VisionReasoner


class ExplainScreenTool(Tool):
    """
    Explains the user's current screen using
    OCR + LLM reasoning.
    """

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

        self.reasoner = VisionReasoner()

    ############################################################

    @property
    def name(self):

        return "Explain Screen"

    ############################################################

    @property
    def description(self):

        return "Explains the current screen."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower()

        keywords = [

            "explain screen",

            "explain my screen",

            "describe my screen",

            "what am i looking at",

            "understand screen",

        ]

        if any(keyword in text for keyword in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        ########################################################
        # Read Screen
        ########################################################

        result = self.vision.read_screen()

        if not result.success:

            return ToolResult(

                success=False,

                message=result.error,

            )

        ########################################################
        # Reason About Screen
        ########################################################

        try:
            explanation = self.reasoner.explain(result)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return ToolResult(
                success=False,
                message=str(e),
            )
        ########################################################

        return ToolResult(

            success=True,

            message=explanation,

            data=result,

        )