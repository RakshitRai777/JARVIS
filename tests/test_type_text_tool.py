import time

from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

print()
print("Open Notepad and click inside it.")
input("Press Enter when ready...")

time.sleep(3)

tests = [

    "Type Hello Boss!",

    "Write JARVIS is typing this sentence.",

    "Enter This is an automated typing test.",

]

for command in tests:

    print()
    print(command)

    result = executor.execute(command)

    print(result.message)

    time.sleep(1)