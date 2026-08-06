from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.keyboard_manager import Keyboard


class TypeTextTool(Tool):
    """
    Types text using the keyboard.

    Examples
    --------
    Type Hello World

    Write Hello Boss

    Enter My Name

    Input Testing 123
    """

    ############################################################

    def __init__(self):

        self.keyboard = Keyboard()

    ############################################################

    @property
    def name(self):

        return "Type Text"

    ############################################################

    @property
    def description(self):

        return "Types text using the keyboard."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("type "):

            return 100

        if text.startswith("write "):

            return 95

        if text.startswith("enter "):

            return 95

        if text.startswith("input "):

            return 95

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        text = self._extract_text(

            context.command

        )

        if not text:

            return ToolResult(

                success=False,

                message="Please specify the text to type.",

            )

        success = self.keyboard.type_text(

            text,

        )

        if success:

            return ToolResult(

                success=True,

                message=f'Typed:\n\n"{text}"',

                data=text,

            )

        return ToolResult(

            success=False,

            message="Failed to type text.",

        )

    ############################################################

    def _extract_text(
        self,
        command: str,
    ) -> str:

        text = command.strip()

        prefixes = [

            "type",

            "write",

            "enter",

            "input",

        ]

        lower = text.lower()

        for prefix in prefixes:

            if lower.startswith(prefix):

                return text[

                    len(prefix):

                ].strip()

        return ""