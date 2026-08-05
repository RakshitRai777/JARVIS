import time

from ai.desktop.screenshot import Screenshot
from ai.tools.vision.vision_manager import VisionManager
from ai.geometry.screen_region import ScreenRegion

def main():

    screenshot = Screenshot()

    print()
    print("Capturing 600x200 region...")
    print()

    ############################################################

    region = ScreenRegion(
        left=0,

        top=0,

        width=600,

        height=200,
    )

    image = screenshot.capture_region(
        region
    )

    ############################################################

    vision = VisionManager()

    start = time.perf_counter()

    result = vision.read_screen(

        image_path=image

    )

    elapsed = time.perf_counter() - start

    ############################################################

    print()

    print("=" * 60)
    print("REGION OCR BENCHMARK")
    print("=" * 60)

    print(f"Success : {result.success}")

    print(f"Elapsed : {elapsed:.2f}s")

    print(f"Image   : {image}")

    print("=" * 60)

    ############################################################

    if result.success:

        print()

        print("Detected Text:")

        print("-" * 60)

        print(result.cleaned_text)

        print("-" * 60)


if __name__ == "__main__":

    main()