from dataclasses import dataclass


@dataclass(slots=True)
class OCRElement:
    """
    Represents one OCR detection.

    Attributes
    ----------
    text
        Recognized text.

    confidence
        OCR confidence score.

    bbox
        Bounding box returned by EasyOCR.

        Format:
            [
                [x1, y1],
                [x2, y2],
                [x3, y3],
                [x4, y4]
            ]
    """

    ############################################################

    text: str

    confidence: float

    bbox: list

    ############################################################
    # Geometry
    ############################################################

    @property
    def left(self) -> int:

        return int(min(point[0] for point in self.bbox))

    ############################################################

    @property
    def right(self) -> int:

        return int(max(point[0] for point in self.bbox))

    ############################################################

    @property
    def top(self) -> int:

        return int(min(point[1] for point in self.bbox))

    ############################################################

    @property
    def bottom(self) -> int:

        return int(max(point[1] for point in self.bbox))

    ############################################################

    @property
    def width(self) -> int:

        return self.right - self.left

    ############################################################

    @property
    def height(self) -> int:

        return self.bottom - self.top

    ############################################################

    @property
    def center(self) -> tuple[int, int]:

        return (

            self.left + self.width // 2,

            self.top + self.height // 2,

        )

    ############################################################

    @property
    def area(self) -> int:

        return self.width * self.height

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

    def __str__(self) -> str:

        return (

            f"OCRElement("

            f"text='{self.text}', "

            f"confidence={self.confidence:.2f}, "

            f"center={self.center}"

            f")"

        )