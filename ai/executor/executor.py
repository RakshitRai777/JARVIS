from ai.execution.execution_result import ExecutionResult

from ai.executor.llm_executor import LLMExecutor
from ai.executor.memory_executor import MemoryExecutor
from ai.executor.system_executor import SystemExecutor
from ai.executor.tool_executor import ToolExecutor

from ai.planner.planner_action import PlannerAction


class Executor:
    """
    Central execution router.

    Receives a Planner Decision and forwards it
    to the appropriate executor.
    """

    def __init__(self):

        self.llm_executor = LLMExecutor()

        self.memory_executor = MemoryExecutor()

        self.tool_executor = ToolExecutor()

        self.system_executor = SystemExecutor()

    def execute(
        self,
        decision,
        context
    ) -> ExecutionResult:

        if decision.action == PlannerAction.LLM:

            return self.llm_executor.execute(context)

        if decision.action == PlannerAction.MEMORY:

            return self.memory_executor.execute(context)

        if decision.action == PlannerAction.TOOL:

            return self.tool_executor.execute(context)

        if decision.action == PlannerAction.SYSTEM:

            return self.system_executor.execute(context)

        return ExecutionResult(
            success=False,
            message=f"Unknown planner action: {decision.action}"
        )