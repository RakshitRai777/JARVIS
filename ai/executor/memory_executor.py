from datetime import datetime

from runtime.runtime import runtime

from ai.execution.execution_result import ExecutionResult

from ai.embeddings.embedding_model import EmbeddingModel

from ai.memory.memory import Memory
from ai.memory.memory_type import MemoryType

from ai.memory.intent.memory_intent_classifier import (
    MemoryIntentClassifier,
)
from ai.memory.intent.memory_intent import MemoryIntent


class MemoryExecutor:
    """
    Executes memory operations.

    Supported operations
    --------------------
    • Store
    • Recall
    • Update
    • Delete (placeholder)
    """

    ############################################################

    def __init__(self):

        self.intent_classifier = MemoryIntentClassifier()

    ############################################################

    def execute(
        self,
        context,
    ):

        memory_service = runtime.services.get(
            "memory"
        )

        user_message = context.messages[-1]["content"]

        ########################################################
        # Detect memory intent
        ########################################################

        intent = self.intent_classifier.classify(
            user_message
        )

        print(f"[MemoryIntent] {intent.value}")

        ########################################################
        # STORE
        ########################################################

        if intent == MemoryIntent.STORE:

            print("[Memory] Creating embedding...")

            embedding = EmbeddingModel.encode(
                user_message
            )

            memory = Memory(

                memory_type=MemoryType.WORKING,

                content=user_message,

                created_at=datetime.now(),

                embedding=embedding,

            )

            if memory_service.remember(memory):

                return ExecutionResult(

                    success=True,

                    message="I will remember that.",

                )

            return ExecutionResult(

                success=True,

                message="I already knew that.",

            )

        ########################################################
        # RECALL
        ########################################################

        if intent == MemoryIntent.RECALL:

            result = memory_service.find(
                user_message
            )

            if result:

                return ExecutionResult(

                    success=True,

                    message=result,

                )

            return ExecutionResult(

                success=False,

                message="I couldn't find anything in memory.",

            )

        ########################################################
        # UPDATE
        ########################################################

        if intent == MemoryIntent.UPDATE:

            print("[Memory] Creating embedding...")

            embedding = EmbeddingModel.encode(
                user_message
            )

            memory = Memory(

                memory_type=MemoryType.WORKING,

                content=user_message,

                created_at=datetime.now(),

                embedding=embedding,

            )

            updated = memory_service.update(
                memory
            )

            if updated:

                return ExecutionResult(

                    success=True,

                    message="I've updated that memory.",

                )

            return ExecutionResult(

                success=False,

                message="I couldn't find anything to update.",

            )

        ########################################################
        # DELETE
        ########################################################

        if intent == MemoryIntent.DELETE:

            return ExecutionResult(

                success=False,

                message="Memory deletion is not implemented yet.",

            )

        ########################################################

        return ExecutionResult(

            success=False,

            message="Unknown memory request.",

        )