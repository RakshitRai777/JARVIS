from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy
from ai.execution.execution_result import ExecutionResult

from ai.workflow.workflow import Workflow


class PlanExecutor:
    """
    Executes an entire ExecutionPlan.

    Responsibilities
    ----------------
    • Execute every step in order
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

    ############################################################

    def execute(
        self,
        plan,
        workflow_name: str = "Execution Plan",
    ) -> ExecutionResult:

        workflow = Workflow(

            name=workflow_name,

        )

        ########################################################

        for step in plan.steps:

            context = ExecutionContext(

                workflow=workflow,

                step=step,

                policy=ExecutionPolicy(),

                metadata={},

            )

            result = self.engine.execute(

                context,

            )

            ####################################################

            if not result.success:

                return result

        ########################################################

        return ExecutionResult(

            success=True,

            message="Execution plan completed successfully.",

        )