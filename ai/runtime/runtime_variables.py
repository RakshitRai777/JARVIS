from __future__ import annotations

from typing import Any


class RuntimeVariables:
    """
    Stores temporary runtime variables.

    Variables exist only for the lifetime
    of a RuntimeSession.

    Future Responsibilities
    -----------------------
    • Variable scopes
    • Read-only variables
    • Type validation
    • Serialization
    • Persistence
    """

    ############################################################

    def __init__(self):

        self._variables: dict[str, Any] = {}

    ############################################################

    def set(
        self,
        name: str,
        value: Any,
    ):

        self._variables[name] = value

    ############################################################

    def get(
        self,
        name: str,
        default: Any = None,
    ) -> Any:

        return self._variables.get(

            name,

            default,

        )

    ############################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._variables

    ############################################################

    def remove(
        self,
        name: str,
    ):

        self._variables.pop(

            name,

            None,

        )

    ############################################################

    def clear(
        self,
    ):

        self._variables.clear()

    ############################################################

    def all(
        self,
    ) -> dict[str, Any]:

        return dict(

            self._variables,

        )

    ############################################################

    def __len__(
        self,
    ) -> int:

        return len(

            self._variables,

        )

    ############################################################

    def __contains__(
        self,
        name: str,
    ) -> bool:

        return name in self._variables