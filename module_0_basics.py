"""
Module 0: Python Fundamentals (Basics)
Lesson 1: Variables and Data Types

In Python, we use variables to store data. Unlike other languages, 
you don't need to declare the type of a variable.
"""

# ---------------------------------------------------------
# 1. Variables and Assignment
# ---------------------------------------------------------

# Strings (Text) - used for prompts, responses, etc.
model_name = "GPT-4"
user_prompt = 'Explain Python like I am five.'

# Integers (Whole numbers) - used for token counts, retries
max_tokens = 256
retry_count = 3

# Floats (Decimal numbers) - used for temperature, probability scores
temperature = 0.7
confidence_score = 0.95

# Booleans (True/False) - used for status checks
is_active = True
has_errors = False

# ---------------------------------------------------------
# 2. Printing and Type Checking
# ---------------------------------------------------------

print("--- Variables and Types ---")
print(f"Model: {model_name} (Type: {type(model_name)})")
print(f"Temperature: {temperature} (Type: {type(temperature)})")
print(f"Is Active: {is_active} (Type: {type(is_active)})")

# ---------------------------------------------------------
# 3. Basic String Operations (Crucial for LLM Testing)
# ---------------------------------------------------------

# Concatenation
full_prompt = "User asked: " + user_prompt
print(f"\nFull Prompt: {full_prompt}")

# Multi-line strings (Triple quotes) - Great for long prompts
system_instruction = """
You are a helpful assistant specialized in software testing.
Please avoid using jargon and provide code examples.
"""
print(f"\nSystem Instruction:\n{system_instruction.strip()}")
print(f"\nSystem Instruction:\n{system_instruction.strip().upper()}\n")

# ---------------------------------------------------------
# EXERCISE: 
# 1. Create a variable for an LLM response (string).
# 2. Create a variable for a response length (integer).
# 3. Print a message combining them using an f-string.
# ---------------------------------------------------------

# Write your code below:
llm_response = "The capital of France is Paris."
response_length = len(llm_response)
print(f"Response: {llm_response} | Length: {response_length}")

# ---------------------------------------------------------
# Lesson 2: Control Flow (if/else, loops)
# ---------------------------------------------------------

# 1. Conditionals (if, elif, else)
# This is how we test if an LLM output meets certain criteria.

print("\n--- Lesson 2: Control Flow ---")

predicted_sentiment = "positive"
confidence = 0.85

if confidence > 0.9:
    print("Action: High confidence. Proceed.")
elif confidence > 0.7:
    print("Action: Medium confidence. Review required.")
else:
    print("Action: Low confidence. Reject.")

# 2. Logical Operators (and, or, not)
is_valid = True
contains_profanity = False

if is_valid and not contains_profanity:
    print("Test Passed: Output is safe and valid.")

# 3. Loops (for)
# Useful for running multiple tests or processing multiple prompts.

test_prompts = [
    "What is AI?",
    "Tell me a joke.",
    "how to bake a cake?"
]

print("\nRunning test prompts:")
for prompt in test_prompts:
    print(f"- Processing prompt: {prompt}")

# 4. Range
print("\nRetrying an API call:")
for attempt in range(1, 4):  # 1 to 3
    print(f"  Attempt {attempt}...")

# ---------------------------------------------------------
# EXERCISE:
# 1. Create a list called `test_scores` with numbers [0.9, 0.4, 0.7].
# 2. Use a 'for' loop to go through the list.
# 3. Inside the loop, use 'if' to print "PASS" if the score is > 0.5,
#    otherwise print "FAIL".
# ---------------------------------------------------------

# Write your code below:
