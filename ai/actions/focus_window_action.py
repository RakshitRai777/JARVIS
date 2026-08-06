from ai.actions.action import Action
from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult

from ai.desktop.window_manager import WindowManager


class FocusWindowAction(Action):
    """
    Activates a desktop window.

    Used by the ReasoningEngine after
    launching an application.
    """

    ############################################################

    def __init__(self):

        self.manager = WindowManager()

    ############################################################

    @property
    def name(self) -> str:

        return "focus_window"

    ############################################################

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:

        ########################################################
        # Read target
        ########################################################

        title = context.step.parameters.get(

            "application",

            "",

        )

        ########################################################

        window = self.manager.find(

            title,

        )

        ########################################################

        if window is None:

            return ActionResult(

                success=False,

                message=f"Window '{title}' was not found.",

            )

        ########################################################

        try:

            window.activate()

        except Exception as ex:

            return ActionResult(

                success=False,

                message=str(ex),

            )

        ########################################################

        return ActionResult(

            success=True,

            message=f"Focused '{window.title}'.",

        )