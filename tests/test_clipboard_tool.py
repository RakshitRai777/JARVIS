import pyperclip

from ai.tools.tool_executor import ToolExecutor

pyperclip.copy("Hello from JARVIS!")

executor = ToolExecutor()

tests = [

    "Read clipboard",

    "Show clipboard",

    "What's in my clipboard?",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)