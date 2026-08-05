from ai.tools.tool import Tool
from ai.tools.tool_registry import ToolRegistry

from ai.tools.utilities.calculator_tool import CalculatorTool

from ai.tools.system.open_app_tool import OpenAppTool
from ai.tools.system.close_app_tool import CloseAppTool

from ai.tools.browser.open_url_tool import OpenURLTool
from ai.tools.browser.google_search_tool import GoogleSearchTool
from ai.tools.browser.youtube_search_tool import YouTubeSearchTool

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