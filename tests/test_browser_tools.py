from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    "Open github.com",

    "Open google.com",

    "Search Google for Python decorators",

    "Google OpenAI GPT-5",

    "Search YouTube for Iron Man",

    "YouTube Python Tutorial",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)