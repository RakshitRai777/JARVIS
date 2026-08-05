import time

from ai.geometry.screen_region import ScreenRegion

from ai.tools.desktop.desktop_manager import DesktopManager

from ai.tools.vision.ocr_manager import OCRManager
from ai.tools.vision.vision_preprocessor import VisionPreprocessor
from ai.tools.vision.vision_result import VisionResult


class VisionManager:
    """
    Central Vision Engine.

    Responsibilities
    ----------------
    • Capture screenshots
    • Capture region screenshots
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
    # Internal OCR Pipeline
    ############################################################

    def _process_image(
        self,
        screenshot: str,
    ) -> VisionResult:

        start_total = time.perf_counter()

        try:

            ####################################################
            # OCR
            ####################################################

            ocr_start = time.perf_counter()

            elements = self.ocr.extract_elements(

                screenshot

            )

            ocr_time = time.perf_counter() - ocr_start

            ####################################################
            # Build Raw Text
            ####################################################

            raw_text = "\n".join(

                element.text

                for element in elements

            )

            ####################################################
            # Preprocess
            ####################################################

            pre_start = time.perf_counter()

            cleaned_text = self.preprocessor.preprocess(

                raw_text

            )

            pre_time = time.perf_counter() - pre_start

            ####################################################
            # Profiling
            ####################################################

            total = time.perf_counter() - start_total

            print()
            print("=" * 60)
            print("VISION PROFILING")
            print("=" * 60)
            print(f"OCR        : {ocr_time:.2f}s")
            print(f"Preprocess : {pre_time:.2f}s")
            print("-" * 60)
            print(f"TOTAL      : {total:.2f}s")
            print("=" * 60)
            print()

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

    ############################################################
    # Full Screen OCR
    ############################################################

    def read_screen(
        self,
        image_path: str | None = None,
    ) -> VisionResult:

        if image_path is None:

            image_path = self.desktop.take_screenshot()

        if image_path is None:

            return VisionResult(

                success=False,

                error="Failed to capture screenshot.",

            )

        return self._process_image(

            image_path

        )

    ############################################################
    # Region OCR
    ############################################################

    def read_region(
        self,
        region: ScreenRegion,
    ) -> VisionResult:

        image_path = self.desktop.take_region_screenshot(

            region

        )

        if image_path is None:

            return VisionResult(

                success=False,

                error="Failed to capture region.",

            )

        return self._process_image(

            image_path

        )