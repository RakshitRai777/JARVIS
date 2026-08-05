from __future__ import annotations

import pygetwindow as gw


class Window:
    """
    Wrapper around a native desktop window.

    This class represents ONE window and exposes
    high-level window operations.
    """

    ############################################################

    def __init__(
        self,
        native_window: gw.Window,
    ):

        self._window = native_window

    ############################################################
    # Properties
    ############################################################

    @property
    def title(self) -> str:

        return self._window.title

    ############################################################

    @property
    def left(self) -> int:

        return self._window.left

    ############################################################

    @property
    def top(self) -> int:

        return self._window.top

    ############################################################

    @property
    def width(self) -> int:

        return self._window.width

    ############################################################

    @property
    def height(self) -> int:

        return self._window.height

    ############################################################

    @property
    def rect(self):

        return (

            self.left,

            self.top,

            self.width,

            self.height,

        )

    ############################################################
    # State
    ############################################################

    def activate(self):

        self._window.activate()

    ############################################################

    def minimize(self):

        self._window.minimize()

    ############################################################

    def maximize(self):

        self._window.maximize()

    ############################################################

    def restore(self):

        self._window.restore()

    ############################################################

    def close(self):

        self._window.close()

    ############################################################
    # Position
    ############################################################

    def move(
        self,
        x: int,
        y: int,
    ):

        self._window.moveTo(

            x,

            y,

        )

    ############################################################

    def resize(
        self,
        width: int,
        height: int,
    ):

        self._window.resizeTo(

            width,

            height,

        )

    ############################################################

    def __repr__(self):

        return (

            f"Window(title={self.title!r}, "

            f"left={self.left}, "

            f"top={self.top}, "

            f"width={self.width}, "

            f"height={self.height})"

        )