import re


class GoalParser:
    """
    Splits a natural language command into
    individual goals.

    This is Planner v2.

    Future versions may use an LLM.
    """

    ############################################################

    def parse(
        self,
        command: str,
    ) -> list[str]:

        text = command.strip()

        ########################################################
        # Normalize separators
        ########################################################

        text = re.sub(

            r"\bthen\b",

            " and ",

            text,

            flags=re.IGNORECASE,

        )

        ########################################################

        parts = re.split(

            r"\band\b|,",

            text,

            flags=re.IGNORECASE,

        )

        ########################################################

        return [

            part.strip()

            for part in parts

            if part.strip()

        ]