from dataclasses import dataclass
from datetime import datetime

from ai.input.input_source import InputSource


@dataclass
class InputEvent:
    """
    A normalized user request.

    Every request entering JARVIS is converted
    into an InputEvent before reaching the Brain.
    """

    ############################################################

    text: str

    ############################################################

    source: InputSource

    ############################################################

    timestamp: datetime

    ############################################################

    metadata: dict | None = None