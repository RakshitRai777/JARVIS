from dataclasses import dataclass
from typing import Any


@dataclass
class ToolContext:
    """
    Context passed to every tool.

    This gives tools everything they need
    without making them depend directly on
    Brain, Planner, or Runtime.

    Future versions may include:

    • Memory service
    • Logger
    • User profile
    • Conversation
    • Vision
    • Voice
    • Settings
    """

    ############################################################

    # Original user command
    command: str

    ############################################################

    # Current conversation (optional)
    conversation: Any = None

    ############################################################

    # Runtime metadata
    metadata: dict | None = None