from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult

from ai.tools.tool_context import ToolContext
from ai.tools.tool_executor import ToolExecutor


class ToolAction(Action):
    """
    Executes a generic tool command.

    The planner never knows which tool to use.
    ToolManager selects the best tool.
    """

    ############################################################

    def __init__(self):

        self.executor = ToolExecutor()

    ############################################################

    @property
    def name(self) -> str:

        return "tool"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################

        command = context.step.parameters.get(

            "command",

            "",

        )

        ########################################################

        result = self.executor.execute(

            command=command,

        )

        ########################################################

        return ActionResult(

            success=result.success,

            message=result.message,

            error=result.error,

            data=result.data,

        )