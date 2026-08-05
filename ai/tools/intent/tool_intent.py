from enum import Enum


class ToolIntent(Enum):
    """
    High-level tool categories.

    The Planner only needs to know
    whether a request should be handled
    by the Tool System.

    The ToolExecutor later chooses
    the exact tool.
    """

    NONE = "none"

    SYSTEM = "system"

    BROWSER = "browser"

    FILESYSTEM = "filesystem"

    CALCULATOR = "calculator"

    MEDIA = "media"

    DEVELOPMENT = "development"

    UTILITY = "utility"