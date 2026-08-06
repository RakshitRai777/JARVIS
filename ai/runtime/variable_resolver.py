import re

from ai.runtime.runtime_variables import RuntimeVariables


class VariableResolver:
    """
    Resolves ${variable} placeholders using RuntimeVariables.

    Examples
    --------
    "Open ${browser}"
        -> "Open Chrome"

    "Search ${query}"
        -> "Search OpenAI"

    Future
    ------
    • Nested variables
    • Expressions
    • Default values
    • Environment variables
    """

    ############################################################

    VARIABLE_PATTERN = re.compile(

        r"\$\{([^}]+)\}"

    )

    ############################################################

    def __init__(
        self,
        variables: RuntimeVariables,
    ):

        self.variables = variables

    ############################################################

    def resolve(
        self,
        text: str,
    ) -> str:

        """
        Replace all ${variable} placeholders.
        """

        if not text:

            return text

        ########################################################

        def replace(match):

            name = match.group(1).strip()

            value = self.variables.get(

                name,

                match.group(0),

            )

            return str(value)

        ########################################################

        return self.VARIABLE_PATTERN.sub(

            replace,

            text,

        )

    ############################################################

    def contains_variables(
        self,
        text: str,
    ) -> bool:

        """
        Returns True if the string contains ${...}
        """

        if not text:

            return False

        return bool(

            self.VARIABLE_PATTERN.search(

                text,

            )

        )