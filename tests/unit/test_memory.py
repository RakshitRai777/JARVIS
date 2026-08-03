from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_manager import MemoryManager
from ai.memory.memory_type import MemoryType


def test_add_memory():

    manager = MemoryManager()

    manager.clear()

    memory = Memory(
        memory_type=MemoryType.WORKING,
        content="Hello",
        created_at=datetime.now()
    )

    manager.add(memory)

    memories = manager.get_all()

    assert len(memories) == 1

    assert memories[0].content == "Hello"