#!/usr/bin/python3
"""
Fixed version of print_square function.
Bug fixed: Added newline after each row with print()
"""

def print_square(size):
    """
    Print a square made of # characters.
    Fixed version with proper newlines.
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()  # Add newline after each row

if __name__ == "__main__":
    print_square(3)
    print()
    print_square(5)
