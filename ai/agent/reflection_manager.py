from datetime import datetime

from ai.agent.reflection_engine import ReflectionEngine
from ai.agent.reflection_context import ReflectionContext

from ai.memory.memory import Memory
from ai.memory.memory_service import MemoryService
from ai.memory.memory_type import MemoryType


class ReflectionManager:
    """
    Coordinates reflection and long-term learning.
    """

    ############################################################

    def __init__(self):

        self.engine = ReflectionEngine()

        self.memory_service = MemoryService()

    ############################################################

    def reflect(
        self,
        context: ReflectionContext,
    ):

        ########################################################

        result = self.engine.reflect(

            context,

        )

        ########################################################
        # Store learning
        ########################################################

        if result.should_store:

            self.memory_service.remember(

                Memory(

                    memory_type=MemoryType.LONG_TERM,

                    content=result.learning,

                    created_at=datetime.now(),

                )

            )

        ########################################################

        return result