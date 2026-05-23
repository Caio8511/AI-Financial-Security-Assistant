print("===================================")
print(" AI Financial Security Assistant ")
print("===================================")

print("\nWelcome to the AI Financial Security Assistant.\n")

question = input("Ask something about financial security: ")

responses = {
    "fraud": "Warning: Monitor suspicious transactions and unknown activities.",
    "phishing": "Never click on suspicious emails or fake banking links.",
    "mfa": "Enable Multi-Factor Authentication to improve account security.",
    "password": "Use strong passwords with numbers and symbols."
}

found = False

for keyword in responses:
    if keyword in question.lower():
        print("\nAI Response:")
        print(responses[keyword])
        found = True

if not found:
    print("\nAI Response:")
    print("Security recommendation generated successfully.")