from __future__ import annotations

from typing import List

from ai.runtime.runtime_history_entry import (
    RuntimeHistoryEntry,
)


class RuntimeHistory:
    """
    Stores the execution history for the current runtime.

    Responsibilities
    ----------------
    • Store execution history
    • Return previous entries
    • Clear history
    • Retrieve latest entry

    Future Responsibilities
    -----------------------
    • Search history
    • Filter history
    • Export history
    • Persist history
    """

    ############################################################

    def __init__(self):

        self._entries: List[
            RuntimeHistoryEntry
        ] = []

    ############################################################

    def add(
        self,
        entry: RuntimeHistoryEntry,
    ):

        self._entries.append(

            entry,

        )

    ############################################################

    def clear(
        self,
    ):

        self._entries.clear()

    ############################################################

    def last(
        self,
    ) -> RuntimeHistoryEntry | None:

        if not self._entries:

            return None

        return self._entries[-1]

    ############################################################

    def all(
        self,
    ) -> List[RuntimeHistoryEntry]:

        return list(

            self._entries,

        )

    ############################################################

    def __len__(
        self,
    ) -> int:

        return len(

            self._entries,

        )

    ############################################################

    def __iter__(
        self,
    ):

        return iter(

            self._entries,

        )