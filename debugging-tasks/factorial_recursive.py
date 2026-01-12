#!/usr/bin/python3
"""
This script contains a buggy implementation of factorial calculation.
Use ChatGPT to identify and fix the bug.
"""

def factorial(n):
    """
    Calculate factorial of n recursively.
    Contains a bug - can you find it with ChatGPT's help?
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n)

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
