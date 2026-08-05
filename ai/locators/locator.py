from abc import ABC, abstractmethod


class Locator(ABC):
    """
    Base class for every locator.

    Examples
    --------

    TextLocator

    TemplateLocator

    AccessibilityLocator

    ObjectLocator
    """

    ############################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the locator.
        """
        ...

    ############################################################

    @abstractmethod
    def locate(
        self,
        vision,
    ):
        """
        Locate something using VisionManager.

        Returns
        -------
        Any result object.
        """
        ...