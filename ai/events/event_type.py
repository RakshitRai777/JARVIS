from enum import Enum


class EventType(Enum):
    """
    High-level events that flow through JARVIS.
    """

    USER_INPUT = "user_input"

    SYSTEM = "system"

    TOOL = "tool"

    MEMORY = "memory"

    WEB = "web"

    VISION = "vision"

    VOICE = "voice"

    TIMER = "timer"

    NOTIFICATION = "notification"