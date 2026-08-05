import ast
import operator
import re

from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult


class CalculatorTool(Tool):
    """
    Safe calculator tool.
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

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        ########################################################
        # Explicit calculator commands
        ########################################################

        keywords = [

            "calculate",

            "solve",

            "compute",

            "evaluate",

        ]

        if any(text.startswith(keyword) for keyword in keywords):

            return 100

        ########################################################
        # "What is" only if followed by mathematics
        ########################################################

        if text.startswith("what is"):

            expression = self._extract_expression(command)

            if self._looks_like_math(expression):

                return 100

        ########################################################
        # Pure mathematical expression
        ########################################################

        expression = self._extract_expression(command)

        if self._looks_like_math(expression):

            return 90

        ########################################################

        return 0

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

            "compute",

            "evaluate",

        ]

        for prefix in prefixes:

            if lower.startswith(prefix):

                text = text[len(prefix):]

                break

        return text.strip(" ?")

    ############################################################

    def _looks_like_math(
        self,
        expression: str,
    ) -> bool:

        expression = expression.strip()

        if not expression:

            return False

        pattern = r"^[0-9\s+\-*/%.()]+$"

        if not re.fullmatch(pattern, expression):

            return False

        return any(ch.isdigit() for ch in expression)

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