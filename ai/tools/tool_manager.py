from ai.tools.tool import Tool
from ai.tools.tool_registry import ToolRegistry

from ai.tools.utilities.calculator_tool import CalculatorTool

from ai.tools.system.open_app_tool import OpenAppTool
from ai.tools.system.close_app_tool import CloseAppTool
from ai.tools.desktop.screenshot_tool import ScreenshotTool
from ai.tools.filesystem.create_folder_tool import CreateFolderTool
from ai.tools.browser.open_url_tool import OpenURLTool
from ai.tools.browser.google_search_tool import GoogleSearchTool
from ai.tools.browser.youtube_search_tool import YouTubeSearchTool
from ai.tools.filesystem.create_file_tool import CreateFileTool
from ai.tools.filesystem.rename_tool import RenameTool
from ai.tools.filesystem.delete_tool import DeleteTool
from ai.tools.desktop.clipboard_tool import ClipboardTool
from ai.tools.desktop.volume_tool import VolumeTool
from ai.tools.desktop.lock_screen_tool import LockScreenTool
from ai.tools.vision.read_screen_tool import ReadScreenTool
from ai.tools.vision.explain_screen_tool import ExplainScreenTool
from ai.tools.vision.find_text_tool import FindTextTool
from ai.tools.vision.click_text_tool import ClickTextTool
from ai.tools.desktop.type_text_tool import TypeTextTool

class ToolManager:
    """
    Manages all registered tools.

    Responsibilities
    ----------------
    • Register tools
    • Unregister tools
    • Expose the ToolRegistry
    • Expose all registered tools

    ToolManager never decides which tool
    should execute a request.

    That responsibility belongs to the
    ToolResolver.
    """

    ############################################################

    def __init__(self):

        self._registry = ToolRegistry()

        self._register_builtin_tools()

    ############################################################

    def _register_builtin_tools(self):
        """
        Register built-in JARVIS tools.
        """

        self.register(

            CalculatorTool()

        )

        self.register(

            OpenAppTool()

        )

        self.register(

            CloseAppTool()

        )

        self.register(
            OpenURLTool()
        )

        self.register(
            GoogleSearchTool()
        )

        self.register(
            YouTubeSearchTool()
        )

        self.register(
            CreateFolderTool()
        )

        self.register(
            CreateFileTool()
        )

        self.register(
            RenameTool()
        )

        self.register(
            DeleteTool()
        )

        self.register(
            ScreenshotTool()
        )

        self.register(
            ClipboardTool()
        )

        self.register(
            VolumeTool()
        )

        self.register(
            LockScreenTool()
        )

        self.register(
            ReadScreenTool()
        )

        self.register(
            ExplainScreenTool()
        )

        self.register(
            FindTextTool()
        )

        self.register(
            ClickTextTool()
        )

        self.register(
            TypeTextTool()
        )

    ############################################################

    def register(
        self,
        tool: Tool,
    ):

        self._registry.register(tool)

    ############################################################

    def unregister(
        self,
        tool_name: str,
    ):

        self._registry.unregister(tool_name)

    ############################################################

    @property
    def tool_registry(
        self,
    ) -> ToolRegistry:
        """
        Exposes the ToolRegistry.

        The ToolResolver uses this
        to inspect registered tools.
        """

        return self._registry

    ############################################################

    def all_tools(
        self,
    ) -> list[Tool]:

        return self._registry.get_tools()