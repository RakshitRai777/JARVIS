from ai.planner.condition import Condition
from ai.runtime.runtime_variables import RuntimeVariables


class ConditionEvaluator:
    """
    Evaluates execution conditions using RuntimeVariables.

    Supported Operators
    -------------------
    ==
    !=

    Future
    ------
    >
    <
    >=
    <=
    contains
    startswith
    endswith
    regex
    exists
    """

    ############################################################

    def __init__(
        self,
        variables: RuntimeVariables,
    ):

        self.variables = variables

    ############################################################

    def evaluate(
        self,
        condition: Condition,
    ) -> bool:

        ########################################################
        # Read runtime value
        ########################################################

        left = self.variables.get(

            condition.left,

        )

        right = condition.right

        ########################################################

        if condition.operator == "==":

            return left == right

        ########################################################

        if condition.operator == "!=":

            return left != right

        ########################################################

        raise ValueError(

            f"Unsupported operator: {condition.operator}"

        )