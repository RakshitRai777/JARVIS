from dataclasses import dataclass

from ai.output.output_channel import OutputChannel


@dataclass
class OutputResponse:
    """
    A normalized JARVIS response.

    Every response leaving the Brain
    becomes an OutputResponse.
    """

    ############################################################

    text: str

    ############################################################

    channel: OutputChannel

    ############################################################

    metadata: dict | None = None