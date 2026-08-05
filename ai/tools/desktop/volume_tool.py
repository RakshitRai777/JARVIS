import re

from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.desktop_manager import DesktopManager


class VolumeTool(Tool):

    ############################################################

    def __init__(self):

        self.manager = DesktopManager()

    ############################################################

    @property
    def name(self):

        return "Volume"

    ############################################################

    @property
    def description(self):

        return "Controls system volume."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower()

        keywords = [

            "volume",

            "mute",

            "unmute",

            "sound",

        ]

        if any(word in text for word in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context,
    ) -> ToolResult:

        command = context.command.lower()

        ########################################################

        if "mute" in command and "unmute" not in command:

            if self.manager.mute():

                return ToolResult(

                    True,

                    "System muted.",

                )

        ########################################################

        if "unmute" in command:

            if self.manager.unmute():

                return ToolResult(

                    True,

                    "System unmuted.",

                )

        ########################################################

        match = re.search(

            r"(\d+)",

            command,

        )

        if match:

            percent = int(match.group(1))

            if self.manager.set_volume(percent):

                return ToolResult(

                    True,

                    f"Volume set to {percent}%."

                )

        ########################################################

        volume = self.manager.get_volume()

        if volume >= 0:

            return ToolResult(

                True,

                f"Current volume is {volume}%."

            )

        return ToolResult(

            False,

            "Unable to control volume."

        )