import time
from pathlib import Path

import cv2

from config.settings import settings

from ai.geometry.screen_region import ScreenRegion
from ai.tools.vision.template.template_match import TemplateMatch
from ai.tools.vision.template.template_result import TemplateResult


class TemplateMatcher:
    """
    Production Template Matching Engine.

    Features
    --------
    • Multi-scale matching
    • Multiple OpenCV algorithms
    • Automatic best-match selection
    • Gaussian blur preprocessing
    • Grayscale matching

    Future
    ------
    • Template cache
    • Rotation support
    • GPU acceleration
    • Edge matching
    • Mask support
    • Non-Maximum Suppression
    """

    ############################################################
    # OpenCV Algorithms
    ############################################################

    METHODS = [

        ("TM_CCOEFF_NORMED", cv2.TM_CCOEFF_NORMED),

        ("TM_CCORR_NORMED", cv2.TM_CCORR_NORMED),

        ("TM_SQDIFF_NORMED", cv2.TM_SQDIFF_NORMED),

    ]

    ############################################################
    # Template Scales
    ############################################################

    SCALES = [

        0.70,
        0.75,
        0.80,
        0.85,
        0.90,
        0.95,
        1.00,
        1.05,
        1.10,
        1.15,
        1.20,
        1.25,
        1.30,

    ]

    ############################################################

    def find(
        self,
        image: str | Path,
        template: str | Path,
        threshold: float = 0.75,
    ) -> TemplateResult:

        start = time.perf_counter()

        ########################################################
        # Load Images
        ########################################################

        image = cv2.imread(

            str(image),

            cv2.IMREAD_GRAYSCALE,

        )

        if image is None:

            return TemplateResult(

                success=False,

                error="Unable to load image.",

            )

        template = cv2.imread(

            str(template),

            cv2.IMREAD_GRAYSCALE,

        )

        if template is None:

            return TemplateResult(

                success=False,

                error="Unable to load template.",

            )

        ########################################################
        # Preprocessing
        ########################################################

        image = cv2.GaussianBlur(

            image,

            (3, 3),

            0,

        )

        template = cv2.GaussianBlur(

            template,

            (3, 3),

            0,

        )

        ########################################################
        # Search
        ########################################################

        best_confidence = -1.0
        best_location = None
        best_scale = 1.0
        best_size = None
        best_method = ""

        ########################################################

        for scale in self.SCALES:

            ####################################################
            # Resize Template
            ####################################################

            resized = cv2.resize(

                template,

                None,

                fx=scale,

                fy=scale,

                interpolation=cv2.INTER_LINEAR,

            )

            h, w = resized.shape

            ####################################################
            # Skip invalid sizes
            ####################################################

            if h < 5 or w < 5:

                continue

            if h >= image.shape[0]:

                continue

            if w >= image.shape[1]:

                continue

            ####################################################
            # Try every OpenCV method
            ####################################################

            for name, method in self.METHODS:

                result = cv2.matchTemplate(

                    image,

                    resized,

                    method,

                )

                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(

                    result

                )

                ################################################

                if method == cv2.TM_SQDIFF_NORMED:

                    confidence = 1.0 - min_val
                    location = min_loc

                else:

                    confidence = max_val
                    location = max_loc

                ################################################

                if settings.OCR_DEBUG:

                    print(

                        f"{name:<22}"

                        f"Scale={scale:.2f}   "

                        f"{confidence:.4f}"

                    )

                ################################################

                if confidence > best_confidence:

                    best_confidence = confidence
                    best_location = location
                    best_scale = scale
                    best_size = (w, h)
                    best_method = name

        ########################################################
        # Debug Summary
        ########################################################

        if settings.OCR_DEBUG:

            print()

            print("=" * 60)

            print("BEST TEMPLATE MATCH")

            print("=" * 60)

            print(f"Method     : {best_method}")
            print(f"Scale      : {best_scale:.2f}")
            print(f"Confidence : {best_confidence:.4f}")

            print("=" * 60)

            print()

        ########################################################
        # Threshold
        ########################################################

        if best_confidence < threshold:

            return TemplateResult(

                success=False,

                execution_time=(
                    time.perf_counter()
                    - start
                ),

                error=(

                    f"Template not found "

                    f"(best confidence={best_confidence:.3f})"

                ),

            )

        ########################################################
        # Build Result
        ########################################################

        region = ScreenRegion(

            left=best_location[0],

            top=best_location[1],

            width=best_size[0],

            height=best_size[1],

        )

        match = TemplateMatch(

            region=region,

            confidence=float(best_confidence),

        )

        ########################################################

        return TemplateResult(

            success=True,

            best_match=match,

            matches=[match],

            execution_time=(
                time.perf_counter()
                - start
            ),

        )