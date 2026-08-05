from datetime import datetime

from ai.input.input_event import InputEvent
from ai.input.input_source import InputSource


class InputManager:
    """
    Converts raw input into InputEvent objects.

    Future sources:
    - Keyboard
    - Voice
    - GUI
    - Mobile
    - API
    """

    ############################################################

    def create_event(
        self,
        text: str,
        source: InputSource = InputSource.KEYBOARD,
        metadata: dict | None = None,
    ) -> InputEvent:

        return InputEvent(

            text=text,

            source=source,

            timestamp=datetime.now(),

            metadata=metadata,

        )