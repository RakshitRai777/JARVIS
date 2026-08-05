from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult

from ai.tools.desktop.type_text_tool import TypeTextTool
from ai.tools.tool_context import ToolContext


class TypeTextAction(Action):
    """
    Workflow Action that types text.

    This is an adapter between the Workflow
    system and the existing Tool system.
    """

    ############################################################

    def __init__(self):

        self.tool = TypeTextTool()

    ############################################################

    @property
    def name(self) -> str:

        return "type_text"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################
        # Extract parameter
        ########################################################

        text = context.step.parameters.get(

            "text",

            "",

        )

        ########################################################

        tool_context = ToolContext(

            command=f"Type {text}"

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

                "text": text

            },

        )