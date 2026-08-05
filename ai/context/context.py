from dataclasses import dataclass, field


@dataclass
class Context:
    """
    Complete context passed throughout the AI pipeline.

    Contains
    --------
    • Original user query
    • Normalized search query
    • System prompt
    • Conversation history
    • Relevant memories
    • Runtime metadata
    """

    ##########################################################
    # Queries
    ##########################################################

    original_query: str = ""

    search_query: str = ""

    ##########################################################
    # Prompt
    ##########################################################

    system_prompt: str = ""

    ##########################################################
    # Conversation
    ##########################################################

    messages: list = field(default_factory=list)

    ##########################################################
    # Memories
    ##########################################################

    memories: list = field(default_factory=list)

    ##########################################################
    # Runtime
    ##########################################################

    metadata: dict = field(default_factory=dict)

    ##########################################################

    def add_message(

        self,

        role: str,

        content: str

    ) -> None:

        self.messages.append(

            {

                "role": role,

                "content": content

            }

        )