import time

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
        # Retry configuration
        ########################################################

        timeout = 5.0          # seconds
        interval = 0.25        # seconds

        start = time.perf_counter()

        ########################################################
        # Retry until timeout
        ########################################################

        while True:

            window = self.manager.find(

                title,

            )

            if window is not None:

                break

            if time.perf_counter() - start >= timeout:

                return ActionResult(

                    success=False,

                    message=f"Window '{title}' was not found.",

                )

            time.sleep(

                interval,

            )

        ########################################################
        # Activate window
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