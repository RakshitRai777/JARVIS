from ai.execution.execution_checkpoint import ExecutionCheckpoint
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
    • Build workflow resume results

    Future Responsibilities
    -----------------------
    • Resume workflow execution
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

    def resume(
        self,
    ) -> WorkflowResumeResult:
        """
        Resume from the latest checkpoint.

        Version 1
        ---------
        Returns resume information only.

        Future versions will actually continue
        workflow execution.
        """

        ########################################################
        # No checkpoint available
        ########################################################

        if self._checkpoint is None:

            return WorkflowResumeResult(

                resumed=False,

            )

        ########################################################
        # Build execution result
        ########################################################

        execution = ExecutionResult(

            success=True,

            message="Workflow ready to resume.",

        )

        ########################################################
        # Build resume result
        ########################################################

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