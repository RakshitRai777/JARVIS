from ai.project.milestone import Milestone
from ai.project.task import Task
from ai.project.task_selector import TaskSelector
from ai.project.task_status import TaskStatus


def main():

    milestone = Milestone(

        title="Project Intelligence",

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Completed Task",

            status=TaskStatus.COMPLETED,

            priority=5,

            progress=100,

        )

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Important Pending",

            status=TaskStatus.PENDING,

            priority=5,

            progress=0,

        )

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Current Task",

            status=TaskStatus.ACTIVE,

            priority=1,

            progress=40,

        )

    )

    ########################################################

    selector = TaskSelector()

    task = selector.select(

        [milestone],

    )

    ########################################################

    print("=" * 60)
    print("TASK SELECTOR")
    print("=" * 60)

    print()

    if task:

        print("Selected")

        print(task.title)

        print()

        print("Status")

        print(task.status.name)

        print()

        print("Priority")

        print(task.priority)

        print()

        print("Progress")

        print(task.progress)

    else:

        print("No task selected.")


if __name__ == "__main__":

    main()