from ai.tools.tool import Tool


class ToolRegistry:
    """
    Stores every available tool.

    Responsibilities
    ----------------
    • Register tools
    • Unregister tools
    • Find tools
    • Expose all registered tools
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
        Remove a tool.
        """

        self._tools = [

            tool

            for tool in self._tools

            if tool.name != tool_name

        ]

    ############################################################

    def all(
        self,
    ) -> list[Tool]:

        """
        Return every registered tool.
        """

        return self._tools.copy()

    ############################################################

    def get_tools(
        self,
    ) -> list[Tool]:
        """
        Backward compatibility.

        TODO:
            Remove after migrating
            all callers to all().
        """

        return self.all()

    ############################################################

    def find(
        self,
        command: str,
    ) -> Tool | None:

        """
        Find the first tool that can
        handle the command.
        """

        for tool in self._tools:

            if tool.can_handle(command):

                return tool

        return None