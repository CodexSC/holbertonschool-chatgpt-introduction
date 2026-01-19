#!/usr/bin/python3
"""
This script prints a square of a given size.
Contains a bug - use ChatGPT to help debug it.
"""

def print_square(size):
    """
    Print a square made of # characters.
    There's a bug here - can you find it?
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")

if __name__ == "__main__":
    print_square(3)
    print()
    print_square(5)
