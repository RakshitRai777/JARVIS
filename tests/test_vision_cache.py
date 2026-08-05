import time

from ai.tools.vision.vision_manager import VisionManager


def main():

    vision = VisionManager()

    ########################################################

    print()

    print("FIRST CALL")

    start = time.perf_counter()

    vision.read_screen()

    print(

        f"{time.perf_counter()-start:.2f}s"

    )

    ########################################################

    print()

    print("SECOND CALL")

    start = time.perf_counter()

    vision.read_screen()

    print(

        f"{time.perf_counter()-start:.4f}s"

    )


if __name__ == "__main__":

    main()
    