from pathlib import Path

from ai.locators.locator import Locator
from ai.locators.locator_result import LocatorResult


class TemplateLocator(Locator):
    """
    Locates a template using VisionManager.
    """

    ############################################################

    def __init__(
        self,
        template: str | Path,
        threshold: float = 0.75,
        image_path: str | Path | None = None,
    ):

        self.template = template
        self.threshold = threshold
        self.image_path = image_path

    ############################################################

    @property
    def name(self):

        return "template"

    ############################################################

    def locate(
        self,
        vision,
    ) -> LocatorResult:

        result = vision.find_template(

            template=self.template,

            image_path=self.image_path,

            threshold=self.threshold,

        )

        ########################################################

        if not result:

            return LocatorResult(

                success=False,

                error=result.error,

            )

        ########################################################

        match = result.best_match

        ########################################################

        return LocatorResult(

            success=True,

            center=match.center,

            region=match.region,

            confidence=match.confidence,

            value=match,

        )