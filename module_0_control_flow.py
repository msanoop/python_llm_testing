"""
Module 0: Python Fundamentals (Basics)
Lesson 2: Control Flow (If/Else, Loops) - Deep Dive

In this file, we explore more complex control flow patterns
that you'll use when building automated tests for LLMs.
"""

# ---------------------------------------------------------
# 1. Advanced Conditionals: Nested If and Elif
# ---------------------------------------------------------
print("--- 1. Advanced Conditionals ---")

response_status = 200  # API Success
response_text = "The AI is ready to help."

if response_status == 200:
    if "AI" in response_text:
        print("Success: API returned valid AI content.")
    else:
        print("Warning: API succeeded but content is unexpected.")
elif response_status == 429:
    print("Error: Rate limit exceeded. Need to retry.")
else:
    print(f"Error: Received status code {response_status}")

# ---------------------------------------------------------
# 2. While Loops: Dealing with Retries
# ---------------------------------------------------------
print("\n--- 2. While Loops (Retry Logic) ---")

attempts = 0
max_retries = 3
success = False

while attempts < max_retries and not success:
    attempts += 1
    print(f"Connecting to LLM (Attempt {attempts})...")
    
    # Simulating a success on the 3rd attempt
    if attempts == 3:
        success = True
        print("Connected successfully!")
    else:
        print("Connection failed. Retrying...")

# ---------------------------------------------------------
# 3. Break and Continue
# ---------------------------------------------------------
print("\n--- 3. Break and Continue ---")

responses = ["Hello", "ERROR: Timeout", "How are you?", "STOP", "The sun is hot."]

print("Processing responses:")
for res in responses:
    if "ERROR" in res:
        print(f"  Skipping: {res}")
        continue  # Skip to the next iteration
    
    if res == "STOP":
        print("  Stop signal received. Ending loop.")
        break  # Exit the loop entirely
        
    print(f"  Valid Response: {res}")

# ---------------------------------------------------------
# 4. Iterating over Dictionaries
# ---------------------------------------------------------
print("\n--- 4. Iterating over Dictionaries ---")

llm_metadata = {
    "model": "Gemini-Pro",
    "version": "1.5",
    "region": "us-central1",
    "latency": 0.45
}

for key, value in llm_metadata.items():
    print(f"Field: {key:10} | Value: {value}")

# ---------------------------------------------------------
# FINAL CHALLENGE:
# 1. Create a list of numbers from 1 to 10.
# 2. Loop through them.
# 3. Print "Even" if the number is even, and "Odd" if it is odd.
# Hint: Use the modulo operator (%) -> (number % 2 == 0) means even.
# ---------------------------------------------------------

# Write your code below:
