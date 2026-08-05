from abc import ABC, abstractmethod

from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult


class Tool(ABC):
    """
    Base class for every JARVIS tool.

    Every tool must implement:

    • can_handle()
    • execute()

    Example
    -------

    CalculatorTool

    OpenChromeTool

    ScreenshotTool
    """

    ############################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human readable name.
        """
        pass

    ############################################################

    @property
    @abstractmethod
    def description(self) -> str:
        """
        What this tool does.
        """
        pass

    ############################################################

    @abstractmethod
    def can_handle(
        self,
        command: str,
    ) -> bool:
        """
        Returns True if this tool can execute
        the given command.
        """
        pass

    ############################################################

    @abstractmethod
    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:
        """
        Execute the tool.
        """
        pass