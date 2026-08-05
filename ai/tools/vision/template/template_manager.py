from pathlib import Path

from ai.tools.vision.template.template_matcher import TemplateMatcher
from ai.tools.vision.template.template_result import TemplateResult


class TemplateManager:
    """
    Central manager for template matching.

    Responsibilities
    ----------------
    • Find one template
    • Find multiple templates (future)
    • Template cache (future)
    • Template library (future)
    • Hybrid matchers (future)
    """

    ############################################################

    def __init__(self):

        self.matcher = TemplateMatcher()

    ############################################################

    def find(
        self,
        image: str | Path,
        template: str | Path,
        threshold: float = 0.75,
    ) -> TemplateResult:
        """
        Find a single template.
        """

        return self.matcher.find(

            image=image,

            template=template,

            threshold=threshold,

        )