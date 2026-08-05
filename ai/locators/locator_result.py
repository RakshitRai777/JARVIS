from dataclasses import dataclass

from ai.geometry.screen_region import ScreenRegion


@dataclass(slots=True)
class LocatorResult:
    """
    Unified result returned by every locator.
    """

    success: bool

    center: tuple[int, int] | None = None

    region: ScreenRegion | None = None

    confidence: float = 0.0

    value: object | None = None

    error: str | None = None

    ############################################################

    def __bool__(self):

        return self.success