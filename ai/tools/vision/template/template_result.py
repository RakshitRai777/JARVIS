from dataclasses import dataclass, field

from ai.tools.vision.template.template_match import TemplateMatch


@dataclass(slots=True)
class TemplateResult:
    """
    Result returned by the template matching engine.

    Contains the best match along with every
    detected match.

    Future
    ------
    • Multiple templates
    • Matching statistics
    • Scale information
    • Rotation information
    """

    ############################################################

    success: bool

    ############################################################

    best_match: TemplateMatch | None = None

    ############################################################

    matches: list[TemplateMatch] = field(

        default_factory=list

    )

    ############################################################

    execution_time: float = 0.0

    ############################################################

    error: str | None = None

    ############################################################

    @property
    def confidence(self) -> float:

        if self.best_match is None:

            return 0.0

        return self.best_match.confidence

    ############################################################

    @property
    def match_count(self) -> int:

        return len(

            self.matches

        )

    ############################################################

    def __bool__(self):

        return self.success

    ############################################################

    def __str__(self):

        return (

            f"TemplateResult("

            f"success={self.success}, "

            f"matches={self.match_count}, "

            f"confidence={self.confidence:.3f}"

            f")"

        )