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

# ---------------------------------------------------------
# EXERCISE: 
# 1. Create a variable for an LLM response (string).
# 2. Create a variable for a response length (integer).
# 3. Print a message combining them using an f-string.
# ---------------------------------------------------------

# Write your code below:
# llm_response = ...
