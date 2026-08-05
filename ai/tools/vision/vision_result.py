from dataclasses import dataclass, field

from ai.tools.vision.ocr_element import OCRElement


@dataclass
class VisionResult:
    """
    Result produced by the Vision Engine.
    """

    ############################################################

    success: bool

    ############################################################

    raw_text: str = ""

    ############################################################

    cleaned_text: str = ""

    ############################################################

    elements: list[OCRElement] = field(

        default_factory=list

    )

    ############################################################

    screenshot_path: str = ""

    ############################################################

    error: str = ""

    ############################################################

    metadata: dict = field(

        default_factory=dict

    )