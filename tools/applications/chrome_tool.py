from tools.base_tool import BaseTool
from tools.tool_result import ToolResult


class ChromeTool(BaseTool):
    """
    Opens Google Chrome.
    """

    def __init__(self):

        super().__init__(
            name="chrome",
            description="Open Google Chrome"
        )

    def execute(
        self,
        command: str
    ) -> ToolResult:

        return ToolResult(
            success=True,
            message="Chrome tool executed."
        )