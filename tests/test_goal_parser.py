from ai.planner.goal_parser import GoalParser


def main():

    parser = GoalParser()

    commands = [

        "Open Chrome and search Google",

        "Open Notepad then type Hello",

        "Open Chrome, search OpenAI, click first result",

    ]

    for command in commands:

        print()

        print(command)

        print(parser.parse(command))


if __name__ == "__main__":

    main()