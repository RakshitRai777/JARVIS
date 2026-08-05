from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Close Notepad",

    "Close Calculator",

]

for command in tests:

    result = executor.execute(command)

    print(result.message)