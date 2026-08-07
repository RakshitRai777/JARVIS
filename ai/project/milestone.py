from dataclasses import dataclass, field
from datetime import datetime

from ai.project.task import Task


@dataclass(slots=True)
class Milestone:
    """
    Represents a major phase of a project.

    A milestone contains multiple tasks that
    together accomplish a significant objective.
    """

    ############################################################

    title: str = ""

    ############################################################

    description: str = ""

    ############################################################

    tasks: list[Task] = field(default_factory=list)

    ############################################################

    created_at: datetime = field(
        default_factory=datetime.now,
    )

    ############################################################

    @property
    def progress(self) -> float:
        """
        Returns the average progress of all tasks.
        """

        if not self.tasks:
            return 0.0

        return sum(task.progress for task in self.tasks) / len(self.tasks)

    ############################################################

    @property
    def completed(self) -> bool:
        """
        Returns True if every task is completed.
        """

        return (
            len(self.tasks) > 0
            and
            all(task.progress >= 100.0 for task in self.tasks)
        )

    ############################################################

    def add_task(
        self,
        task: Task,
    ) -> None:

        self.tasks.append(task)