from abc import ABC, abstractmethod

from tools.tool_result import ToolResult


class BaseTool(ABC):
    """
    Base class for every JARVIS tool.
    """

    def __init__(
        self,
        name: str,
        description: str
    ):

        self.name = name

        self.description = description

    @abstractmethod
    def execute(
        self,
        command: str
    ) -> ToolResult:
        """
        Execute the tool.
        """
        pass