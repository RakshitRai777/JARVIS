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

    ############################################################

    def successful(
            self,
    ) -> list[RuntimeHistoryEntry]:
        return[
            entry 
            for entry in self._entries
            if entry.result.success
        ]

    ############################################################

    def failed(
        self,
    ) -> list[RuntimeHistoryEntry]:
        return[
            entry 
            for entry in self._entries
            if not entry.result.success
        ]

    ############################################################

    def last_success(
        self,
    ) -> RuntimeHistoryEntry | None:
        for entry in reversed(
            self._entries,
        ):
            if entry.result.success:
                return entry
        return None

    ############################################################

    def last_failure(
        self,
    ) -> RuntimeHistoryEntry | None:
    
        for entry in reversed(
    
            self._entries,
    
        ):
    
            if not entry.result.success:
    
                return entry
    
        return None

    ############################################################

    def by_action(
        self,
        action: str,
    ) -> list[RuntimeHistoryEntry]:
    
        return [
    
            entry
    
            for entry in self._entries
    
            if entry.action == action
    
        ]

    ############################################################

    def by_workflow(
        self,
        workflow: str,
    ) -> list[RuntimeHistoryEntry]:
    
        return [
    
            entry
    
            for entry in self._entries
    
            if entry.workflow == workflow
    
        ]