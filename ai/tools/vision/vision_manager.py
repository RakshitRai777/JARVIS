import time
from difflib import SequenceMatcher
from pathlib import Path

from config.settings import settings

from ai.geometry.screen_region import ScreenRegion

from ai.tools.vision.cache import VisionCache
from ai.tools.vision.ocr_manager import OCRManager
from ai.tools.vision.template.template_manager import TemplateManager
from ai.tools.vision.template.template_result import TemplateResult
from ai.tools.vision.vision_preprocessor import VisionPreprocessor
from ai.tools.vision.vision_result import VisionResult
from ai.desktop.screenshot import Screenshot

class VisionManager:
    """
    Central Vision Engine.

    Responsibilities
    ----------------
    • Capture screenshots
    • Capture region screenshots
    • OCR
    • Template Matching
    • OCR preprocessing
    • Vision caching
    • Return structured results
    """

    ############################################################

    def __init__(self):

        self.screenshot = Screenshot()

        self.ocr = OCRManager()

        self.preprocessor = VisionPreprocessor()

        self.templates = TemplateManager()

        self.cache = VisionCache(
            ttl=1.0
        )

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
            # Raw Text
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

            if settings.VISION_PROFILING:

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
        image_path: str | Path | None = None,
        use_cache: bool = True,
    ) -> VisionResult:

        ########################################################
        # Determine whether this is a live capture
        ########################################################

        live_capture = image_path is None

        ########################################################
        # Cache lookup
        ########################################################

        if live_capture and use_cache:

            cached = self.cache.get()

            if cached is not None:

                return cached

        ########################################################
        # Capture screenshot
        ########################################################

        if live_capture:

            image_path = self.screenshot.capture()

        ########################################################

        if image_path is None:

            return VisionResult(

                success=False,

                error="Failed to capture screenshot.",

            )

        ########################################################
        # OCR Pipeline
        ########################################################

        result = self._process_image(

            image_path

        )

        ########################################################
        # Cache only live captures
        ########################################################

        if live_capture and use_cache:

            self.cache.set(

                result

            )

        ########################################################

        return result


    ############################################################
    # Region OCR
    ############################################################
    
    def read_region(
        self,
        region: ScreenRegion,
    ) -> VisionResult:
    
        image_path = self.screenshot.capture_region(
    
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
    
    ############################################################
    # Template Matching
    ############################################################
    
    def find_template(
        self,
        template: str | Path,
        image_path: str | Path | None = None,
        threshold: float = 0.75,
    ) -> TemplateResult:
        """
        Find a template on the current screen.
    
        Parameters
        ----------
        template:
            Template image path.
    
        image_path:
            Optional screenshot path.
            If omitted, a live screenshot is captured.
    
        threshold:
            Minimum confidence.
    
        Returns
        -------
        TemplateResult
        """
    
        ########################################################
    
        if image_path is None:
    
            image_path = self.screenshot.capture()
    
        ########################################################
    
        return self.templates.find(
    
            image=image_path,
    
            template=template,
    
            threshold=threshold,
    
        )

        ############################################################
        # Find Text
        ############################################################

    def find_text(
        self,
        text: str,
        image_path: str | Path | None = None,
    ):
        """
        Find the OCR element that best matches the
        requested text.

        Priority
        --------
        1. Exact match
        2. Contains match
        3. Best similarity

        Returns
        -------
        OCRElement | None
        """

        ########################################################

        result = self.read_screen(

            image_path=image_path,

        )

        ########################################################

        if not result.success:

            return None

        ########################################################

        target = text.lower().strip()

        ########################################################
        # 1. Exact Match
        ########################################################

        for element in result.elements:

            if element.text.lower().strip() == target:

                return element

        ########################################################
        # 2. Contains Match
        ########################################################

        contains = []

        for element in result.elements:

            current = element.text.lower()

            if target in current:

                contains.append(element)

        if contains:

            contains.sort(

                key=lambda e: len(e.text)

            )

            return contains[0]

        ########################################################
        # 3. Similarity Match
        ########################################################

        best_element = None

        best_score = 0.0

        for element in result.elements:

            score = SequenceMatcher(

                None,

                target,

                element.text.lower(),

            ).ratio()

            if score > best_score:

                best_score = score

                best_element = element

        ########################################################

        if best_score >= 0.60:

            return best_element

        ########################################################

        return None

    ############################################################
    # Cache Management
    ############################################################

    def clear_cache(
        self,
    ) -> None:
        """
        Clear the vision cache.

        Useful when the desktop changes significantly or
        before starting a new workflow.
        """

        self.cache.clear()

    ############################################################

    def has_cached_result(
        self,
    ) -> bool:
        """
        Returns True if a valid cached VisionResult exists.
        """

        return self.cache.valid()