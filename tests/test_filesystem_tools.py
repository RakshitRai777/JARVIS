from ai.tools.tool_executor import ToolExecutor

executor = ToolExecutor()

tests = [

    # Create folders

    "Create folder TestFolder",

    "Make folder DemoFolder",

    "New folder AIProjects",

    # Create files

    "Create file notes.txt",

    "New file todo.md",

    "Make file config.json",

    # Rename

    "Rename notes.txt to notes_old.txt",

    "Rename DemoFolder to MyProjects",

    # Delete

    "Delete notes_old.txt",

    "Delete MyProjects",

]

for command in tests:

    print()

    print(command)

    result = executor.execute(command)

    print(result.message)