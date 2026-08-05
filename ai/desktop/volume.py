from __future__ import annotations

from pycaw.pycaw import AudioUtilities


class Volume:
    """
    System volume utility.

    Responsibilities
    ----------------
    • Get current volume
    • Set volume
    • Mute
    • Unmute
    """

    ############################################################

    def _interface(self):

        device = AudioUtilities.GetSpeakers()

        return device.EndpointVolume

    ############################################################

    def get(self) -> int:

        volume = self._interface()

        level = volume.GetMasterVolumeLevelScalar()

        return int(level * 100)

    ############################################################

    def set(
        self,
        percent: int,
    ) -> bool:

        percent = max(0, min(100, percent))

        volume = self._interface()

        volume.SetMasterVolumeLevelScalar(

            percent / 100,

            None,

        )

        return True

    ############################################################

    def mute(self) -> bool:

        volume = self._interface()

        volume.SetMute(

            1,

            None,

        )

        return True

    ############################################################

    def unmute(self) -> bool:

        volume = self._interface()

        volume.SetMute(

            0,

            None,

        )

        return True