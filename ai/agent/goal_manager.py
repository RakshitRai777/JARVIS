from datetime import datetime

from ai.agent.goal import Goal
from ai.agent.goal_status import GoalStatus


class GoalManager:
    """
    Manages long-running agent goals.
    """

    ############################################################

    def __init__(self):

        self._goals: list[Goal] = []

    ############################################################

    def create_goal(
        self,
        title: str,
        description: str = "",
    ) -> Goal:

        goal = Goal(

            title=title,

            description=description,

        )

        self._goals.append(

            goal,

        )

        return goal

    ############################################################

    def get_goals(
        self,
    ) -> list[Goal]:

        return self._goals

    ############################################################

    def find_goal(
            self,
            title: str,
    ) -> Goal | None:
        for goal in self._goals:
            if goal.title.lower() == title.lower():
                return goal
        return None

    ############################################################

    def get_active_goal(
            self,
    ) -> Goal | None:
        for goal in self._goals:
            if goal.status == GoalStatus.ACTIVE:
                return goal
        return None

    ############################################################

    def remove_goal(
        self,
        goal:Goal,
    ) -> bool:
        if goal in self._goals:
            self._goals.remove(goal,)
            return True
        return False

    ############################################################

    def activate(
        self,
        goal: Goal,
    ) -> None:

        goal.status = GoalStatus.ACTIVE

    ############################################################

    def pause(
        self,
        goal: Goal,
    ) -> None:

        goal.status = GoalStatus.PAUSED

    ############################################################

    def complete(
        self,
        goal: Goal,
    ) -> None:

        goal.status = GoalStatus.COMPLETED

        goal.progress = 100.0

        goal.completed_at = datetime.now()

    ############################################################

    def fail(
        self,
        goal: Goal,
    ) -> None:

        goal.status = GoalStatus.FAILED

    ############################################################

    def cancel(
        self,
        goal: Goal,
    ) -> None:

        goal.status = GoalStatus.CANCELLED

    ############################################################

    def update_progress(
        self,
        goal: Goal,
        progress: float,
    ) -> None:

        progress = max(

            0.0,

            min(

                100.0,

                progress,

            ),

        )

        goal.progress = progress

        if progress >= 100.0:

            self.complete(

                goal,

            )