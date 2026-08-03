from runtime.startup import initialize_runtime
from ai.brain.brain import Brain


initialize_runtime()

brain = Brain()

print("=" * 60)
print("JARVIS v0.6")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    user = input("\nYou : ")

    if user.lower() in ["exit", "quit"]:
        print("\nJARVIS : Goodbye, Sir.")
        break

    reply = brain.chat(user)

    print(f"\nJARVIS : {reply}")