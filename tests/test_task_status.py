from ai.project.task_status import TaskStatus


def main():

    print("=" * 60)
    print("TASK STATUS")
    print("=" * 60)

    for status in TaskStatus:

        print(

            status.name,

            "=",

            status.value,

        )


if __name__ == "__main__":

    main()