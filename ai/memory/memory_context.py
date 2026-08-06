from dataclasses import dataclass, field

from ai.memory.memory import Memory


@dataclass(slots=True)
class MemoryContext:
    """
    Memories supplied to the planner
    for the current request.
    """

    ############################################################

    query: str = ""

    ############################################################

    memories: list[Memory] = field(

        default_factory=list,

    )

    ############################################################

    def add(
        self,
        memory: Memory,
    ) -> None:

        self.memories.append(

            memory,

        )

    ############################################################

    @property
    def count(
        self,
    ) -> int:

        return len(

            self.memories,

        )

    ############################################################

    def clear(
        self,
    ) -> None:

        self.memories.clear()