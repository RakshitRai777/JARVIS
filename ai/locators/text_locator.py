from ai.locators.locator import Locator
from ai.locators.locator_result import LocatorResult


class TextLocator(Locator):
    """
    Locates text using OCR.
    """

    ############################################################

    def __init__(
        self,
        text: str,
        image_path=None,
    ):

        self.text = text
        self.image_path = image_path

    ############################################################

    @property
    def name(self):

        return "text"

    ############################################################

    def locate(
        self,
        vision,
    ) -> LocatorResult:

        element = vision.find_text(

            self.text,

            image_path=self.image_path,

        )

        ########################################################

        if element is None:

            return LocatorResult(

                success=False,

                error=f"'{self.text}' not found.",

            )

        ########################################################

        return LocatorResult(

            success=True,

            center=element.center,

            region=element.region,

            confidence=element.confidence,

            value=element,

        )