from runtime.startup import initialize_runtime

from ai.brain.brain import Brain


def run():

    initialize_runtime()

    brain = Brain()

    print("=" * 60)
    print("TOOL TEST")
    print("=" * 60)

    commands = [
        "Open Chrome",
        "open chrome",
        "OPEN CHROME"
    ]

    for command in commands:

        print()

        print(f"USER : {command}")

        reply = brain.chat(command)

        print(f"JARVIS : {reply}")


if __name__ == "__main__":
    run()