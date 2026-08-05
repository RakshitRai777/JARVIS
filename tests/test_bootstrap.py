from ai.core.bootstrap import Bootstrap

from ai.desktop.mouse import Mouse
from ai.desktop.window_manager import WindowManager
from ai.tools.vision.vision_manager import VisionManager


def main():

    bootstrap = Bootstrap()

    container = bootstrap.build()

    print()

    print(container)

    print()

    print(container.resolve(Mouse))

    print(container.resolve(WindowManager))

    print(container.resolve(VisionManager))

    print()

    print(len(container))


if __name__ == "__main__":

    main()