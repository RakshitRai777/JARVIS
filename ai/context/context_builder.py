from runtime.runtime import runtime

from ai.context.context import Context
from ai.context.system_prompt import SYSTEM_PROMPT


class ContextBuilder:
    """
    Builds the base context for the LLM.

    Responsibilities
    ----------------
    • System Prompt
    • Conversation History
    • Relevant Memories
    • Metadata

    NOTE
    ----
    Web retrieval is NOT handled here.
    RAG builds its own prompt separately.
    """

    ############################################################

    def build(
        self,
        conversation,
        original_query="",
        search_query="",
        metadata=None
    ):

        context = Context(
            system_prompt=SYSTEM_PROMPT,
            original_query=original_query,
            search_query=search_query,
        )
        context.original_query = original_query

        context.search_query = search_query

        context.metadata = metadata or {}

        ########################################################
        # System Prompt
        ########################################################

        context.add_message(
            "system",
            context.system_prompt
        )

        ########################################################
        # Retrieve Relevant Memories
        ########################################################

        memory_service = runtime.services.get("memory")

        if memory_service is not None:

            latest_message = ""

            history = conversation.history()

            if history:

                latest_message = history[-1].content

            memories = memory_service.find(
                latest_message
            )

            context.memories = memories

            if memories:

                memory_text = "\n".join(

                    f"- {memory.content}"

                    for memory in memories

                )

                context.add_message(

                    "system",

                    (
                        "Relevant memories about the user:\n"
                        f"{memory_text}"
                    )

                )

        ########################################################
        # Conversation History
        ########################################################

        for message in conversation.history():

            context.add_message(

                message.role,

                message.content

            )

        ########################################################

        return context