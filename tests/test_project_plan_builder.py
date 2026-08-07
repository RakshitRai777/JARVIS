from ai.project.task import Task
from ai.project.task_status import TaskStatus

from ai.planner.project_plan_builder import (
    ProjectPlanBuilder,
)


def main():

    task = Task(

        title="Implement ProjectManager",

        status=TaskStatus.ACTIVE,

        progress=40,

    )

    ########################################################

    builder = ProjectPlanBuilder()

    plan = builder.build(

        task,

    )

    ########################################################

    print("=" * 60)
    print("PROJECT PLAN BUILDER")
    print("=" * 60)

    print()

    print("Task")

    print(task.title)

    print()

    print("Execution Steps")

    print()

    for index, step in enumerate(

        plan.steps,

        start=1,

    ):

        print(

            f"{index}.",

            step.description,

        )


if __name__ == "__main__":

    main()