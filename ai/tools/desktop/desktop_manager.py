import ctypes
from datetime import datetime
from pathlib import Path

import pyperclip
from PIL import ImageGrab
from pycaw.pycaw import AudioUtilities

from config.settings import settings
from ai.geometry.screen_region import ScreenRegion


class DesktopManager:
    """
    Central manager for desktop operations.

    Responsibilities
    ----------------
    • Screenshots
    • Region Screenshots
    • Clipboard
    • Volume
    • Brightness
    • Lock screen

    Tools should never directly call
    Windows APIs.
    """

    ############################################################
    # Screenshot
    ############################################################

    def take_screenshot(
        self,
        directory: str | Path = settings.SCREENSHOT_DIR,
    ) -> str | None:

        try:

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

        except Exception as e:

            print("\nSCREENSHOT ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################
    # Region Screenshot
    ############################################################

    def take_region_screenshot(
        self,
        region: ScreenRegion,
        directory: str | Path = settings.SCREENSHOT_DIR,
    ) -> str | None:
        """
        Captures a screenshot of a specific region.
        """

        try:

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

        except Exception as e:

            print("\nREGION SCREENSHOT ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################
    # Lock Screen
    ############################################################

    def lock_screen(
        self,
    ) -> bool:

        try:

            ctypes.windll.user32.LockWorkStation()

            return True

        except Exception as e:

            print("\nLOCK SCREEN ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################
    # Clipboard
    ############################################################

    def get_clipboard(
        self,
    ) -> str | None:

        try:

            return pyperclip.paste()

        except Exception as e:

            print("\nGET CLIPBOARD ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################

    def set_clipboard(
        self,
        text: str,
    ) -> bool:

        try:

            pyperclip.copy(text)

            return True

        except Exception as e:

            print("\nSET CLIPBOARD ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################
    # Volume Helpers
    ############################################################

    def _get_volume_interface(self):

        try:

            device = AudioUtilities.GetSpeakers()

            volume = device.EndpointVolume

            return volume

        except Exception as e:

            print("\nGET VOLUME INTERFACE ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################

    def get_volume(
        self,
    ) -> int:

        try:

            volume = self._get_volume_interface()

            level = volume.GetMasterVolumeLevelScalar()

            return int(level * 100)

        except Exception as e:

            print("\nGET VOLUME ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################

    def set_volume(
        self,
        percent: int,
    ) -> bool:

        try:

            percent = max(
                0,
                min(100, percent),
            )

            volume = self._get_volume_interface()

            volume.SetMasterVolumeLevelScalar(

                percent / 100,

                None,

            )

            return True

        except Exception as e:

            print("\nSET VOLUME ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################

    def mute(
        self,
    ) -> bool:

        try:

            volume = self._get_volume_interface()

            volume.SetMute(

                1,

                None,

            )

            return True

        except Exception as e:

            print("\nMUTE ERROR")
            print(type(e).__name__)
            print(e)

            raise

    ############################################################

    def unmute(
        self,
    ) -> bool:

        try:

            volume = self._get_volume_interface()

            volume.SetMute(

                0,

                None,

            )

            return True

        except Exception as e:

            print("\nUNMUTE ERROR")
            print(type(e).__name__)
            print(e)

            raise