from ai.project.task import Task
from ai.project.task_status import TaskStatus


class TaskRanker:
    """
    Ranks candidate tasks and selects the
    best one for execution.

    Current Strategy
    ----------------
    1. Ignore completed tasks
    2. Prefer ACTIVE tasks
    3. Higher priority wins
    4. Higher progress wins
    """

    ############################################################

    def rank(
        self,
        tasks: list[Task],
    ) -> Task | None:

        ########################################################
        # Remove completed tasks
        ########################################################

        candidates = [

            task

            for task in tasks

            if task.status != TaskStatus.COMPLETED

        ]

        ########################################################

        if not candidates:

            return None

        ########################################################

        candidates.sort(

            key=lambda task: (

                task.status != TaskStatus.ACTIVE,

                -task.priority,

                -task.progress,

            ),

        )

        ########################################################

        return candidates[0]