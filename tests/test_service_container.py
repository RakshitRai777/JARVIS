from ai.core.service_container import ServiceContainer

from ai.desktop.mouse import Mouse

from ai.desktop.window_manager import WindowManager


def main():

    container = ServiceContainer()

    mouse = Mouse()

    windows = WindowManager()

    ########################################################

    container.register(mouse)

    container.register(windows)

    ########################################################

    print()

    print(container)

    print()

    print(

        container.contains(Mouse)

    )

    print(

        container.contains(WindowManager)

    )

    print()

    print(

        container.resolve(Mouse)

    )

    print(

        container.resolve(WindowManager)

    )

    print()

    print(

        len(container)

    )


if __name__ == "__main__":

    main()