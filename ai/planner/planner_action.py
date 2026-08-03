from enum import Enum


class PlannerAction(Enum):
    """
    All actions that the Planner can request.
    """

    LLM = "LLM"

    TOOL = "TOOL"

    MEMORY = "MEMORY"

    SYSTEM = "SYSTEM"