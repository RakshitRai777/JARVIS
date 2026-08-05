from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult

from ai.tools.desktop.press_key_tool import PressKeyTool
from ai.tools.tool_context import ToolContext


class PressKeyAction(Action):
    """
    Workflow Action that presses a keyboard key.

    Acts as an adapter between the Workflow
    system and the existing Tool system.
    """

    ############################################################

    def __init__(self):

        self.tool = PressKeyTool()

    ############################################################

    @property
    def name(self) -> str:

        return "press_key"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################
        # Extract parameter
        ########################################################

        key = context.step.parameters.get(

            "key",

            "",

        )

        ########################################################

        tool_context = ToolContext(

            command=f"Press {key}"

        )

        ########################################################

        result = self.tool.execute(

            tool_context

        )

        ########################################################

        return ActionResult(

            success=result.success,

            message=result.message,

            error=result.error,

            data={

                "key": key

            },

        )