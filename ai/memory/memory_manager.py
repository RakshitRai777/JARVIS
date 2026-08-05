from ai.embeddings.embedding_model import EmbeddingModel
from ai.embeddings.similarity import cosine_similarity

from ai.memory.stores.json_memory_store import JsonMemoryStore
from ai.memory.search import MemorySearch
from ai.memory.update.memory_updater import MemoryUpdater

class MemoryManager:

    ############################################################

    def __init__(self):

        self.store = JsonMemoryStore()
        self.updater = MemoryUpdater()

    ############################################################

    def add(self, memory):

        self.store.add(memory)

    def update(self, memory):

        memories = self.store.get_all()

        updated = self.updater.update(

            memories,

            memory,

        )

        if updated is None:

            return False

        self.store.save_all(memories)

        return True

    ############################################################

    def get_all(self):

        return self.store.get_all()

    ############################################################

    def clear(self):

        self.store.clear()

    ############################################################

    def count(self):

        return len(
            self.store.get_all()
        )

    ############################################################

    def exists(self, memory):

        content = memory.content.strip().lower()

        for existing in self.store.get_all():

            if existing.content.strip().lower() == content:

                return True

        return False

    ############################################################

    def find(
        self,
        query: str,
        top_k: int = 5,
    ):

        memories = self.store.get_all()

        if not memories:
            return []

        ########################################################
        # Embed query
        ########################################################

        query_embedding = EmbeddingModel.encode(query)

        ########################################################
        # Keyword extraction
        ########################################################

        keywords = MemorySearch.keywords(query)

        ########################################################

        scored = []

        for memory in memories:

            ###############################################
            # Skip memories without embeddings
            ###############################################

            if memory.embedding is None:
                continue

            ###############################################
            # Semantic similarity
            ###############################################

            semantic = cosine_similarity(

                query_embedding,

                memory.embedding,

            )

            ###############################################
            # Keyword score
            ###############################################

            content = memory.content.lower()

            keyword_hits = 0

            for keyword in keywords:

                if keyword in content:
                    keyword_hits += 1

            keyword_score = keyword_hits / max(
                len(keywords),
                1,
            )

            ###############################################
            # Hybrid score
            ###############################################

            score = (

                semantic * 0.80 +

                keyword_score * 0.20

            )

            scored.append(

                (

                    score,

                    memory,

                )

            )

        ########################################################

        scored.sort(

            key=lambda x: x[0],

            reverse=True,

        )

        ########################################################
        # Debug
        ########################################################

        print()

        print("[Memory Search]")

        for score, memory in scored[:top_k]:

            print(

                f"{score:.3f} | "

                f"{memory.content}"

            )

        print()

        ########################################################

        return [

            memory

            for score, memory in scored[:top_k]

            if score > 0.35

        ]