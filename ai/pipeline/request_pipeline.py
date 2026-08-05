from ai.input.input_event import InputEvent


class RequestPipeline:
    """
    Prepares an InputEvent for the Brain.

    Responsibilities
    ----------------
    • Validate requests
    • (Future)
      - Speech cleanup
      - Wake-word removal
      - Language detection
      - Profanity filtering
      - Session enrichment
    """

    def process(
        self,
        event: InputEvent,
    ) -> InputEvent:

        # Future preprocessing goes here.

        return event