import time

from ai.actions.action_manager import ActionManager
from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_result import ExecutionResult
from ai.verification.verification_manager import VerificationManager


class ExecutionEngine:
    """
    Executes a single workflow step.

    Responsibilities
    ----------------
    • Execute actions
    • Execute verification
    • Apply execution policies
    • Return ExecutionResult

    Future Responsibilities
    -----------------------
    • Retry
    • Timeout
    • Recovery
    • Waiting
    • Screenshots
    """

    ############################################################

    def __init__(self):

        self.action_manager = ActionManager()

        self.verification_manager = VerificationManager()

    ############################################################

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionResult:

        start = time.perf_counter()

        ########################################################
        # Execute Action
        ########################################################

        action_result = self.action_manager.execute(

            workflow=context.workflow,

            step=context.step,

            metadata=context.metadata,

        )

        ########################################################

        if not action_result.success:

            return ExecutionResult(

                success=False,

                message=action_result.message,

                error=action_result.error,

                execution_time=(
                    time.perf_counter() - start
                ),

            )

        ########################################################
        # Verification
        ########################################################

        #
        # We intentionally skip verification for now.
        #
        # The policy exists.
        # The framework exists.
        # We'll connect them next.
        #

        ########################################################

        return ExecutionResult(

            success=True,

            message=action_result.message,

            data=action_result.data,

            execution_time=(
                time.perf_counter() - start
            ),

        )