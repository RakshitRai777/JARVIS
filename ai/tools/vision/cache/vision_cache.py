import time

from ai.tools.vision.vision_result import VisionResult


class VisionCache:
    """
    Generic cache for VisionManager.

    Currently caches:
        • OCR VisionResult

    Future:
        • Screenshots
        • Template Matches
        • Object Detection
        • Accessibility Tree
    """

    ############################################################

    def __init__(
        self,
        ttl: float = 1.0,
    ):

        self.ttl = ttl

        self.clear()

    ############################################################

    def clear(self):

        self._vision_result: VisionResult | None = None

        self._timestamp = 0.0

    ############################################################

    def valid(self) -> bool:

        if self._vision_result is None:

            return False

        return (

            time.perf_counter()

            - self._timestamp

            <= self.ttl

        )

    ############################################################

    def get(self) -> VisionResult | None:

        if self.valid():

            return self._vision_result

        return None

    ############################################################

    def set(
        self,
        result: VisionResult,
    ):

        self._vision_result = result

        self._timestamp = time.perf_counter()