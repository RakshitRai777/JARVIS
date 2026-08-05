from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    """
    Standard result returned by every tool.

    Attributes
    ----------
    success
        Whether the tool executed successfully.

    message
        Human-readable response for the user.

    data
        Optional structured data returned by the tool.

    error
        Optional error message.
    """

    success: bool

    message: str

    data: Any = None

    error: str | None = None