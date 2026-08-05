from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Open Notepad",

    "Open Calculator",

    "Open Explorer",

]

for command in tests:

    result = executor.execute(command)

    print(result.message)