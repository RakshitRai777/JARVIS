from __future__ import annotations

from typing import Any


class ServiceContainer:
    """
    Central dependency container for JARVIS.

    Stores shared singleton-like services used across
    the application.

    This is the Composition Root of the system.
    """

    ############################################################

    def __init__(self):

        self._services: dict[type, Any] = {}

    ############################################################

    def register(
        self,
        service: Any,
    ) -> None:
        """
        Register a service instance.
        """

        self._services[type(service)] = service

    ############################################################

    def resolve(
        self,
        service_type: type,
    ) -> Any:
        """
        Resolve a registered service.

        Raises
        ------
        KeyError
            If the service has not been registered.
        """

        if service_type not in self._services:

            raise KeyError(

                f"{service_type.__name__} has not been registered."

            )

        return self._services[service_type]

    ############################################################

    def contains(
        self,
        service_type: type,
    ) -> bool:

        return service_type in self._services

    ############################################################

    def clear(
        self,
    ) -> None:

        self._services.clear()

    ############################################################

    def __len__(
        self,
    ) -> int:

        return len(self._services)

    ############################################################

    def __repr__(
        self,
    ) -> str:

        return (

            f"ServiceContainer("

            f"services={len(self)})"

        )