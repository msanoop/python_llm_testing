# Learning Path: Python for LLM Testing

This plan is designed to transition you from general Python knowledge to specialized skills in testing Large Language Models (LLMs).

## Proposed Changes

### Module 0: Python Fundamentals (Basics)
Before diving into testing, we will cover the essential building blocks.
- **[NEW] [module_0_basics.py](file:///C:/Users/msano/.gemini/antigravity/scratch/python_llm_testing/module_0_basics.py)**: Covering variables, data types, loops, and functions.

### Module 1: Python for Automation & Testing
Transitioning basics into professional testing patterns.
- **[NEW] [module_1_pytest.py](file:///C:/Users/msano/.gemini/antigravity/scratch/python_llm_testing/module_1_pytest.py)**: Exercises focusing on `pytest`, fixtures, and assertions.

### LLM Integration
Learning how to programmatically interact with LLMs.
- **[NEW] [module_2_llm_api.py](file:///C:/Users/msano/.gemini/antigravity/scratch/python_llm_testing/module_2_llm_api.py)**: Handling API calls, environment variables, and asynchronous execution.

### Evaluation Strategies
The core of LLM testing: how to judge model output.
- **[NEW] [module_3_evals.py](file:///C:/Users/msano/.gemini/antigravity/scratch/python_llm_testing/module_3_evals.py)**: Implementing metrics like BLEU, ROUGE, and using LLM-as-a-judge patterns.

## Verification Plan

### Automated Tests
- We will use `pytest` to run our own test suites.
- We will verify API connectivity using mock responses to save costs.

### Manual Verification
- Reviewing LLM outputs to compare against automated evaluation scores.
