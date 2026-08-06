import time

from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult


class WaitAction(Action):
    """
    Waits for a specified amount of time.

    Used by the ReasoningEngine to pause execution
    before continuing to the next workflow step.
    """

    ############################################################

    @property
    def name(self) -> str:

        return "wait"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################
        # Read seconds
        ########################################################

        seconds = context.step.parameters.get(

            "seconds",

            1,

        )

        ########################################################

        time.sleep(seconds)

        ########################################################

        return ActionResult(

            success=True,

            message=f"Waited {seconds} second(s).",

        )