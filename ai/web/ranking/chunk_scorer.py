from dataclasses import dataclass


@dataclass
class ChunkScore:

    semantic: float = 0.0

    keyword: float = 0.0

    entity: float = 0.0

    title: float = 0.0

    authority: float = 0.0

    freshness: float = 0.0

    ######################################################

    @property
    def total(self):

        return (

            0.40 * self.semantic +

            0.20 * self.keyword +

            0.15 * self.entity +

            0.10 * self.title +

            0.10 * self.authority +

            0.05 * self.freshness

        )