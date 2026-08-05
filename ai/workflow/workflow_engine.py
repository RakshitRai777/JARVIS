import time

from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy

from ai.workflow.workflow import Workflow
from ai.workflow.workflow_result import WorkflowResult


class WorkflowEngine:
    """
    Executes workflows.

    Responsibilities
    ----------------
    • Iterate through workflow steps
    • Build ExecutionContext
    • Delegate execution to ExecutionEngine
    • Aggregate WorkflowResult

    WorkflowEngine intentionally does NOT know
    how actions, verification, retries or recovery
    are implemented.
    """

    ############################################################

    def __init__(self):

        self.execution_engine = ExecutionEngine()

    ############################################################

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:

        start_time = time.perf_counter()

        completed_steps = 0

        ########################################################

        shared_data = {}

        ########################################################

        for step in workflow:

            ####################################################
            # Build Execution Context
            ####################################################

            context = ExecutionContext(

                workflow=workflow,

                step=step,

                policy=ExecutionPolicy(),

                shared_data=shared_data,

            )

            ####################################################
            # Execute Step
            ####################################################

            result = self.execution_engine.execute(

                context

            )

            ####################################################

            if not result.success:

                return WorkflowResult(

                    success=False,

                    completed_steps=completed_steps,

                    total_steps=len(workflow),

                    execution_time=(
                        time.perf_counter()
                        - start_time
                    ),

                    error=result.error
                    or result.message,

                )

            ####################################################

            completed_steps += 1

        ########################################################

        return WorkflowResult(

            success=True,

            completed_steps=completed_steps,

            total_steps=len(workflow),

            execution_time=(
                time.perf_counter()
                - start_time
            ),

        )