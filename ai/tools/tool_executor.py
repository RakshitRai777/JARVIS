from ai.tools.tool_context import ToolContext
from ai.tools.tool_manager import ToolManager
from ai.tools.tool_result import ToolResult


class ToolExecutor:
    """
    Executes JARVIS tools.

    Responsibilities
    ----------------
    • Find the correct tool
    • Build ToolContext
    • Execute the tool
    • Return ToolResult

    The executor never knows
    which tools exist.
    """

    ############################################################

    def __init__(self):

        self.manager = ToolManager()

    ############################################################

    def execute(
        self,
        command: str,
        conversation=None,
        metadata=None,
    ) -> ToolResult:

        ########################################################
        # Find tool
        ########################################################

        tool = self.manager.find(command)

        if tool is None:

            return ToolResult(

                success=False,

                message="I couldn't find a tool to handle that command.",

                error="Tool not found",

            )

        ########################################################
        # Build context
        ########################################################

        context = ToolContext(

            command=command,

            conversation=conversation,

            metadata=metadata,

        )

        ########################################################
        # Execute tool
        ########################################################

        try:

            return tool.execute(context)

        except Exception as e:

            return ToolResult(

                success=False,

                message=f"{tool.name} failed.",

                error=str(e),

            )