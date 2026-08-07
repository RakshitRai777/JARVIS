from dataclasses import dataclass, field

from ai.agent.goal import Goal


@dataclass(slots=True)
class GoalContext:
    """
    Holds the current goal state used during
    planning and reasoning.
    """

    ############################################################

    current_goal: Goal | None = None

    ############################################################

    all_goals: list[Goal] = field(

        default_factory=list,

    )