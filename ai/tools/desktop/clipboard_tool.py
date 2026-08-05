from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.desktop_manager import DesktopManager


class ClipboardTool(Tool):
    """
    Reads the clipboard.
    """

    ############################################################

    def __init__(self):

        self.manager = DesktopManager()

    ############################################################

    @property
    def name(self):

        return "Clipboard"

    ############################################################

    @property
    def description(self):

        return "Reads clipboard contents."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower()

        keywords = [

            "clipboard",

            "read clipboard",

            "show clipboard",

            "paste clipboard",

            "what's in my clipboard",

            "what is in my clipboard",

        ]

        if any(keyword in text for keyword in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context,
    ) -> ToolResult:

        text = self.manager.get_clipboard()

        if text is None:

            return ToolResult(

                success=False,

                message="Unable to read the clipboard.",

            )

        if text == "":

            return ToolResult(

                success=True,

                message="Clipboard is empty.",

            )

        return ToolResult(

            success=True,

            message=f"Clipboard:\n{text}",

            data=text,

        )