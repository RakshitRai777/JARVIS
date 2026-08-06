from ai.agent.reflection_context import ReflectionContext
from ai.agent.reflection_manager import ReflectionManager

from ai.execution.execution_result import ExecutionResult

from ai.memory.memory_service import MemoryService


def main():

    ########################################################

    memory = MemoryService()

    memory.clear()

    ########################################################

    context = ReflectionContext(

        execution_result=ExecutionResult(

            success=True,

            message="Completed",

        ),

        objective="Continue FitOS",

        workflow="Planning Workflow",

    )

    ########################################################

    manager = ReflectionManager()

    result = manager.reflect(

        context,

    )

    ########################################################

    print("=" * 60)
    print("REFLECTION MANAGER")
    print("=" * 60)

    print("Reflection")

    print(result.reflection)

    print()

    print("Learning")

    print(result.learning)

    print()

    print("Stored Memories")

    print(memory.count())

    print()

    for item in memory.get_all():

        print("-", item.content)


if __name__ == "__main__":

    main()