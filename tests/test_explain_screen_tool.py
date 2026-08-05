from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Explain my screen",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print()

    print(result.message)