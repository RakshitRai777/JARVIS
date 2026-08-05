from ai.executor.executor import Executor

from ai.planner.execution_plan import (
    ExecutionPlan,
)

from ai.planner.execution_step import (
    ExecutionStep,
)


class PlanExecutor:
    """
    Executes an ExecutionPlan.

    Responsibilities
    ----------------
    • Iterate through plan steps
    • Delegate each step to the Executor
    • Stop execution on failure

    PlanExecutor never executes tools,
    memory or LLM directly.
    """

    ############################################################

    def __init__(self):

        self.executor = Executor()

    ############################################################

    def execute(
        self,
        plan: ExecutionPlan,
        context,
    ):

        result = None

        ########################################################
        # Execute every step
        ########################################################

        for step in plan.steps:

            result = self._execute_step(

                step,

                context,

            )

            ####################################################
            # Stop on failure
            ####################################################

            if result is None:

                break

        ########################################################

        return result

    ############################################################

    def _execute_step(
        self,
        step: ExecutionStep,
        context,
    ):

        return self.executor.execute_step(

            step,

            context,

        )