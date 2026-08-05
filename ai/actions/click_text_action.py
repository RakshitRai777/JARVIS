from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult

from ai.tools.vision.click_text_tool import ClickTextTool
from ai.tools.tool_context import ToolContext


class ClickTextAction(Action):
    """
    Workflow Action that clicks text on the screen.

    Currently this wraps ClickTextTool.
    Later it will directly use VisionManager
    and MouseManager.
    """

    ############################################################

    def __init__(self):

        self.tool = ClickTextTool()

    ############################################################

    @property
    def name(self) -> str:

        return "click_text"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################
        # Extract parameter
        ########################################################

        target = context.step.parameters.get(

            "target",

            "",

        )

        ########################################################

        tool_context = ToolContext(

            command=f"Click {target}"

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

                "target": target

            },

        )