from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.keyboard_manager import KeyboardManager


class HotkeyTool(Tool):
    """
    Executes keyboard shortcuts.

    Examples
    --------
    Press Ctrl C
    Press Ctrl V
    Press Ctrl Shift S
    Press Alt Tab
    Press Win D
    """

    ############################################################

    MODIFIER_KEYS = {

        "ctrl",
        "shift",
        "alt",
        "win",
        "windows",

    }

    ############################################################

    def __init__(self):

        self.keyboard = KeyboardManager()

    ############################################################

    @property
    def name(self):

        return "Hotkey"

    ############################################################

    @property
    def description(self):

        return "Executes keyboard shortcuts."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if not text.startswith("press "):

            return 0

        words = text.split()

        modifiers = sum(
            word in self.MODIFIER_KEYS
            for word in words
        )

        if modifiers >= 1:

            return 110

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        keys = self._extract_keys(

            context.command

        )

        if len(keys) < 2:

            return ToolResult(

                success=False,

                message="Please specify a keyboard shortcut.",

            )

        ########################################################

        normalized = []

        for key in keys:

            if key == "windows":

                key = "win"

            normalized.append(key)

        ########################################################

        success = self.keyboard.hotkey(

            *normalized

        )

        if success:

            return ToolResult(

                success=True,

                message=f"Pressed {' + '.join(normalized)}.",

                data=normalized,

            )

        return ToolResult(

            success=False,

            message="Failed to execute hotkey.",

        )

    ############################################################

    def _extract_keys(
        self,
        command: str,
    ) -> list[str]:

        text = command.lower().strip()

        if text.startswith("press"):

            text = text[5:].strip()

        return text.split()