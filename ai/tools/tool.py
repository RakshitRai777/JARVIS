from abc import ABC, abstractmethod

from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult


class Tool(ABC):
    """
    Base class for every JARVIS tool.
    """

    ############################################################

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    ############################################################

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    ############################################################

    @abstractmethod
    def match_score(
        self,
        command: str,
    ) -> int:
        """
        Returns how well this tool matches.

        0 = cannot handle

        100 = perfect match
        """
        pass

    ############################################################

    @abstractmethod
    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:
        pass