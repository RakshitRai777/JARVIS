from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.planner.context_builder import ContextBuilder


def main():

    ########################################################

    memory_context = MemoryContext(

        query="Continue FitOS",

    )

    ########################################################

    memory_context.add(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################

    memory_context.add(

        Memory(

            memory_type=MemoryType.GOAL,

            content="Build AI Operating System",

            created_at=datetime.now(),

        )

    )

    ########################################################

    builder = ContextBuilder()

    ########################################################

    context = builder.build(

        memory_context,

    )

    ########################################################

    print("=" * 60)
    print("CONTEXT BUILDER")
    print("=" * 60)

    print(context)


if __name__ == "__main__":

    main()