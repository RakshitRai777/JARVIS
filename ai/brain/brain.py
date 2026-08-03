from datetime import datetime

from runtime.runtime import runtime

from ai.conversation.conversation_manager import ConversationManager
from ai.context.context_builder import ContextBuilder
from ai.executor.executor import Executor
from ai.memory.extraction.fact_extractor import FactExtractor
from ai.memory.memory import Memory
from ai.memory.memory_type import MemoryType
from ai.planner.planner import Planner


class Brain:
    """
    JARVIS Brain

    Responsibilities
    ----------------
    - Receive user input
    - Manage conversations
    - Build context
    - Ask the Planner what to do
    - Execute the decision
    - Store assistant responses
    - Automatically extract user facts
    """

    def __init__(self):

        self.conversations = ConversationManager()

        self.context_builder = ContextBuilder()

        self.planner = Planner()

        self.executor = Executor()

        self.fact_extractor = FactExtractor()

    def chat(
        self,
        user_message: str,
        conversation_id: str = "default",
        metadata=None
    ) -> str:

        # --------------------------------------------------
        # Get Conversation
        # --------------------------------------------------

        conversation = self.conversations.get(
            conversation_id
        )

        # --------------------------------------------------
        # Store User Message
        # --------------------------------------------------

        conversation.add(
            "user",
            user_message
        )

        # --------------------------------------------------
        # Planner
        # --------------------------------------------------

        decision = self.planner.decide(
            user_message
        )

        print(
            f"[Planner] "
            f"Action={decision.action.value} | "
            f"Reason={decision.reason}"
        )

        # --------------------------------------------------
        # Build Context
        # --------------------------------------------------

        context = self.context_builder.build(
            conversation=conversation,
            metadata=metadata
        )

        # --------------------------------------------------
        # Execute
        # --------------------------------------------------

        result = self.executor.execute(
            decision,
            context
        )

        # --------------------------------------------------
        # Store Assistant Reply
        # --------------------------------------------------

        conversation.add(
            "assistant",
            result.message
        )

        # --------------------------------------------------
        # Automatic Fact Extraction
        # --------------------------------------------------

        fact = self.fact_extractor.extract(
            user_message
        )

        if fact is not None:

            memory_service = runtime.services.get(
                "memory"
            )

            if memory_service is not None:

                stored= memory_service.remember(

                    Memory(

                        memory_type=MemoryType.WORKING,

                        content=fact.content,

                        created_at=datetime.now()

                    )

                )

        # --------------------------------------------------
        # Return
        # --------------------------------------------------

        return result.message