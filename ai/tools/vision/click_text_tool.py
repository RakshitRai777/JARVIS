from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.desktop.mouse_manager import MouseManager
from ai.tools.vision.text_locator import TextLocator
from ai.tools.vision.vision_manager import VisionManager


class ClickTextTool(Tool):
    """
    Clicks text currently visible on the screen.

    Version 1 defaults to Dry Run mode to safely
    verify OCR and coordinate detection before
    enabling real mouse clicks.
    """

    ############################################################

    TEST_MODE = "click"

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

        self.locator = TextLocator()

        self.mouse = MouseManager()

    ############################################################

    @property
    def name(self):

        return "Click Text"

    ############################################################

    @property
    def description(self):

        return "Clicks text visible on the screen."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("click on "):

            return 100

        if text.startswith("click "):

            return 100

        if text.startswith("press "):

            return 95

        if text.startswith("select "):

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

                message="Please specify what to click.",

            )

        ########################################################
        # Locate text
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
        # Geometry
        ########################################################

        x, y = element.center

        ########################################################
        # Test Modes
        ########################################################
        
        if self.TEST_MODE == "dry":
        
            return ToolResult(
        
                success=True,
        
                message=(
        
                    "[DRY RUN]\n\n"
        
                    f"Target      : {element.text}\n"
        
                    f"Confidence  : {element.confidence:.2f}\n"
        
                    f"Position    : ({x}, {y})\n\n"
        
                    "Mouse click NOT executed."
        
                ),
        
                data=element,
        
            )
        
        ########################################################
        
        if self.TEST_MODE == "move":
        
            self.mouse.move_to(
        
                x,
        
                y,
        
                duration=0.5,
        
            )
        
            return ToolResult(
        
                success=True,
        
                message=(
        
                    "[MOVE TEST]\n\n"
        
                    f"Target      : {element.text}\n"
        
                    f"Confidence  : {element.confidence:.2f}\n"
        
                    f"Mouse moved to ({x}, {y})"
        
                ),
        
                data=element,
        
            )

        ########################################################
        # Real Click
        ########################################################

        success = self.mouse.left_click(

            x,

            y,

        )

        if success:

            return ToolResult(

                success=True,

                message=(
                    f"Clicked '{element.text}' "
                    f"at ({x}, {y})."
                ),

                data=element,

            )

        return ToolResult(

            success=False,

            message="Mouse click failed.",

        )

    ############################################################

    def _extract_target(
        self,
        command: str,
    ) -> str:

        text = command.lower().strip()

        prefixes = [

            "click on",

            "click",

            "press",

            "select",

        ]

        for prefix in prefixes:

            if text.startswith(prefix):

                return command[
                    len(prefix):
                ].strip(" ?\"'")

        return ""