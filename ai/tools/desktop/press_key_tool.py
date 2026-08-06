from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.keyboard_manager import Keyboard


class PressKeyTool(Tool):
    """
    Presses a single keyboard key.

    Examples
    --------
    Press Enter
    Press Tab
    Press Escape
    Press F5
    Press Left
    """

    ############################################################

    VALID_KEYS = {

        # Basic
        "enter",
        "tab",
        "space",
        "escape",
        "esc",
        "backspace",
        "delete",

        # Navigation
        "up",
        "down",
        "left",
        "right",
        "home",
        "end",
        "pageup",
        "pagedown",

        # Editing
        "insert",

        # Function keys
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",

    }

    ############################################################

    def __init__(self):

        self.keyboard = Keyboard()

    ############################################################

    @property
    def name(self):

        return "Press Key"

    ############################################################

    @property
    def description(self):

        return "Presses a keyboard key."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("press "):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        key = self._extract_key(

            context.command

        )

        if not key:

            return ToolResult(

                success=False,

                message="Please specify a key to press.",

            )

        if key not in self.VALID_KEYS:

            return ToolResult(

                success=False,

                message=f"Unsupported key: {key}",

            )

        ########################################################

        if key == "esc":

            key = "escape"

        ########################################################

        success = self.keyboard.press(

            key,

        )

        if success:

            return ToolResult(

                success=True,

                message=f"Pressed {key}.",

                data=key,

            )

        return ToolResult(

            success=False,

            message=f"Failed to press {key}.",

        )

    ############################################################

    def _extract_key(
        self,
        command: str,
    ) -> str:

        text = command.lower().strip()

        if text.startswith("press"):

            return text[5:].strip()

        return ""