class VisionPrompts:
    """
    Centralized prompts used by the Vision Engine.

    Every Vision tool should obtain its prompt
    from this class instead of embedding prompts
    directly into the tool.
    """

    ############################################################

    @staticmethod
    def explain_screen(
        screen_text: str,
    ) -> str:

        return f"""
You are JARVIS Vision.

The following text was extracted from the user's
current screen using OCR.

Your job is to explain what the user is currently
looking at.

Instructions:

- Identify the application if possible.
- Identify the user's current activity.
- Ignore OCR mistakes.
- Combine fragmented text naturally.
- Produce a concise explanation.
- Use bullet points when helpful.
- Do not invent information that is not supported
  by the OCR.

OCR TEXT
========

{screen_text}

========

Provide a helpful explanation.
"""