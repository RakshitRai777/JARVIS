from ai.web.pipeline.web_pipeline import WebPipeline


class WebKnowledge:
    """
    Handles knowledge retrieval from the web.
    """

    ##########################################################

    def __init__(self):

        self.pipeline = WebPipeline()

    ##########################################################

    def search(
        self,
        question: str,
    ):

        return self.pipeline.retrieve(question)