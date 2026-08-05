from ai.llm_manager import LLMManager

llm = LLMManager()

print("Sending request...")

response = llm.generate(

    "Reply with exactly: Hello Boss."

)

print()

print(response)