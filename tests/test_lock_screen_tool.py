from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Lock screen",

    "Lock computer",

    "Lock workstation",

]

for command in tests:

    print()

    print(command)

    input("Press Enter to execute...")

    result = executor.execute(command)

    print(result.message)