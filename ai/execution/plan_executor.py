from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy
from ai.execution.execution_result import ExecutionResult

from ai.workflow.workflow import Workflow

from ai.runtime.runtime import Runtime


class PlanExecutor:
    """
    Executes an entire ExecutionPlan.

    Responsibilities
    ----------------
    • Execute every step in order
    • Maintain Runtime state
    • Stop on failure
    • Return the final ExecutionResult

    Future
    ------
    • Retry
    • Recovery
    • Parallel execution
    • Conditional branches
    """

    ############################################################

    def __init__(self):

        self.engine = ExecutionEngine()

        self.runtime = Runtime()

    ############################################################

    def execute(
        self,
        plan,
        workflow_name: str = "Execution Plan",
    ) -> ExecutionResult:

        ########################################################
        # Reset runtime for a new execution
        ########################################################

        self.runtime.reset()

        self.runtime.set_workflow(

            workflow_name,

        )

        ########################################################

        workflow = Workflow(

            name=workflow_name,

        )

        ########################################################
        # Execute every step
        ########################################################

        for step in plan.steps:

            ####################################################
            # Update runtime
            ####################################################

            self.runtime.set_step(

                step.description,

            )

            self.runtime.set_last_action(

                step.action,

            )

            ####################################################
            # Build execution context
            ####################################################

            context = ExecutionContext(

                workflow=workflow,

                step=step,

                policy=ExecutionPolicy(),

                metadata={},

            )

            ####################################################
            # Execute
            ####################################################

            result = self.engine.execute(

                context,

            )

            ####################################################
            # Store last result
            ####################################################

            self.runtime.update_from_execution(

                step,

                result,

            )

            ####################################################
            # Stop on failure
            ####################################################

            if not result.success:

                return result

        ########################################################
        # Success
        ########################################################

        return ExecutionResult(

            success=True,

            message="Execution plan completed successfully.",

        )