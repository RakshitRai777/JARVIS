from dataclasses import dataclass


@dataclass(frozen=True)
class Application:
    """
    Represents a desktop application.
    """

    ############################################################

    name: str

    ############################################################

    launch_command: str

    ############################################################

    process_name: str | None

    ############################################################

    aliases: tuple[str, ...] = ()


class ApplicationDatabase:
    """
    Stores known desktop applications.

    Responsibilities
    ----------------
    • Register applications
    • Find applications
    • Never launch or close them
    """

    ############################################################

    def __init__(self):

        self._applications = [

            ####################################################
            # Browsers
            ####################################################

            Application(

                name="Google Chrome",

                launch_command="chrome",

                process_name="chrome.exe",

                aliases=(

                    "chrome",

                    "google chrome",

                ),

            ),

            Application(

                name="Microsoft Edge",

                launch_command="msedge",

                process_name="msedge.exe",

                aliases=(

                    "edge",

                    "microsoft edge",

                ),

            ),

            Application(

                name="Firefox",

                launch_command="firefox",

                process_name="firefox.exe",

                aliases=(

                    "firefox",

                ),

            ),

            ####################################################
            # IDEs
            ####################################################

            Application(

                name="Visual Studio Code",

                launch_command="code",

                process_name="Code.exe",

                aliases=(

                    "vs code",

                    "vscode",

                    "visual studio code",

                    "code",

                ),

            ),

            Application(

                name="PyCharm",

                launch_command="pycharm64",

                process_name="pycharm64.exe",

                aliases=(

                    "pycharm",

                ),

            ),

            ####################################################
            # Windows Apps
            ####################################################

            Application(

                name="Notepad",

                launch_command="notepad",

                process_name="notepad.exe",

                aliases=(

                    "notepad",

                ),

            ),

            Application(

                name="Calculator",

                launch_command="calc",

                process_name="CalculatorApp.exe",

                aliases=(

                    "calculator",

                    "calc",

                ),

            ),

            Application(

                name="File Explorer",

                launch_command="explorer",

                process_name=None,

                aliases=(

                    "explorer",

                    "file explorer",

                ),

            ),

            Application(

                name="Command Prompt",

                launch_command="cmd",

                process_name="cmd.exe",

                aliases=(

                    "cmd",

                    "command prompt",

                ),

            ),

            Application(

                name="PowerShell",

                launch_command="powershell",

                process_name="powershell.exe",

                aliases=(

                    "powershell",

                ),

            ),

        ]

    ############################################################

    def find(
        self,
        text: str,
    ) -> Application | None:

        text = text.lower()

        for app in self._applications:

            if app.name.lower() in text:

                return app

            for alias in app.aliases:

                if alias in text:

                    return app

        return None

    ############################################################

    def all(self) -> list[Application]:

        return self._applications.copy()