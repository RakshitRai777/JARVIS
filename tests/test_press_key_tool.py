import time

from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

print()
print("Open Notepad and click inside it.")
input("Press Enter when ready...")

time.sleep(3)

tests = [

    "Type Hello Boss",

    "Press Enter",

    "Type This is line two",

    "Press Enter",

    "Type PressKeyTool is working",

]

for command in tests:

    print()
    print(command)

    result = executor.execute(command)

    print(result.message)

    time.sleep(1)