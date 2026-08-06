from ai.execution.execution_result import ExecutionResult
from ai.execution.recovery_result import RecoveryResult
from ai.execution.execution_context import ExecutionContext

class RecoveryEngine:
    """
    Handles recovery after execution has failed.

    Responsibilities
    ----------------
    • Collect failure information
    • Build RecoveryResult
    • Return structured recovery data

    Future Responsibilities
    -----------------------
    • Capture screenshot
    • Save runtime snapshot
    • Persist recovery reports
    • Automatic recovery
    • Planner-assisted recovery
    """

    ############################################################

    def recover(
        self,
        context: ExecutionContext,
        execution_result: ExecutionResult,
    ) -> RecoveryResult:

        ########################################################
        # Build recovery information
        ########################################################

        return RecoveryResult(

            recovered = execution_result.success,

            workflow=context.workflow,

            step=context.step.description,

            error=execution_result.error,

            execution_result=execution_result,

        )