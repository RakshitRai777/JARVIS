from dataclasses import dataclass, field


@dataclass
class Context:
    """
    Complete context sent to the LLM.
    """

    system_prompt: str

    messages: list = field(default_factory=list)

    memories: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    def add_message(
        self,
        role: str,
        content: str
    ):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )