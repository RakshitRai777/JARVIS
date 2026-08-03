from tools.base_tool import BaseTool


class ToolRegistry:
    """
    Registry of all available tools.
    """

    def __init__(self):

        self._tools = {}

    def register(
        self,
        tool: BaseTool
    ):

        self._tools[tool.name.lower()] = tool

    def get(
        self,
        name: str
    ):

        return self._tools.get(name.lower())

    def all(self):

        return self._tools

    def clear(self):

        self._tools.clear()

    def execute(
        self,
        tool_name: str,
        command: str
    ):

        tool = self.get(tool_name)

        if tool is None:
            return None

        return tool.execute(command)