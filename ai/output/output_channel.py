from enum import Enum


class OutputChannel(Enum):
    """
    Where JARVIS should deliver the response.
    """

    CONSOLE = "console"

    VOICE = "voice"

    GUI = "gui"

    MOBILE = "mobile"

    API = "api"

    SYSTEM = "system"