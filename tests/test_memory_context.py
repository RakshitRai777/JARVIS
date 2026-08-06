from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType


def main():

    context = MemoryContext(

        query="What is my favourite editor?",

    )

    print("=" * 60)
    print("INITIAL")
    print("=" * 60)

    print("Query :", context.query)
    print("Count :", context.count)

    print()

    memory = Memory(

        memory_type=MemoryType.PROFILE,

        content="Favourite editor is VS Code",

        created_at=datetime.now(),

    )

    context.add(

        memory,

    )

    print("=" * 60)
    print("AFTER ADD")
    print("=" * 60)

    print("Count :", context.count)

    print("Memory :", context.memories[0].content)

    print()

    context.clear()

    print("=" * 60)
    print("AFTER CLEAR")
    print("=" * 60)

    print("Count :", context.count)


if __name__ == "__main__":

    main()