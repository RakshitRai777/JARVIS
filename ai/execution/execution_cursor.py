from ai.planner.execution_step import ExecutionStep


class ExecutionCursor:
    """
    Tracks progress through an execution plan.

    Responsibilities
    ----------------
    • Track current position
    • Move to next step
    • Move to previous step
    • Jump to a step
    • Reset execution
    • Expose current step

    Future Responsibilities
    -----------------------
    • Pause / Resume
    • Breakpoints
    • Skip steps
    """

    ############################################################

    def __init__(
        self,
        steps: list[ExecutionStep],
    ):

        self._steps = steps

        self._index = 0

    ############################################################

    @property
    def index(
        self,
    ) -> int:

        return self._index

    ############################################################

    @property
    def total_steps(
        self,
    ) -> int:

        return len(self._steps)

    ############################################################

    def current(
        self,
    ) -> ExecutionStep | None:

        if not self._steps:

            return None

        if self._index >= len(self._steps):

            return None

        return self._steps[self._index]

    ############################################################

    def has_next(
        self,
    ) -> bool:

        return self._index < len(self._steps)

    ############################################################

    def next(
        self,
    ) -> None:

        if self.has_next():

            self._index += 1

    ############################################################

    def previous(
        self,
    ) -> None:

        if self._index > 0:

            self._index -= 1

    ############################################################

    def goto(
        self,
        index: int,
    ) -> None:

        if 0 <= index <= len(self._steps):

            self._index = index

    ############################################################

    def reset(
        self,
    ) -> None:

        self._index = 0