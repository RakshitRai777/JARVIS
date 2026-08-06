import subprocess
import time

from ai.actions.action_manager import ActionManager
from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep


def main():

    ############################################################
    # Open Notepad
    ############################################################

    subprocess.Popen("notepad.exe")

    time.sleep(2)

    ############################################################

    manager = ActionManager()

    workflow = Workflow(

        name="Focus Test",

    )

    step = WorkflowStep(

        action="focus_window",

        parameters={

            "application": "Notepad",

        },

    )

    ############################################################

    result = manager.execute(

        workflow,

        step,

    )

    print()

    print(result)


if __name__ == "__main__":

    main()