from ai.tools.tool import Tool
from ai.tools.tool_registry import ToolRegistry
from ai.tools.utilities.calculator_tool import CalculatorTool
from ai.tools.system.open_app_tool import OpenAppTool
from ai.tools.system.close_app_tool import CloseAppTool
class ToolManager:
    """
    Manages all registered tools.

    Responsibilities
    ----------------
    • Register tools
    • Find the correct tool
    • Expose all available tools

    The ToolManager is the only class that
    should directly interact with the
    ToolRegistry.
    """

    ############################################################

    def __init__(self):

        self.registry = ToolRegistry()

        self._register_builtin_tools()

    ############################################################

    def _register_builtin_tools(self):
        """
        Register built-in JARVIS tools.

        New tools will be added here.
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
        

        pass

    ############################################################

    def register(
        self,
        tool: Tool,
    ):

        self.registry.register(tool)

    ############################################################

    def unregister(
        self,
        tool_name: str,
    ):

        self.registry.unregister(tool_name)

    ############################################################

    def find(
        self,
        command: str,
    ) -> Tool | None:

        return self.registry.find(command)

    ############################################################

    def all_tools(
        self,
    ) -> list[Tool]:

        return self.registry.get_tools()