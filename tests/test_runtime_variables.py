from ai.runtime.runtime import Runtime


def main():

    runtime = Runtime()

    variables = runtime.runtime_variables

    print("=" * 60)
    print("INITIAL")
    print("=" * 60)

    print("Count :", len(variables))

    ############################################################

    variables.set(

        "window",

        "Notepad",

    )

    variables.set(

        "count",

        5,

    )

    ############################################################

    print()
    print("=" * 60)
    print("AFTER SET")
    print("=" * 60)

    print("Window :", variables.get("window"))

    print("Count :", variables.get("count"))

    print("Exists :", variables.exists("window"))

    print("Total :", len(variables))

    ############################################################

    variables.remove(

        "count",

    )

    ############################################################

    print()
    print("=" * 60)
    print("AFTER REMOVE")
    print("=" * 60)

    print("Total :", len(variables))

    ############################################################

    runtime.reset()

    ############################################################

    print()
    print("=" * 60)
    print("AFTER RESET")
    print("=" * 60)

    print(

        "Total :",

        len(

            runtime.runtime_variables,

        ),

    )


if __name__ == "__main__":

    main()