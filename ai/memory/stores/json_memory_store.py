import json
from pathlib import Path
from datetime import datetime

from ai.memory.memory_store import MemoryStore
from ai.memory.memory import Memory
from ai.memory.memory_type import MemoryType


class JsonMemoryStore(MemoryStore):

    def __init__(self):

        self.file = Path("data/memory.json")

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8"
            )

    def add(self, memory):

        memories = self.get_all()

        memories.append(memory)

        data = []

        for m in memories:

            data.append({
                "memory_type": m.memory_type.value,
                "content": m.content,
                "created_at": m.created_at.isoformat(),
                "metadata": m.metadata
            })

        self.file.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )

    def get_all(self):

        raw = json.loads(
            self.file.read_text(
                encoding="utf-8"
            )
        )

        memories = []

        for item in raw:

            memories.append(
                Memory(
                    memory_type=MemoryType(
                        item["memory_type"]
                    ),
                    content=item["content"],
                    created_at=datetime.fromisoformat(
                        item["created_at"]
                    ),
                    metadata=item.get(
                        "metadata"
                    )
                )
            )

        return memories

    def clear(self):

        self.file.write_text(
            "[]",
            encoding="utf-8"
        )