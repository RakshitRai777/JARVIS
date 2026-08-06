import time
from copy import deepcopy

from ai.actions.action_manager import ActionManager

from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_result import ExecutionResult
from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_resume_engine import ExecutionResumeEngine
from ai.execution.execution_controller import ExecutionController

from ai.execution.retry_engine import RetryEngine
from ai.execution.retry_policy import RetryPolicy
from ai.execution.recovery_engine import RecoveryEngine

from ai.planner.condition_evaluator import ConditionEvaluator
from ai.runtime.variable_resolver import VariableResolver
from ai.verification.verification_manager import VerificationManager


class ExecutionEngine:
    """
    Executes a single workflow step.

    Responsibilities
    ----------------
    • Resolve runtime variables
    • Evaluate execution conditions
    • Execute actions
    • Execute verification
    • Apply retry policies
    • Save execution checkpoints
    • Return ExecutionResult
    """

    ############################################################

    def __init__(self):

        self.action_manager = ActionManager()

        self.verification_manager = VerificationManager()

        self.retry_engine = RetryEngine()

        self.recovery_engine = RecoveryEngine()

        self.resume_engine = ExecutionResumeEngine()

        self.controller = ExecutionController()

    ############################################################

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionResult:

        start = time.perf_counter()

        ########################################################
        # Execution started
        ########################################################

        self.controller.start()

        ########################################################
        # Work on a copy of the execution step
        ########################################################

        step = deepcopy(

            context.step,

        )

        ########################################################
        # Resolve runtime variables
        ########################################################

        resolver = VariableResolver(

            context.runtime.runtime_variables,

        )

        for key, value in step.parameters.items():

            if isinstance(value, str):

                step.parameters[key] = resolver.resolve(

                    value,

                )

        ########################################################
        # Condition evaluator
        ########################################################

        condition_evaluator = ConditionEvaluator(

            context.runtime.runtime_variables,

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
        # Evaluate execution condition
        ########################################################

        if resolved_context.step.condition is not None:

            should_execute = condition_evaluator.evaluate(

                resolved_context.step.condition,

            )

            if not should_execute:

                self.controller.complete()

                return ExecutionResult(

                    success=True,

                    message="Step skipped (condition evaluated to False).",

                    execution_time=(

                        time.perf_counter() - start

                    ),

                )

        ########################################################
        # Execute action
        ########################################################

        retry_policy = RetryPolicy()

        action_result = self.retry_engine.execute(

            operation=lambda: self.action_manager.execute(

                resolved_context,

            ),

            policy=retry_policy,

        )

        ########################################################
        # Action failed
        ########################################################

        if not action_result.success:

            self.controller.fail()

            recovery = self.recovery_engine.recover(

                context=resolved_context,

                execution_result=action_result,

            )

            return ExecutionResult(

                success=False,

                message=action_result.message,

                data=recovery,

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

                resolved_context.step.verification_rule,

            )

            if not verification.success:

                self.controller.fail()

                return ExecutionResult(

                    success=False,

                    message="Verification failed.",

                    error=verification.error,

                    execution_time=(

                        time.perf_counter() - start

                    ),

                )

        ########################################################
        # Save checkpoint
        ########################################################

        checkpoint = ExecutionCheckpoint(

            workflow=resolved_context.workflow,

            current_step=resolved_context.attempt,

            total_steps=resolved_context.shared_data.get(

                "total_steps",

                1,

            ),

        )

        self.resume_engine.save_checkpoint(

            checkpoint,

        )

        ########################################################
        # Success
        ########################################################

        self.controller.complete()

        return ExecutionResult(

            success=True,

            message=action_result.message,

            data=action_result.data,

            execution_time=(

                time.perf_counter() - start

            ),

        )