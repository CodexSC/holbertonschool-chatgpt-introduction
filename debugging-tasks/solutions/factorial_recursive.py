#!/usr/bin/python3
"""
Fixed version of factorial calculation.
Bug fixed: Changed base case from n == 1 to n <= 1 to handle n=0
and changed recursion from factorial(n) to factorial(n-1)
"""

def factorial(n):
    """
    Calculate factorial of n recursively.
    Fixed version with proper base case and recursion.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Factorial of 0:", factorial(0))
    print("Factorial of 1:", factorial(1))
