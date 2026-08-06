from ai.runtime.runtime_state import RuntimeState
from ai.runtime.runtime_history import RuntimeHistory
from datetime import datetime

from ai.runtime.runtime_history_entry import (
    RuntimeHistoryEntry,
)

class Runtime:
    """
    Central runtime controller.

    Owns the live RuntimeState and RuntimeHistory
    and provides methods for updating and resetting them.

    Future Responsibilities
    -----------------------
    • Sessions
    • History
    • Variables
    • Recovery
    """

    ############################################################

    def __init__(self):

        self.state = RuntimeState()

        self.history = RuntimeHistory()

    ############################################################

    def reset(
        self,
    ):
        """
        Reset runtime.
        """

        self.state = RuntimeState()

        self.history.clear()

    ############################################################

    def set_workflow(
        self,
        workflow: str,
    ):

        self.state.current_workflow = workflow

    ############################################################

    def set_step(
        self,
        step: str,
    ):

        self.state.current_step = step

    ############################################################

    def set_application(
        self,
        application: str,
    ):

        self.state.current_application = application

    ############################################################

    def set_window(
        self,
        window: str,
    ):

        self.state.current_window = window

    ############################################################

    def set_last_action(
        self,
        action: str,
    ):

        self.state.last_action = action

    ############################################################

    def set_last_tool(
        self,
        tool: str,
    ):

        self.state.last_tool = tool

    ############################################################

    def set_last_result(
        self,
        result,
    ):

        self.state.last_result = result

    ############################################################

    def update_from_execution(
        self,
        step,
        result,
    ):
        """
        Update runtime after a step execution.
        """

        ########################################################
        # Last execution
        ########################################################

        self.state.last_action = step.action

        self.state.last_result = result

        ########################################################
        # Store original command
        ########################################################

        command = step.parameters.get(

            "command",

            None,

        )

        self.state.last_command = command

        ########################################################
        # Placeholder
        ########################################################

        self.state.last_tool = None

        entry = RuntimeHistoryEntry(
            timestamp=datetime.now(),
            workflow=(
                self.state.current_workflow
                or "Unknown Workflow"
            ),

            step=(
                step.description
                or step.action
            ),
            action=step.action,
            command=command,
            result=result,
        )
        self.history.add(
            entry,
        )

    ############################################################

    @property
    def runtime_state(
        self,
    ) -> RuntimeState:

        return self.state

    ############################################################

    @property
    def runtime_history(
        self,
    ) -> RuntimeHistory:

        return self.history