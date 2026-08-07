from ai.project.project_status import ProjectStatus


def main():

    print("=" * 60)
    print("PROJECT STATUS")
    print("=" * 60)

    for status in ProjectStatus:

        print(

            status.name,

            "=",

            status.value,

        )


if __name__ == "__main__":

    main()