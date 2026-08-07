from ai.agent.goal_status import GoalStatus


def main():

    print("=" * 60)
    print("GOAL STATUS")
    print("=" * 60)

    for status in GoalStatus:

        print(

            status.name,

            "=",

            status.value,

        )


if __name__ == "__main__":

    main()