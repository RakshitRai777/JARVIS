from __future__ import annotations

from datetime import datetime
from pathlib import Path

from PIL import ImageGrab

from ai.geometry.screen_region import ScreenRegion
from config.settings import settings


class Screenshot:
    """
    Screenshot utility.

    Responsibilities
    ----------------
    • Capture full screen
    • Capture screen regions

    Does NOT perform OCR.
    Does NOT manage desktop state.
    """

    ############################################################

    def capture(
        self,
        directory: str | Path = settings.SCREENSHOT_DIR,
    ) -> str:

        folder = Path(directory)

        folder.mkdir(

            parents=True,

            exist_ok=True,

        )

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S_%f"

        )

        file = folder / f"{timestamp}.png"

        image = ImageGrab.grab()

        image.save(file)

        return str(file)

    ############################################################

    def capture_region(
        self,
        region: ScreenRegion,
        directory: str | Path = settings.SCREENSHOT_DIR,
    ) -> str:

        folder = Path(directory)

        folder.mkdir(

            parents=True,

            exist_ok=True,

        )

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S_%f"

        )

        file = folder / f"{timestamp}_region.png"

        image = ImageGrab.grab(

            bbox=region.as_bbox()

        )

        image.save(file)

        return str(file)