import ast
import operator

from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult


class CalculatorTool(Tool):
    """
    Safe calculator tool.

    Supports:

    +  -  *  /  **  %  //

    Examples
    --------
    Calculate 25*16

    What is 81/9?

    9+7*3
    """

    ############################################################

    @property
    def name(self) -> str:

        return "Calculator"

    ############################################################

    @property
    def description(self) -> str:

        return "Performs mathematical calculations."

    ############################################################

    def can_handle(
        self,
        command: str,
    ) -> bool:

        text = command.lower()

        keywords = [

            "calculate",
            "what is",
            "solve",

        ]

        if any(k in text for k in keywords):

            return True

        operators = "+-*/%"

        return any(op in command for op in operators)

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        expression = self._extract_expression(
            context.command
        )

        if not expression:

            return ToolResult(

                success=False,

                message="I couldn't find a mathematical expression.",

            )

        try:

            result = self._safe_eval(
                expression
            )

            return ToolResult(

                success=True,

                message=f"The answer is {result}.",

                data=result,

            )

        except Exception:

            return ToolResult(

                success=False,

                message="Invalid mathematical expression.",

            )

    ############################################################

    def _extract_expression(
        self,
        text: str,
    ) -> str:

        lower = text.lower()

        prefixes = [

            "calculate",
            "what is",
            "solve",

        ]

        for prefix in prefixes:

            if lower.startswith(prefix):

                text = text[len(prefix):]

                break

        return text.strip(" ?")

    ############################################################

    def _safe_eval(
        self,
        expression: str,
    ):

        operators = {

            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.FloorDiv: operator.floordiv,
            ast.USub: operator.neg,

        }

        def evaluate(node):

            if isinstance(node, ast.Constant):

                return node.value

            if isinstance(node, ast.BinOp):

                return operators[type(node.op)](

                    evaluate(node.left),

                    evaluate(node.right),

                )

            if isinstance(node, ast.UnaryOp):

                return operators[type(node.op)](

                    evaluate(node.operand)

                )

            raise TypeError(
                "Unsupported expression."
            )

        tree = ast.parse(
            expression,
            mode="eval",
        )

        return evaluate(tree.body)