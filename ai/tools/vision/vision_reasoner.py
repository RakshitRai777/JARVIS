from ai.llm_manager import LLMManager

from ai.tools.vision.vision_prompts import VisionPrompts
from ai.tools.vision.vision_result import VisionResult


class VisionReasoner:
    """
    Performs high-level reasoning on VisionResults.

    This class is responsible for converting
    OCR output into natural-language understanding
    using the configured LLM.

    Vision tools should never communicate directly
    with the LLM.
    """

    ############################################################

    def __init__(self):

        self.llm = LLMManager()

    ############################################################

    def explain(
        self,
        vision_result: VisionResult,
    ) -> str:

        ########################################################
        # Build Prompt
        ########################################################

        prompt = VisionPrompts.explain_screen(

            vision_result.cleaned_text

        )

        ########################################################
        # Ask LLM
        ########################################################

        response = self.llm.generate(

            prompt

        )

        ########################################################

        return response