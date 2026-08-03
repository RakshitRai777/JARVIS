from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_manager import MemoryManager
from ai.memory.memory_type import MemoryType


def test_duplicate_memory():

    manager = MemoryManager()

    manager.clear()

    memory = Memory(
        memory_type=MemoryType.WORKING,
        content="My favourite colour is blue",
        created_at=datetime.now()
    )

    manager.add(memory)

    assert manager.exists(memory)

    assert manager.count() == 1