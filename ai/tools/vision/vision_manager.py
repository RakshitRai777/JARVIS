from ai.tools.desktop.desktop_manager import DesktopManager

from ai.tools.vision.ocr_manager import OCRManager
from ai.tools.vision.vision_result import VisionResult


class VisionManager:
    """
    Coordinates the Vision pipeline.

    Responsibilities
    ----------------
    • Capture screenshot
    • Perform OCR
    • Return structured result
    """

    ############################################################

    def __init__(self):

        self.desktop = DesktopManager()

        self.ocr = OCRManager()

    ############################################################

    def read_screen(
        self,
    ) -> VisionResult:

        ########################################################
        # Capture screenshot
        ########################################################

        screenshot = self.desktop.take_screenshot()

        if screenshot is None:

            return VisionResult(

                success=False,

                error="Failed to capture screenshot.",

            )

        ########################################################
        # OCR
        ########################################################

        try:

            text = self.ocr.extract_text(

                screenshot

            )

            return VisionResult(

                success=True,

                text=text,

                screenshot_path=screenshot,

            )

        except Exception as e:

            return VisionResult(

                success=False,

                screenshot_path=screenshot,

                error=str(e),

            )