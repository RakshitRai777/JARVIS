from ai.execution.execution_result import ExecutionResult

from tools.tool_registry import ToolRegistry
from tools.applications.chrome_tool import ChromeTool


class ToolExecutor:
    """
    Executes desktop tools.
    """

    def __init__(self):

        self.registry = ToolRegistry()

        # Register all available tools

        self.registry.register(
            ChromeTool()
        )

    def execute(
        self,
        context
    ) -> ExecutionResult:

        if not context.messages:

            return ExecutionResult(
                success=False,
                message="No command received."
            )

        command = context.messages[-1]["content"].lower()

        if "chrome" in command:

            result = self.registry.execute(
                "chrome",
                command
            )

            return ExecutionResult(
                success=result.success,
                message=result.message
            )

        return ExecutionResult(
            success=False,
            message="Unknown tool."
        )