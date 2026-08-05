from abc import ABC, abstractmethod

from ai.actions.action_context import ActionContext
from ai.actions.action_result import ActionResult


class Action(ABC):
    """
    Base class for every executable workflow action.

    Unlike Tools, Actions do not perform any
    natural-language understanding.

    They execute structured workflow steps.
    """

    ############################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique action name.

        Example:
            click_text
            type_text
            press_key
        """
        pass

    ############################################################

    @abstractmethod
    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:
        """
        Execute the action.
        """
        pass