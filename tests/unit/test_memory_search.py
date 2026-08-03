from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_manager import MemoryManager
from ai.memory.memory_type import MemoryType


def test_memory_search():

    manager = MemoryManager()

    manager.clear()

    manager.add(
        Memory(
            memory_type=MemoryType.WORKING,
            content="Remember my favourite colour is blue",
            created_at=datetime.now()
        )
    )

    manager.add(
        Memory(
            memory_type=MemoryType.WORKING,
            content="Remember I live in Uttarakhand",
            created_at=datetime.now()
        )
    )

    results = manager.find(
        "What is my favourite colour?"
    )

    assert len(results) == 1

    assert "blue" in results[0].content.lower()