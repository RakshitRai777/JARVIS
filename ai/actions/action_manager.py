from ai.actions.action_context import ActionContext
from ai.actions.action_registry import ActionRegistry
from ai.actions.action_result import ActionResult

from ai.actions.type_text_action import TypeTextAction
from ai.actions.press_key_action import PressKeyAction

from ai.actions.click_text_action import ClickTextAction

class ActionManager:
    """
    Central execution manager for all workflow actions.

    Responsibilities
    ----------------
    • Register actions
    • Resolve actions
    • Build ActionContext
    • Execute actions

    Future responsibilities
    -----------------------
    • Verification
    • Retry
    • Logging
    • Metrics
    • Screenshots
    • Recovery
    """

    ############################################################

    def __init__(self):

        self.registry = ActionRegistry()

        ########################################################
        # Register Actions
        ########################################################

        self.registry.register(
            TypeTextAction()
        )

        self.registry.register(
            PressKeyAction()
        )

        self.registry.register(
            ClickTextAction()
        )

    ############################################################

    def execute(
        self,
        workflow,
        step,
        metadata=None,
    ) -> ActionResult:

        ########################################################
        # Resolve Action
        ########################################################

        action = self.registry.get(

            step.action

        )

        if action is None:

            return ActionResult(

                success=False,

                error=f"No action registered for '{step.action}'.",

            )

        ########################################################
        # Build Context
        ########################################################

        context = ActionContext(

            workflow=workflow,

            step=step,

            metadata=metadata or {},

        )

        ########################################################
        # Execute
        ########################################################

        return action.execute(

            context

        )