from ai.actions.action_manager import ActionManager
from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep

workflow = Workflow(
    name="Click Test"
)

workflow.add_step(

    WorkflowStep(

        action="click_text",

        parameters={

            "target": "ChatGPT"

        }

    )

)

manager = ActionManager()

result = manager.execute(

    workflow,

    workflow.steps[0]

)

print()

print(result)