from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.planner.planning_context import PlanningContext


def main():

    ########################################################

    memory_context = MemoryContext(

        query="Continue FitOS",

    )

    memory_context.add(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################

    context = PlanningContext(

        command="Continue FitOS",

        memory_context=memory_context,

    )

    ########################################################

    print("=" * 60)
    print("PLANNING CONTEXT")
    print("=" * 60)

    print("Command :", context.command)

    print("Memory Count :", context.memory_context.count)

    print()

    for memory in context.memory_context.memories:

        print("-", memory.content)


if __name__ == "__main__":

    main()