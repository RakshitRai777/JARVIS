import time
from copy import deepcopy

from ai.actions.action_manager import ActionManager

from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_result import ExecutionResult

from ai.verification.verification_manager import VerificationManager

from ai.runtime.variable_resolver import VariableResolver


class ExecutionEngine:
    """
    Executes a single workflow step.

    Responsibilities
    ----------------
    • Execute actions
    • Execute verification
    • Apply execution policies
    • Resolve runtime variables
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
        # Work on a copy of the step
        ########################################################

        step = deepcopy(context.step)

        ########################################################
        # Resolve runtime variables
        ########################################################

        resolver = VariableResolver(

            context.runtime.runtime_variables,

        )

        ########################################################
        # Resolve every string parameter
        ########################################################

        for key, value in step.parameters.items():

            if isinstance(value, str):

                step.parameters[key] = resolver.resolve(

                    value,

                )

        ########################################################
        # Create resolved execution context
        ########################################################

        resolved_context = ExecutionContext(

            workflow=context.workflow,

            step=step,

            policy=context.policy,

            runtime=context.runtime,

            metadata=context.metadata,

            shared_data=context.shared_data,

            attempt=context.attempt,

        )

        ########################################################
        # Execute Action
        ########################################################

        action_result = self.action_manager.execute(

            workflow=resolved_context.workflow,

            step=resolved_context.step,

            metadata=resolved_context.metadata,

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

            resolved_context.policy.verify

            and

            resolved_context.step.verification_rule is not None

        ):

            verification = self.verification_manager.verify(

                resolved_context.step.verification_rule

            )

            ####################################################

            if not verification.success:

                return ExecutionResult(

                    success=False,

                    message="Verification failed.",

                    error=verification.error,

                    execution_time=(

                        time.perf_counter() - start

                    ),

                )

        ########################################################

        return ExecutionResult(

            success=True,

            message=action_result.message,

            data=action_result.data,

            execution_time=(

                time.perf_counter() - start

            ),

        )