from dataclasses import dataclass, field
from typing import Any


@dataclass
class WebResult:
    """
    Represents the result of a web search or retrieval.

    This object is passed throughout the entire web pipeline.
    """

    success: bool = False

    title: str = ""

    url: str = ""

    snippet: str = ""

    content: str = ""

    source: str = ""

    error: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)