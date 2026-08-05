from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Find Remote Laptop Control Via Mobile",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)