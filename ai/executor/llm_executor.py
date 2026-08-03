from ai.execution.execution_result import ExecutionResult
from ai.llm_manager import LLMManager


class LLMExecutor:
    """
    Executes LLM requests.
    """

    def __init__(self):

        self.llm = LLMManager()

    def execute(self, context):

        reply = self.llm.generate(
            context.messages
        )

        return ExecutionResult(
            success=True,
            message=reply
        )