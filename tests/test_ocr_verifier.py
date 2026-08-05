from ai.verification.verification_manager import VerificationManager
from ai.verification.verification_rule import VerificationRule

manager = VerificationManager()

rule = VerificationRule(

    rule_type="text_exists",

    expected="ChatGPT"

)

result = manager.verify(

    rule

)

print()

print(result)

print()

print("Confidence:", result.confidence)