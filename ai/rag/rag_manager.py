from ai.rag.answer_generator import AnswerGenerator


class RAGManager:
    """
    Generates grounded answers from already retrieved chunks.

    It DOES NOT retrieve knowledge itself.
    """

    def __init__(self):

        self.generator = AnswerGenerator()

    ##########################################################

    def answer(

        self,

        question: str,

        chunks,

    ) -> str:

        return self.generator.generate(

            question=question,

            chunks=chunks,

        )