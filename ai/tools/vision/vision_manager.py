from ai.tools.desktop.desktop_manager import DesktopManager

from ai.tools.vision.ocr_manager import OCRManager
from ai.tools.vision.vision_preprocessor import VisionPreprocessor
from ai.tools.vision.vision_result import VisionResult


class VisionManager:
    """
    Central Vision Engine.

    Responsibilities
    ----------------
    • Capture screenshot
    • Perform OCR
    • Preprocess OCR
    • Preserve OCR metadata
    • Return structured VisionResult
    """

    ############################################################

    def __init__(self):

        self.desktop = DesktopManager()

        self.ocr = OCRManager()

        self.preprocessor = VisionPreprocessor()

    ############################################################

    def read_screen(
        self,
        image_path: str | None = None,
    ) -> VisionResult:
        """
        Reads text from the current screen or
        from an existing image.

        Parameters
        ----------
        image_path:
            Optional image path. If omitted,
            a new screenshot is captured.
        """

        ########################################################
        # Capture screenshot if needed
        ########################################################

        screenshot = image_path

        if screenshot is None:

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

            ####################################################
            # Extract OCR elements
            ####################################################

            elements = self.ocr.extract_elements(

                screenshot

            )

            ####################################################
            # Build raw text
            ####################################################

            raw_text = "\n".join(

                element.text

                for element in elements

            )

            ####################################################
            # Preprocess OCR
            ####################################################

            cleaned_text = self.preprocessor.preprocess(

                raw_text

            )

            ####################################################
            # Build VisionResult
            ####################################################

            return VisionResult(

                success=True,

                raw_text=raw_text,

                cleaned_text=cleaned_text,

                elements=elements,

                screenshot_path=screenshot,

            )

        except Exception as e:

            return VisionResult(

                success=False,

                screenshot_path=screenshot,

                error=str(e),

            )