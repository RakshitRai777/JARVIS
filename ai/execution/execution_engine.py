import time

from ai.actions.action_manager import ActionManager

from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_result import ExecutionResult

from ai.verification.verification_manager import (
    VerificationManager,
)


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

        if (

            context.policy.verify

            and

            context.step.verification_rule is not None

        ):

            verification = self.verification_manager.verify(

                context.step.verification_rule

            )

            ####################################################

            if not verification.success:

                return ExecutionResult(

                    success=False,

                    message="Verification failed.",

                    error=verification.error,

                    execution_time=(
                        time.perf_counter()
                        - start
                    ),

                )

        ########################################################

        return ExecutionResult(

            success=True,

            message=action_result.message,

            data=action_result.data,

            execution_time=(
                time.perf_counter()
                - start
            ),

        )