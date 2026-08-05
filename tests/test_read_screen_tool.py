from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Read my screen",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print()

    print("OCR Result:")

    print("--------------------------------")

    print(result.message)

    print("--------------------------------")