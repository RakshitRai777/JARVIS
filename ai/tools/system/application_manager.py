import subprocess

from ai.tools.system.application_database import Application


class ApplicationManager:
    """
    Handles all desktop application operations.

    Responsibilities
    ----------------
    • Launch
    • Close
    • Restart (future)
    • Check running state (future)
    """

    ############################################################

    def launch(
        self,
        application: Application,
    ) -> bool:

        try:

            subprocess.Popen(

                [application.launch_command],

                shell=True,

            )

            return True

        except Exception as e:

            print()

            print("[ApplicationManager]")

            print(e)

            print()

            return False

    ############################################################

    def close(
        self,
        application: Application,
    ) -> bool:

        if application.process_name is None:

            print()

            print(

                "[ApplicationManager] "

                f"{application.name} "

                "cannot be safely terminated."

            )

            print()

            return False

        try:

            subprocess.run(

                [

                    "taskkill",

                    "/IM",

                    application.process_name,

                    "/F",

                ],

                capture_output=True,

                text=True,

            )

            return True

        except Exception as e:

            print()

            print("[ApplicationManager]")

            print(e)

            print()

            return False