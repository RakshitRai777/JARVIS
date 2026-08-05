import time

from ai.tools.vision.vision_manager import VisionManager


vision = VisionManager()

start = time.perf_counter()

result = vision.read_screen()

elapsed = time.perf_counter() - start

print()

print(result.success)

print()

print(f"Elapsed: {elapsed:.2f} seconds")