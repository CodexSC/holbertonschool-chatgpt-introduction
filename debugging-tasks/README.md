# Debugging Tasks

This directory contains examples of buggy code to help you learn how to use ChatGPT for debugging.

## Learning Objectives

- Learn to identify common programming errors
- Practice using ChatGPT to debug code efficiently
- Understand how to ask ChatGPT effective debugging questions
- Develop systematic debugging approaches

## Tasks

### Task 1: Factorial Recursive Bug
**File**: `factorial_recursive.py`

This script calculates factorial recursively but contains bugs.

**How to use ChatGPT**:
1. Run the script and observe the error
2. Copy the error message and code to ChatGPT
3. Ask: "I'm getting this error in my Python code. Can you help me debug it?"
4. Follow ChatGPT's suggestions and understand the fix

**Expected behavior**: Should calculate factorial correctly (e.g., 5! = 120)

### Task 2: Print Square Bug
**File**: `print_square.py`

This script prints a square of # characters but doesn't display correctly.

**How to use ChatGPT**:
1. Run the script and observe the output
2. Share the code with ChatGPT
3. Ask: "This code should print a square but the output is wrong. What's the issue?"
4. Apply the suggested fix

**Expected behavior**: Should print proper squares with rows and columns

### Task 3: Bash Script Bug
**File**: `change_directory.sh`

This bash script attempts to change directories but may fail.

**How to use ChatGPT**:
1. Run the script and observe the behavior
2. Ask ChatGPT: "This bash script fails when the directory doesn't exist. How can I add error handling?"
3. Implement the suggested improvements

**Expected behavior**: Should handle non-existent directories gracefully

## Solutions

Check the `solutions/` directory for fixed versions of all scripts. Try to fix them yourself first before looking at the solutions!

## Tips for Using ChatGPT for Debugging

1. **Provide context**: Include the error message, relevant code, and what you expected to happen
2. **Be specific**: Describe the exact problem you're facing
3. **Ask follow-up questions**: If you don't understand the fix, ask ChatGPT to explain
4. **Test incrementally**: Apply one fix at a time and test
5. **Learn the pattern**: Try to understand why the bug occurred to avoid similar issues

## Example ChatGPT Prompts

- "I'm getting a RecursionError in my Python factorial function. Here's my code: [paste code]. What's wrong?"
- "My Python script prints output on one line instead of multiple lines. Can you help me fix it?"
- "How can I add error handling to a bash script that changes directories?"
- "Can you explain why [specific code] causes [specific error]?"
