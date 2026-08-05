from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.desktop_manager import DesktopManager


class LockScreenTool(Tool):
    """
    Locks the Windows workstation.
    """

    ############################################################

    def __init__(self):

        self.manager = DesktopManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Lock Screen"

    ############################################################

    @property
    def description(self) -> str:

        return "Locks the computer."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        keywords = [

            "lock",

            "lock screen",

            "lock computer",

            "lock pc",

            "lock workstation",

        ]

        if any(keyword in text for keyword in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        success = self.manager.lock_screen()

        if success:

            return ToolResult(

                success=True,

                message="Computer locked successfully.",

            )

        return ToolResult(

            success=False,

            message="Failed to lock the computer.",

        )