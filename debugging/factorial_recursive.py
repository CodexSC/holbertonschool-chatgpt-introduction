#!/usr/bin/python3
import sys

def factorial(n):

    """
    Calculate the factorial of a given number"

    Parameters:
    n (int): The number for which the factorial is to be calculated."

    Returns:
        int: The factorial of the given number.
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n==0:
            return 1
    else:
        return n * factorial(n-1)
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError as e:
    print(f"Error: {str(e)}")
except IndexError:
    print("Error: No argument provided")

