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

    manager.activate(project)

    ########################################################

    milestone = Milestone(

        title="Project Intelligence",

    )

    milestone.add_task(

        Task(

            title="ProjectManager",

            status=TaskStatus.COMPLETED,

            progress=100,

        )

    )

    milestone.add_task(

        Task(

            title="ProjectContext",

            status=TaskStatus.ACTIVE,

            progress=50,

        )

    )

    ########################################################

    manager.add_milestone(

        project,

        milestone,

    )

    ########################################################

    print("=" * 60)
    print("PROJECT MANAGER")
    print("=" * 60)

    print("Project")

    print(project.name)

    print()

    print("Status")

    print(project.status.name)

    print()

    print("Progress")

    print(project.progress)

    print()

    print("Milestones")

    print(len(manager.get_milestones(project)))

    print()

    print("Active Project")

    active = manager.get_active_project()

    print(active.name if active else "None")


if __name__ == "__main__":

    main()