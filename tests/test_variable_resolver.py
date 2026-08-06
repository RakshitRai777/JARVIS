from ai.runtime.runtime_variables import RuntimeVariables
from ai.runtime.variable_resolver import VariableResolver


def main():

    variables = RuntimeVariables()

    ############################################################

    variables.set(

        "browser",

        "Chrome",

    )

    variables.set(

        "query",

        "OpenAI GPT-5",

    )

    variables.set(

        "user",

        "Rakshit",

    )

    ############################################################

    resolver = VariableResolver(

        variables,

    )

    ############################################################

    print("=" * 60)
    print("SINGLE VARIABLE")
    print("=" * 60)

    text = "Open ${browser}"

    print("Before :", text)

    print("After  :", resolver.resolve(text))

    ############################################################

    print()
    print("=" * 60)
    print("MULTIPLE VARIABLES")
    print("=" * 60)

    text = "Search ${query} using ${browser}"

    print("Before :", text)

    print("After  :", resolver.resolve(text))

    ############################################################

    print()
    print("=" * 60)
    print("UNKNOWN VARIABLE")
    print("=" * 60)

    text = "Hello ${username}"

    print("Before :", text)

    print("After  :", resolver.resolve(text))

    ############################################################

    print()
    print("=" * 60)
    print("NO VARIABLES")
    print("=" * 60)

    text = "Open Notepad"

    print("Before :", text)

    print("After  :", resolver.resolve(text))

    ############################################################

    print()
    print("=" * 60)
    print("CONTAINS VARIABLES")
    print("=" * 60)

    print(

        resolver.contains_variables(

            "Open ${browser}"

        )

    )

    print(

        resolver.contains_variables(

            "Open Notepad"

        )

    )


if __name__ == "__main__":
    main()