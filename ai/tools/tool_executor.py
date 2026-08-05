from ai.tools.intent.tool_intent_classifier import (
    ToolIntentClassifier,
)

from ai.tools.resolver.tool_resolver import (
    ToolResolver,
)

from ai.tools.tool_context import ToolContext
from ai.tools.tool_manager import ToolManager
from ai.tools.tool_result import ToolResult


class ToolExecutor:
    """
    Executes JARVIS tools.

    Responsibilities
    ----------------
    • Classify tool intent
    • Resolve the correct tool
    • Build ToolContext
    • Execute the selected tool
    • Return ToolResult

    ToolExecutor never decides which tool
    should handle a command.
    """

    ############################################################

    def __init__(self):

        self.manager = ToolManager()

        self.intent_classifier = ToolIntentClassifier()

        self.resolver = ToolResolver(

            self.manager.tool_registry

        )

    ############################################################

    def execute(
        self,
        command: str,
        conversation=None,
        metadata=None,
    ) -> ToolResult:

        ########################################################
        # Classify Intent
        ########################################################

        intent = self.intent_classifier.classify(

            command

        )

        ########################################################
        # Resolve Tool
        ########################################################

        tool = self.resolver.resolve(

            command,

            intent,

        )

        if tool is None:

            return ToolResult(

                success=False,

                message="I couldn't find a tool to handle that request.",

                error="Tool not found",

            )

        ########################################################
        # Build Context
        ########################################################

        context = ToolContext(

            command=command,

            conversation=conversation,

            metadata=metadata,

        )

        ########################################################
        # Execute Tool
        ########################################################

        try:

            return tool.execute(

                context

            )

        except Exception as e:

            import traceback
            print("\n" + "=" * 80)
            print("JARVIS TOOL EXCEPTION")
            print("=" * 80)

            traceback.print_exc()

            print("=" * 80 + "\n")

            return ToolResult(

                success=False,

                message=str(e),

                error=traceback.format_exc(),

            )