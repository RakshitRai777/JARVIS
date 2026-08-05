from ai.execution.execution_policy import ExecutionPolicy

from ai.verification.verification_rule import VerificationRule

from ai.workflow.workflow import Workflow
from ai.workflow.workflow_engine import WorkflowEngine
from ai.workflow.workflow_step import WorkflowStep


def main():

    workflow = Workflow(

        name="Workflow Engine Test"

    )

    ############################################################
    # Step 1
    ############################################################

    workflow.add_step(

        WorkflowStep(

            action="type_text",

            parameters={

                "text": "Hello from Workflow Engine"

            },

            policy=ExecutionPolicy(

                verify=True

            ),

            verification_rule=VerificationRule(

                rule_type="text_exists",

                expected="Hello from Workflow Engine"

            ),

        )

    )

    ############################################################
    # Step 2
    ############################################################

    workflow.add_step(

        WorkflowStep(

            action="press_key",

            parameters={

                "key": "enter"

            }

        )

    )

    ############################################################
    # Step 3
    ############################################################

    workflow.add_step(

        WorkflowStep(

            action="type_text",

            parameters={

                "text": "Workflow execution successful"

            },

            policy=ExecutionPolicy(

                verify=True

            ),

            verification_rule=VerificationRule(

                rule_type="text_exists",

                expected="Workflow execution successful"

            ),

        )

    )

    ############################################################

    print()

    print("Open Notepad and place the cursor inside it.")

    input("Press Enter when ready...")

    print()

    ############################################################

    engine = WorkflowEngine()

    result = engine.execute(

        workflow

    )

    ############################################################

    if result.success:

        print(

            f"Workflow completed "

            f"({result.completed_steps}/"

            f"{result.total_steps} steps, "

            f"{result.execution_time:.2f}s)"

        )

    else:

        print()

        print("Workflow FAILED")

        print()

        print(result.error)


############################################################

if __name__ == "__main__":

    main()