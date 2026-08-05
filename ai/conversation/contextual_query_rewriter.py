from ai.conversation.rewrite_result import RewriteResult
from ai.llm_manager import LLMManager


class ContextualQueryRewriter:
    """
    Uses the LLM to rewrite conversational queries into
    standalone questions.
    """

    ##########################################################

    def __init__(self):

        self.llm = LLMManager()

    ##########################################################

    def rewrite(
        self,
        conversation,
        query: str,
    ) -> RewriteResult:

        ######################################################
        # Build recent history
        ######################################################

        history = conversation.history()

        recent = history[-6:]

        transcript = []

        for message in recent:

            role = message.role.capitalize()

            transcript.append(
                f"{role}: {message.content}"
            )

        transcript = "\n".join(transcript)

        ######################################################
        # Prompt
        ######################################################

        prompt = f"""
You rewrite conversational questions.

Rewrite ONLY if the user's latest question depends on previous conversation.

Rules:

- Preserve the meaning.
- Resolve pronouns like he, she, they, it, this company, this language.
- Produce ONE standalone question.
- Do not answer.
- If already standalone, return it unchanged.

Conversation:

{transcript}

Latest Question:

{query}

Standalone Question:
"""

        ######################################################

        messages = [

            {

                "role": "system",

                "content": (
                    "You are a contextual query rewriter."
                )

            },

            {

                "role": "user",

                "content": prompt

            }

        ]

        rewritten = self.llm.generate(messages).strip()

        ######################################################

        if not rewritten:

            rewritten = query

        ######################################################

        return RewriteResult(

            original_query=query,

            rewritten_query=rewritten,

            changed=(
                rewritten.lower().strip()
                != query.lower().strip()
            ),

            reason="LLM contextual rewrite."

        )