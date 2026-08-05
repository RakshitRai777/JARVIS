from ai.tools.tool import Tool


class ToolRegistry:
    """
    Stores every available tool.

    New tools register themselves here.

    The ToolManager discovers tools from
    this registry.
    """

    ############################################################

    def __init__(self):

        self._tools: list[Tool] = []

    ############################################################

    def register(
        self,
        tool: Tool,
    ):

        """
        Register a tool.
        """

        self._tools.append(tool)

    ############################################################

    def unregister(
        self,
        tool_name: str,
    ):

        """
        Remove a tool by name.
        """

        self._tools = [

            tool

            for tool in self._tools

            if tool.name != tool_name

        ]

    ############################################################

    def get_tools(self) -> list[Tool]:

        """
        Return all registered tools.
        """

        return self._tools.copy()

    ############################################################

    def find(
        self,
        command: str,
    ) -> Tool | None:

        """
        Find the first tool that can
        execute the command.
        """

        for tool in self._tools:

            if tool.can_handle(command):

                return tool

        return None