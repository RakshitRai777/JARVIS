from ai.memory.memory_context import MemoryContext


class ContextBuilder:
    """
    Builds structured planning context from retrieved memories.

    Future Responsibilities
    -----------------------
    • Summarize memories
    • Rank memories
    • Merge duplicate information
    • Include runtime state
    • Include active goals
    • Include execution history
    """

    ############################################################

    def build(
        self,
        memory_context: MemoryContext,
    ) -> str:

        ########################################################
        # No memories
        ########################################################

        if memory_context.count == 0:

            return "No relevant memories."

        ########################################################

        lines = [

            "Relevant Memories:",

        ]

        ########################################################

        for memory in memory_context.memories:

            lines.append(

                f"- {memory.content}"

            )

        ########################################################

        return "\n".join(

            lines,

        )