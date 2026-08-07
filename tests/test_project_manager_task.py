from ai.project.project_manager import ProjectManager
from ai.project.milestone import Milestone
from ai.project.task import Task
from ai.project.task_status import TaskStatus


def main():

    manager = ProjectManager()

    ########################################################

    project = manager.create_project(

        "FitOS",

        "AI Operating System",

    )

    ########################################################

    milestone = Milestone(

        title="Project Intelligence",

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Completed",

            status=TaskStatus.COMPLETED,

            progress=100,

        )

    )

    ########################################################

    milestone.add_task(

        Task(

            title="Implement ProjectManager",

            status=TaskStatus.ACTIVE,

            progress=40,

            priority=5,

        )

    )

    ########################################################

    manager.add_milestone(

        project,

        milestone,

    )

    ########################################################

    task = manager.get_active_task(

        project,

    )

    ########################################################

    print("=" * 60)
    print("PROJECT MANAGER TASK")
    print("=" * 60)

    print()

    if task:

        print("Selected")

        print(task.title)

        print(task.status.name)

        print(task.progress)

    else:

        print("No task selected.")


if __name__ == "__main__":

    main()