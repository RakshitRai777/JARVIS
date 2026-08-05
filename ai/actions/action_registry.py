from ai.actions.action import Action


class ActionRegistry:
    """
    Stores and retrieves workflow actions.

    WorkflowEngine never imports individual actions.
    It asks the registry for the correct one.
    """

    ############################################################

    def __init__(self):

        self._actions: dict[str, Action] = {}

    ############################################################

    def register(
        self,
        action: Action,
    ):

        self._actions[action.name] = action

    ############################################################

    def get(
        self,
        name: str,
    ) -> Action | None:

        return self._actions.get(

            name.lower()

        )

    ############################################################

    def all(self):

        return list(

            self._actions.values()

        )

    ############################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self._actions

    ############################################################

    def clear(self):

        self._actions.clear()