from ai.tools.system.application_database import ApplicationDatabase

db = ApplicationDatabase()

tests = [

    "Open Chrome",

    "Launch VS Code",

    "Open Notepad",

    "Start Calculator",

]

for t in tests:

    app = db.find(t)

    if app:

        print(app.name, "->", app.command)

    else:

        print("Not Found")