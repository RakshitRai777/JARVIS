from datetime import datetime

from runtime.runtime import runtime

from ai.conversation.conversation_manager import ConversationManager
from ai.context.context_builder import ContextBuilder
from ai.executor.executor import Executor
from ai.memory.extraction.fact_extractor import FactExtractor
from ai.memory.memory import Memory
from ai.memory.memory_type import MemoryType
from ai.planner.planner import Planner
from ai.conversation.query_resolution.conversation_resolver import ConversationResolver
from ai.web.query_rewriter.query_rewriter import QueryRewriter
from ai.conversation.contextual_detector import ContextualDetector
from ai.conversation.contextual_query_rewriter import ContextualQueryRewriter
from ai.conversation.entity_extraction.entity_extractor import EntityExtractor

class Brain:
    """
    JARVIS Brain

    Responsibilities
    ----------------
    • Receive user input
    • Normalize user input
    • Manage conversations
    • Build context
    • Ask the Planner what to do
    • Execute the decision
    • Store assistant responses
    • Automatically extract user facts

    IMPORTANT

    Brain knows NOTHING about:
        • Web
        • RAG
        • Memory Retrieval
        • Knowledge Router

    Those belong to lower layers.
    """

    ############################################################

    def __init__(self):

        self.conversations = ConversationManager()

        self.context_builder = ContextBuilder()

        self.planner = Planner()

        self.executor = Executor()

        self.fact_extractor = FactExtractor()

        self.entity_extractor = EntityExtractor()

        self.query_rewriter = QueryRewriter()

        self.conversation_resolver = ConversationResolver()

        self.context_detector = ContextualDetector()

        self.contextual_rewriter = ContextualQueryRewriter()

    ############################################################

    def chat(
        self,
        user_message: str,
        conversation_id: str = "default",
        metadata=None,
    ) -> str:

        ########################################################
        # Conversation
        ########################################################

        conversation = self.conversations.get(
            conversation_id
        )

        conversation.add(
            "user",
            user_message
        )

        ########################################################
        # Resolve conversational references
        ########################################################

        resolution = self.conversation_resolver.resolve(
            user_message,
            conversation,
        )

        resolved_message = resolution.resolved_query

        if resolution.changed:

            print()

            print("[ConversationResolver]")

            print(f"Original : {resolution.original_query}")

            print(f"Resolved : {resolution.resolved_query}")

            print(f"Reason   : {resolution.reason}")

            print()

        ########################################################
        # Normalize Query
        ########################################################

        rewrite = self.query_rewriter.rewrite(
            resolved_message
        )

        effective_message = rewrite.rewritten_query

        ########################################################
        # Context-aware rewriting
        ########################################################

        if self.context_detector.needs_context(effective_message):

            rewrite2 = self.contextual_rewriter.rewrite(
                conversation,
                effective_message,
            )

            if rewrite2.changed:

                print()

                print("[ContextualRewriter]")

                print(f"Original : {rewrite2.original_query}")

                print(f"Rewritten: {rewrite2.rewritten_query}")

                print(f"Reason   : {rewrite2.reason}")

                print()

            effective_message = rewrite2.rewritten_query

        if rewrite.changed:

            print()

            print("[QueryRewriter]")

            print(f"Original : {rewrite.original_query}")

            print(f"Rewritten: {rewrite.rewritten_query}")

            print(f"Reason   : {rewrite.reason}")

            print()

        ########################################################
        # Planner
        ########################################################

        decision = self.planner.decide(
            effective_message
        )

        print(
            f"[Planner] "
            f"Action={decision.action.value} | "
            f"Reason={decision.reason}"
        )

        ########################################################
        # Build Context
        ########################################################

        context = self.context_builder.build(
            conversation=conversation,
            original_query=user_message,
            search_query=effective_message,
            metadata=metadata,
        )

        ########################################################
        # Execute
        ########################################################

        result = self.executor.execute(
            decision,
            context,
        )

        ########################################################
        # Store assistant reply
        ########################################################

        conversation.add(
            "assistant",
            result.message
        )

        ########################################################
        # Extract conversation entities
        ########################################################
        try:
            extraction = self.entity_extractor.extract(
                result.message
            )

            if extraction.entities:
                print()
                print("[EntityExtractor]")

                for entity in extraction.entities:
                    conversation.entity_memory.add(entity)

                    print(
                        f"{entity.entity_type.value.upper()} : "
                        f"{entity.name}"
                    )
                print()

        except Exception as e:
            print("[EntityExtractor] Failed")
            print(e)
        
        ########################################################
        # Automatic Fact Extraction
        ########################################################

        fact = self.fact_extractor.extract(
            user_message
        )

        if fact is not None:

            memory_service = runtime.services.get(
                "memory"
            )

            if memory_service is not None:

                memory_service.remember(

                    Memory(

                        memory_type=MemoryType.WORKING,

                        content=fact.content,

                        created_at=datetime.now()

                    )

                )

        ########################################################

        return result.message