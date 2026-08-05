from ai.output.output_response import OutputResponse


class ResponsePipeline:
    """
    Processes responses before they leave JARVIS.

    Responsibilities
    ----------------
    • Personality
    • Voice formatting
    • Emotion
    • Response filtering
    """

    def process(
        self,
        response: OutputResponse,
    ) -> OutputResponse:

        # Future personality & voice processing.

        return response