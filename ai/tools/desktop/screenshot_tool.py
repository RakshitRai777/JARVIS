from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.desktop_manager import DesktopManager


class ScreenshotTool(Tool):
    """
    Takes screenshots of the desktop.
    """

    ############################################################

    def __init__(self):

        self.manager = DesktopManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Screenshot"

    ############################################################

    @property
    def description(self) -> str:

        return "Captures a screenshot of the desktop."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower()

        keywords = [

            "screenshot",
            "screen shot",
            "capture screen",
            "capture the screen",
            "take screenshot",
            "take a screenshot",
            "take screen shot",

        ]

        if any(keyword in text for keyword in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        file = self.manager.take_screenshot()

        if file:

            return ToolResult(

                success=True,

                message=f"Screenshot saved to:\n{file}",

                data=file,

            )

        return ToolResult(

            success=False,

            message="Failed to take screenshot.",

        )