from ai.memory.stores.json_memory_store import JsonMemoryStore
from ai.memory.search import MemorySearch


class MemoryManager:

    def __init__(self):

        self.store = JsonMemoryStore()

    def add(self, memory):

        self.store.add(memory)

    def get_all(self):

        return self.store.get_all()

    def clear(self):

        self.store.clear()

    def count(self):

        return len(
            self.store.get_all()
        )

    def exists(self, memory):

        content = memory.content.strip().lower()

        for existing in self.store.get_all():

            if existing.content.strip().lower() == content:

                return True

        return False

    def find(self, query: str):

        keywords = MemorySearch.keywords(query)

        matches = []

        for memory in self.store.get_all():

            content = memory.content.lower()

            score = 0

            for keyword in keywords:

                if keyword in content:

                    score += 1

            if score > 0:

                matches.append(
                    (
                        score,
                        memory
                    )
                )

        matches.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [
            memory
            for _, memory in matches
        ]