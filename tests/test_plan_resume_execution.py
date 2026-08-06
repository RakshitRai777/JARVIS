from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_policy import ExecutionPolicy
from ai.execution.execution_result import ExecutionResult
from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.plan_executor import PlanExecutor

from ai.planner.execution_plan import ExecutionPlan
from ai.planner.execution_step import ExecutionStep
from ai.actions.action_result import ActionResult
from ai.workflow.workflow import Workflow


############################################################
# Fake Action Manager
############################################################

class FakeActionManager:

    def execute(
        self,
        context,
    ):

        print(f"Executing -> {context.step.description}")

        return ActionResult(

            success=True,

            message="Success",

        )


############################################################

def make_step(name: str):

    return ExecutionStep(

        action="tool",

        parameters={

            "command": name,

        },

        description=name,

    )


############################################################

def main():

    ########################################################
    # Build execution plan
    ########################################################

    plan = ExecutionPlan(

        steps=[

            make_step("Step 1"),

            make_step("Step 2"),

            make_step("Step 3"),

            make_step("Step 4"),

            make_step("Step 5"),

        ]

    )

    ########################################################

    executor = PlanExecutor()

    ########################################################
    # Replace ActionManager
    ########################################################

    executor.engine.action_manager = FakeActionManager()

    ########################################################
    # Save checkpoint
    ########################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Resume Workflow",

        current_step=2,

        total_steps=5,

    )

    executor.resume_engine.save_checkpoint(

        checkpoint,

    )

    ########################################################

    print("=" * 60)
    print("RESUME EXECUTION")
    print("=" * 60)

    ########################################################

    result = executor.execute(

        plan,

        workflow_name="Resume Workflow",

    )

    ########################################################

    print()
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(result)


if __name__ == "__main__":

    main()