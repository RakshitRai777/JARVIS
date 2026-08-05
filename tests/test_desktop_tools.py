from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Take a screenshot",

    "Capture screen",

    "Take screenshot",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)