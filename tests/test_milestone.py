from ai.project.milestone import Milestone
from ai.project.task import Task
from ai.project.task_status import TaskStatus


def main():

    ########################################################

    milestone = Milestone(

        title="Project Intelligence",

        description="Build the Project subsystem.",

    )

    ########################################################

    milestone.add_task(

        Task(

            title="ProjectStatus",

            status=TaskStatus.COMPLETED,

            progress=100.0,

        )

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Project",

            status=TaskStatus.COMPLETED,

            progress=100.0,

        )

    )

    ########################################################

    milestone.add_task(

        Task(

            title="ProjectManager",

            status=TaskStatus.ACTIVE,

            progress=40.0,

        )

    )

    ########################################################

    print("=" * 60)
    print("MILESTONE")
    print("=" * 60)

    print("Title       :", milestone.title)

    print("Description :", milestone.description)

    print("Tasks       :", len(milestone.tasks))

    print("Progress    :", milestone.progress)

    print("Completed   :", milestone.completed)

    print()

    print("Task List")

    print("-" * 60)

    for task in milestone.tasks:

        print(

            f"{task.title:20}",

            task.status.name,

            f"{task.progress:.0f}%",

        )


if __name__ == "__main__":

    main()