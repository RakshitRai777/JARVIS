from ai.actions.action_context import ActionContext
from ai.actions.action_registry import ActionRegistry
from ai.actions.action_result import ActionResult

from ai.actions.tool_action import ToolAction
from ai.actions.wait_action import WaitAction
from ai.actions.focus_window_action import FocusWindowAction
from ai.actions.type_text_action import TypeTextAction
from ai.actions.press_key_action import PressKeyAction
from ai.actions.click_text_action import ClickTextAction

from ai.execution.execution_context import ExecutionContext


class ActionManager:
    """
    Central execution manager for workflow actions.
    """

    ############################################################

    def __init__(self):

        self.registry = ActionRegistry()

        ########################################################
        # Register actions
        ########################################################

        self.registry.register(ToolAction())
        self.registry.register(WaitAction())
        self.registry.register(FocusWindowAction())
        self.registry.register(TypeTextAction())
        self.registry.register(PressKeyAction())
        self.registry.register(ClickTextAction())

    ############################################################

    def execute(
        self,
        context: ExecutionContext,
    ) -> ActionResult:

        ########################################################
        # Resolve action
        ########################################################

        action = self.registry.get(

            context.step.action,

        )

        ########################################################

        if action is None:

            return ActionResult(

                success=False,

                error=f"No action registered for '{context.step.action}'.",

            )

        ########################################################
        # Build ActionContext
        ########################################################

        action_context = ActionContext(

            workflow=context.workflow,

            step=context.step,

            runtime=context.runtime,

            metadata=context.metadata,

            shared_data=context.shared_data,

        )

        ########################################################
        # Execute
        ########################################################

        return action.execute(

            action_context,

        )