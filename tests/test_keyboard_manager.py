import time

from ai.tools.desktop.keyboard_manager import KeyboardManager


keyboard = KeyboardManager()

print()

print("Open Notepad or any text editor.")

input("Press Enter when ready...")

time.sleep(3)

print("Typing...")

keyboard.type_text(

    "Hello Boss! This text was typed by JARVIS.",

)

time.sleep(1)

keyboard.press("enter")

keyboard.type_text(

    "KeyboardManager is working successfully.",

)

time.sleep(1)

keyboard.press("enter")

keyboard.type_text(

    "Testing hotkeys in 2 seconds...",

)

time.sleep(2)

keyboard.hotkey(

    "ctrl",

    "a",

)

time.sleep(1)

keyboard.hotkey(

    "ctrl",

    "c",

)

print()

print("KeyboardManager test completed.")