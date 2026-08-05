from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.vision.vision_manager import VisionManager
from ai.tools.vision.text_locator import TextLocator


class FindTextTool(Tool):
    """
    Finds text currently visible on the screen.
    """

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

        self.locator = TextLocator()

    ############################################################

    @property
    def name(self):

        return "Find Text"

    ############################################################

    @property
    def description(self):

        return "Finds text on the current screen."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("find "):

            return 100

        if text.startswith("locate "):

            return 100

        if text.startswith("where is "):

            return 95

        if text.startswith("search screen for "):

            return 95

        if text.startswith("find text "):

            return 95

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        ########################################################
        # Read screen
        ########################################################

        result = self.vision.read_screen()

        if not result.success:

            return ToolResult(

                success=False,

                message=result.error,

            )

        ########################################################
        # Extract target
        ########################################################

        target = self._extract_target(

            context.command

        )

        if not target:

            return ToolResult(

                success=False,

                message="Please specify the text to find.",

            )

        ########################################################
        # Locate
        ########################################################

        element = self.locator.find_best_match(

            result.elements,

            target,

        )

        if element is None:

            return ToolResult(

                success=False,

                message=f"'{target}' was not found on the screen.",

            )

        ########################################################

        x, y = element.center

        ########################################################

        return ToolResult(

            success=True,

            message=(
                f"Found '{element.text}'\n\n"
                f"Confidence : {element.confidence:.2f}\n"
                f"Center : ({x}, {y})"
            ),

            data=element,

        )

    ############################################################

    def _extract_target(
        self,
        command: str,
    ) -> str:

        text = command.lower().strip()

        prefixes = [

            "search screen for",

            "where is",

            "find text",

            "locate",

            "find",

        ]

        for prefix in prefixes:

            if text.startswith(prefix):

                return command[

                    len(prefix):

                ].strip(" ?\"'")

        return ""