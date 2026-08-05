from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "What is my volume?",

    "Set volume to 35",

    "Mute",

    "Unmute",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)