from ai.tools.desktop.mouse_manager import MouseManager

mouse = MouseManager()

print("Current Position:")

print(mouse.position())

print()

input("Press Enter to move mouse...")

mouse.move_to(500, 500)

print("Mouse moved.")

input("Press Enter to left click...")

mouse.left_click()

print("Clicked.")

input("Press Enter to right click...")

mouse.right_click()

print("Right clicked.")

input("Press Enter to double click...")

mouse.double_click()

print("Double clicked.")