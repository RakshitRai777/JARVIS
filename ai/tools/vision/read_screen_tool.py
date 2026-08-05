from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.vision.vision_manager import VisionManager


class ReadScreenTool(Tool):
    """
    Reads text from the current screen using OCR.
    """

    ############################################################

    def __init__(self):

        self.manager = VisionManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Read Screen"

    ############################################################

    @property
    def description(self) -> str:

        return "Reads text from the current screen."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        keywords = [

            "read screen",

            "read my screen",

            "what is on my screen",

            "what's on my screen",

            "extract text",

            "read this screen",

            "scan screen",

            "ocr",

        ]

        if any(keyword in text for keyword in keywords):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        result = self.manager.read_screen()

        if result.success:

            if result.text.strip():

                return ToolResult(

                    success=True,

                    message=result.text,

                    data=result,

                )

            return ToolResult(

                success=True,

                message="No readable text was found on the screen.",

                data=result,

            )

        return ToolResult(

            success=False,

            message=result.error,

        )