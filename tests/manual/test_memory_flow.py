from ai.brain.brain import Brain
from runtime.startup import initialize_runtime
initialize_runtime()
brain = Brain()

print("=" * 60)

print(brain.chat("My favourite colour is blue"))

print(brain.chat("I live in Uttarakhand"))

print(brain.chat("What is my favourite colour?"))

print(brain.chat("Where do I live?"))

print("=" * 60)