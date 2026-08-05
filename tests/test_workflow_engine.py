from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep
from ai.workflow.workflow_engine import WorkflowEngine

workflow = Workflow(

    name="Keyboard Test"

)

workflow.add_step(

    WorkflowStep(

        action="type_text",

        parameters={

            "text": "Hello from Workflow Engine"

        }

    )

)

workflow.add_step(

    WorkflowStep(

        action="press_key",

        parameters={

            "key": "enter"

        }

    )

)

workflow.add_step(

    WorkflowStep(

        action="type_text",

        parameters={

            "text": "Workflow execution successful"

        }

    )

)

engine = WorkflowEngine()

print()

print("Open Notepad and place the cursor inside it.")

input("Press Enter when ready...")

import time

time.sleep(3)

result = engine.execute(

    workflow

)

print()

print(result)