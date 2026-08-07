from enum import Enum, auto


class PlanningStrategyType(Enum):
    """
    High-level planning strategies selected
    after reasoning.
    """

    ############################################################

    DEFAULT = auto()

    ############################################################

    RESUME_GOAL = auto()

    ############################################################

    CREATE_GOAL = auto()

    ############################################################

    STORE_MEMORY = auto()

    ############################################################

    EXECUTE_TOOL = auto()

    ############################################################

    SYSTEM_COMMAND = auto()