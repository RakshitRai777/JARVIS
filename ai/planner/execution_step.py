from dataclasses import dataclass


@dataclass
class ExecutionStep:
    """
    Represents one executable step
    produced by the Planner.
    """

    ############################################################

    action: str

    ############################################################

    parameters: dict

    ############################################################

    description: str