from ai.brain.brain import Brain
from runtime.runtime import runtime


def run():

    print("=" * 60)
    print("BRAIN TEST")
    print("=" * 60)

    # Get the shared MemoryService from the Runtime
    memory_service = runtime.services.get("memory")

    # Start every test with a clean memory store
    memory_service.clear()

    brain = Brain()

    tests = [
        "Remember my favourite colour is blue",
        "Remember I live in Uttarakhand",
        "Remember my dog's name is Bruno"
    ]

    for text in tests:

        print()
        print(f"USER : {text}")

        reply = brain.chat(text)

        print(f"JARVIS : {reply}")

    print()
    print("=" * 60)
    print("WORKING MEMORY")
    print("=" * 60)

    for memory in memory_service.get_all():

        print(memory.content)

    print()
    print("=" * 60)