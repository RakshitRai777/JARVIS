from dataclasses import dataclass

from ai.geometry.screen_region import ScreenRegion


@dataclass(slots=True)
class TemplateMatch:
    """
    Represents a single template match.

    Example
    -------

    Chrome icon

    Settings button

    Send button
    """

    ############################################################

    region: ScreenRegion

    ############################################################

    confidence: float

    ############################################################

    @property
    def center(self) -> tuple[int, int]:

        return self.region.center

    ############################################################

    @property
    def left(self) -> int:

        return self.region.left

    ############################################################

    @property
    def top(self) -> int:

        return self.region.top

    ############################################################

    @property
    def width(self) -> int:

        return self.region.width

    ############################################################

    @property
    def height(self) -> int:

        return self.region.height

    ############################################################

    def __str__(self):

        return (

            f"TemplateMatch("

            f"confidence={self.confidence:.3f}, "

            f"region={self.region}"

            f")"

        )