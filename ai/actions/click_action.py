from ai.actions.action import Action
from ai.execution.execution_result import ExecutionResult
from ai.tools.desktop.click_tool import ClickTool


class ClickAction(Action):
    """
    Generic click action.

    Works with any Locator implementation.
    """

    ############################################################

    def __init__(self):

        self.tool = ClickTool()

    ############################################################

    @property
    def name(self) -> str:

        return "click"

    ############################################################

    def execute(
        self,
        locator,
    ) -> ExecutionResult:

        success = self.tool.click(

            locator

        )

        if success:

            return ExecutionResult(

                success=True,

                message="Click completed.",

            )

        return ExecutionResult(

            success=False,

            message="Unable to locate target.",

        )