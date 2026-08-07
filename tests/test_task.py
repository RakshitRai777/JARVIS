from ai.project.task import Task
from ai.project.task_status import TaskStatus


def main():

    ########################################################

    print("=" * 60)
    print("DEFAULT TASK")
    print("=" * 60)

    task = Task()

    print(task)

    ########################################################

    print()

    print("=" * 60)
    print("CUSTOM TASK")
    print("=" * 60)

    task = Task(

        title="Implement ProjectManager",

        description="Create the ProjectManager class.",

        status=TaskStatus.ACTIVE,

        progress=35.0,

        priority=1,

    )

    print("Title       :", task.title)

    print("Description :", task.description)

    print("Status      :", task.status.name)

    print("Progress    :", task.progress)

    print("Priority    :", task.priority)

    print("Created     :", task.created_at)

    print("Completed   :", task.completed_at)


if __name__ == "__main__":

    main()