from datetime import datetime

from runtime.runtime import runtime

from ai.execution.execution_result import ExecutionResult

from ai.memory.memory import Memory
from ai.memory.memory_type import MemoryType


class MemoryExecutor:

    """
    Executes memory requests.
    """

    def execute(
        self,
        context
    ):

        memory_service = runtime.services.get(
            "memory"
        )

        user_message = context.messages[-1]["content"]

        memory = Memory(
            memory_type=MemoryType.WORKING,
            content=user_message,
            created_at=datetime.now()
        )

        memory_service.remember(memory)

        return ExecutionResult(
            success=True,
            message="I will remember that."
        )