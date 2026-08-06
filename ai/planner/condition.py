from dataclasses import dataclass


@dataclass
class Condition:
    """
    Represents a condition that determines
    whether an execution step should run.

    Future
    ------
    • Runtime variables
    • Verification results
    • Expressions
    • OCR conditions
    • Vision conditions
    """

    ############################################################

    left: str

    operator: str

    right: str