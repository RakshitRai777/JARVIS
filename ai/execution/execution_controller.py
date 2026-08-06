from ai.execution.execution_state import ExecutionState


class ExecutionController:
    """
    Controls the lifecycle of workflow execution.

    Responsibilities
    ----------------
    • Start execution
    • Pause execution
    • Resume execution
    • Cancel execution
    • Complete execution
    • Mark execution as failed
    • Expose execution state
    """

    ############################################################

    def __init__(self):

        self._state = ExecutionState.IDLE

    ############################################################

    @property
    def state(self) -> ExecutionState:

        return self._state

    ############################################################

    def start(self):

        self._state = ExecutionState.RUNNING

    ############################################################

    def pause(self):

        if self._state == ExecutionState.RUNNING:

            self._state = ExecutionState.PAUSED

    ############################################################

    def resume(self):

        if self._state == ExecutionState.PAUSED:

            self._state = ExecutionState.RUNNING

    ############################################################

    def cancel(self):

        self._state = ExecutionState.CANCELLED

    ############################################################

    def complete(self):

        self._state = ExecutionState.COMPLETED

    ############################################################

    def fail(self):

        self._state = ExecutionState.FAILED

    ############################################################

    def reset(self):

        self._state = ExecutionState.IDLE

    ############################################################

    def is_idle(self) -> bool:

        return self._state == ExecutionState.IDLE

    ############################################################

    def is_running(self) -> bool:

        return self._state == ExecutionState.RUNNING

    ############################################################

    def is_paused(self) -> bool:

        return self._state == ExecutionState.PAUSED

    ############################################################

    def is_completed(self) -> bool:

        return self._state == ExecutionState.COMPLETED

    ############################################################

    def is_failed(self) -> bool:

        return self._state == ExecutionState.FAILED

    ############################################################

    def is_cancelled(self) -> bool:

        return self._state == ExecutionState.CANCELLED