from dataclasses import dataclass


@dataclass
class ToolResult:
    """
    Result returned by every tool.
    """

    success: bool

    message: str

    data: dict | None = None