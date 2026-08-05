from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ScreenRegion:
    """
    Represents a rectangular region on the screen.

    Coordinates are expressed in screen pixels.

    Example
    -------

    ScreenRegion(

        left=100,

        top=200,

        width=300,

        height=120,

    )
    """

    ############################################################

    left: int

    ############################################################

    top: int

    ############################################################

    width: int

    ############################################################

    height: int

    ############################################################

    @property
    def right(self) -> int:

        return self.left + self.width

    ############################################################

    @property
    def bottom(self) -> int:

        return self.top + self.height

    ############################################################

    @property
    def center(self) -> tuple[int, int]:

        return (

            self.left + self.width // 2,

            self.top + self.height // 2,

        )

    ############################################################

    def expand(
        self,
        pixels: int,
    ) -> "ScreenRegion":

        return ScreenRegion(

            left=self.left - pixels,

            top=self.top - pixels,

            width=self.width + pixels * 2,

            height=self.height + pixels * 2,

        )

    ############################################################

    def contains(
        self,
        x: int,
        y: int,
    ) -> bool:

        return (

            self.left <= x <= self.right

            and

            self.top <= y <= self.bottom

        )

    ############################################################

    def as_bbox(
        self,
    ) -> tuple[int, int, int, int]:

        """
        Returns a PIL ImageGrab bbox.
        """

        return (

            self.left,

            self.top,

            self.right,

            self.bottom,

        )

    ############################################################

    def __str__(self):

        return (

            f"Region("

            f"{self.left}, "

            f"{self.top}, "

            f"{self.width}, "

            f"{self.height}"

            f")"

        )