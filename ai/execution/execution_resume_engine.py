from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_cursor import ExecutionCursor
from ai.execution.execution_result import ExecutionResult
from ai.execution.workflow_resume_result import WorkflowResumeResult


class ExecutionResumeEngine:
    """
    Manages workflow execution checkpoints.

    Responsibilities
    ----------------
    • Save checkpoints
    • Retrieve checkpoints
    • Clear checkpoints
    • Report checkpoint availability
    • Position an ExecutionCursor for workflow resume

    Future Responsibilities
    -----------------------
    • Persist checkpoints to disk
    • Restore checkpoints after restart
    """

    ############################################################

    def __init__(self):

        self._checkpoint: ExecutionCheckpoint | None = None

    ############################################################

    def save_checkpoint(
        self,
        checkpoint: ExecutionCheckpoint,
    ) -> None:

        self._checkpoint = checkpoint

    ############################################################

    def get_checkpoint(
        self,
    ) -> ExecutionCheckpoint | None:

        return self._checkpoint

    ############################################################

    def has_checkpoint(
        self,
    ) -> bool:

        return self._checkpoint is not None

    ############################################################

    def clear_checkpoint(
        self,
    ) -> None:

        self._checkpoint = None

    ############################################################

    def resume_cursor(
        self,
        cursor: ExecutionCursor,
    ) -> WorkflowResumeResult:
        """
        Position the execution cursor at the saved checkpoint.

        This method does not execute any workflow steps.
        Execution remains the responsibility of PlanExecutor.
        """

        ########################################################
        # No checkpoint available
        ########################################################

        if self._checkpoint is None:

            return WorkflowResumeResult(

                resumed=False,

            )

        ########################################################
        # Position cursor
        ########################################################

        cursor.goto(

            self._checkpoint.current_step,

        )

        ########################################################
        # Build execution result
        ########################################################

        execution = ExecutionResult(

            success=True,

            message="Workflow ready to resume.",

        )

        ########################################################
        # Return resume result
        ########################################################

        return WorkflowResumeResult(

            resumed=True,

            checkpoint=self._checkpoint,

            execution_result=execution,

            resumed_step=cursor.index,

            completed=(
                cursor.index >= cursor.total_steps
            ),

        )

    ############################################################

    def resume(
        self,
    ) -> WorkflowResumeResult:
        """
        Backward-compatible API.

        Returns resume information without requiring
        an ExecutionCursor.
        """

        if self._checkpoint is None:

            return WorkflowResumeResult(

                resumed=False,

            )

        execution = ExecutionResult(

            success=True,

            message="Workflow ready to resume.",

        )

        return WorkflowResumeResult(

            resumed=True,

            checkpoint=self._checkpoint,

            execution_result=execution,

            resumed_step=self._checkpoint.current_step,

            completed=(
                self._checkpoint.current_step
                >=
                self._checkpoint.total_steps
            ),

        )