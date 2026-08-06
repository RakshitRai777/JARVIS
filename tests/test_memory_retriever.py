from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_retriever import MemoryRetriever
from ai.memory.memory_type import MemoryType


def main():

    retriever = MemoryRetriever()

    ########################################################
    # Clean memory
    ########################################################

    retriever.memory_service.clear()

    ########################################################
    # Add memories
    ########################################################

    retriever.memory_service.remember(

        Memory(

            memory_type=MemoryType.PROFILE,

            content="My favourite editor is VS Code",

            created_at=datetime.now(),

        )

    )

    retriever.memory_service.remember(

        Memory(

            memory_type=MemoryType.PROFILE,

            content="I like Python",

            created_at=datetime.now(),

        )

    )

    ########################################################

    context = retriever.retrieve(

        "What is my favourite editor?"

    )

    ########################################################

    print("=" * 60)
    print("MEMORY RETRIEVAL")
    print("=" * 60)

    print("Query :", context.query)

    print("Count :", context.count)

    print()

    for memory in context.memories:

        print("-", memory.content)


if __name__ == "__main__":

    main()