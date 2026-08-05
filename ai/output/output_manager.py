from ai.output.output_channel import OutputChannel
from ai.output.output_response import OutputResponse


class OutputManager:
    """
    Converts Brain responses into OutputResponse objects.
    """

    ############################################################

    def create_response(
        self,
        text: str,
        channel: OutputChannel = OutputChannel.CONSOLE,
        metadata: dict | None = None,
    ) -> OutputResponse:

        return OutputResponse(

            text=text,

            channel=channel,

            metadata=metadata,

        )