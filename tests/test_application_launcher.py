from ai.tools.system.application_database import (
    ApplicationDatabase,
)

from ai.tools.system.application_launcher import (
    ApplicationLauncher,
)

db = ApplicationDatabase()

launcher = ApplicationLauncher()

app = db.find("Open Notepad")

print(launcher.launch(app))