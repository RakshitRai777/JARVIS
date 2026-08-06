import time

from ai.actions.action_manager import ActionManager
from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep


def main():

    manager = ActionManager()

    workflow = Workflow(

        name="Wait Test",

    )

    step = WorkflowStep(

        action="wait",

        parameters={

            "seconds": 2,

        },

    )

    print()

    print("Starting wait...")

    start = time.perf_counter()

    result = manager.execute(

        workflow,

        step,

    )

    elapsed = time.perf_counter() - start

    print()

    print(result)

    print()

    print(f"Elapsed: {elapsed:.2f}s")


if __name__ == "__main__":

    main()