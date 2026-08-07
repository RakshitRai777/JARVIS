from ai.project.milestone import Milestone
from ai.project.task import Task
from ai.project.task_ranker import TaskRanker
from ai.project.task_status import TaskStatus


class TaskSelector:
    """
    Selects the next task to execute.

    Responsibilities
    ----------------
    • Collect candidate tasks
    • Delegate ranking to TaskRanker
    """

    ############################################################

    def __init__(self):

        self.ranker = TaskRanker()

    ############################################################

    def select(
        self,
        milestones: list[Milestone],
    ) -> Task | None:

        ########################################################
        # Collect candidate tasks
        ########################################################

        candidates: list[Task] = []

        for milestone in milestones:

            for task in milestone.tasks:

                if task.status != TaskStatus.COMPLETED:

                    candidates.append(task)

        ########################################################
        # Rank candidates
        ########################################################

        return self.ranker.rank(

            candidates,

        )