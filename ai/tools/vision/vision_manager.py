import time

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
        # Start Profiling
        ########################################################

        start_total = time.perf_counter()

        ########################################################
        # Capture screenshot if needed
        ########################################################

        screenshot = image_path

        capture_start = time.perf_counter()

        if screenshot is None:

            screenshot = self.desktop.take_screenshot()

        capture_time = time.perf_counter() - capture_start

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

            ocr_start = time.perf_counter()

            elements = self.ocr.extract_elements(

                screenshot

            )

            ocr_time = time.perf_counter() - ocr_start

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

            pre_start = time.perf_counter()

            cleaned_text = self.preprocessor.preprocess(

                raw_text

            )

            pre_time = time.perf_counter() - pre_start

            ####################################################
            # Total Time
            ####################################################

            total_time = time.perf_counter() - start_total

            print()
            print("=" * 60)
            print("VISION PROFILING")
            print("=" * 60)
            print(f"Screenshot : {capture_time:.2f}s")
            print(f"OCR        : {ocr_time:.2f}s")
            print(f"Preprocess : {pre_time:.2f}s")
            print("-" * 60)
            print(f"TOTAL      : {total_time:.2f}s")
            print("=" * 60)
            print()

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