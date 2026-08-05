from dataclasses import dataclass
from datetime import datetime

from ai.events.event_type import EventType


@dataclass
class Event:
    """
    Generic event flowing through JARVIS.
    """

    event_type: EventType

    timestamp: datetime

    payload: dict

    metadata: dict | None = None