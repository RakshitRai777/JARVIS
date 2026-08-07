from ai.project.task import Task
from ai.project.task_ranker import TaskRanker
from ai.project.task_status import TaskStatus


def main():

    tasks = [

        Task(

            title="Low Priority",

            status=TaskStatus.PENDING,

            priority=1,

            progress=0,

        ),

        Task(

            title="Current Task",

            status=TaskStatus.ACTIVE,

            priority=1,

            progress=45,

        ),

        Task(

            title="Important Task",

            status=TaskStatus.PENDING,

            priority=5,

            progress=0,

        ),

        Task(

            title="Completed",

            status=TaskStatus.COMPLETED,

            priority=100,

            progress=100,

        ),

    ]

    ########################################################

    ranker = TaskRanker()

    selected = ranker.rank(

        tasks,

    )

    ########################################################

    print("=" * 60)
    print("TASK RANKER")
    print("=" * 60)

    print()

    if selected:

        print("Selected")

        print(selected.title)

        print()

        print("Status")

        print(selected.status.name)

        print()

        print("Priority")

        print(selected.priority)

        print()

        print("Progress")

        print(selected.progress)

    else:

        print("No candidate task found.")


if __name__ == "__main__":

    main()