from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from typing import Any

from ai.runtime.runtime_history import RuntimeHistory


@dataclass
class RuntimeSession:
    """
    Represents one runtime execution session.

    A session groups together:

    • Runtime history
    • Metadata
    • Start time
    • End time

    Future Responsibilities
    -----------------------
    • Statistics
    • Variables
    • Recovery
    • Persistence
    """

    ############################################################

    session_id: str = field(

        default_factory=lambda: str(

            uuid4()

        )

    )

    ############################################################

    started_at: datetime = field(

        default_factory=datetime.now

    )

    ############################################################

    ended_at: datetime | None = None

    ############################################################

    history: RuntimeHistory = field(

        default_factory=RuntimeHistory

    )

    ############################################################

    metadata: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    def end(
        self,
    ):

        """
        Mark the session as finished.
        """

        self.ended_at = datetime.now()

    ############################################################

    @property
    def active(
        self,
    ) -> bool:

        return self.ended_at is None