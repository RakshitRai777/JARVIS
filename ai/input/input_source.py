from enum import Enum


class InputSource(Enum):
    """
    Where the request came from.

    The Brain should never care about this.

    Only the Input Layer knows.
    """

    KEYBOARD = "keyboard"

    VOICE = "voice"

    API = "api"

    GUI = "gui"

    MOBILE = "mobile"

    VISION = "vision"

    SYSTEM = "system"