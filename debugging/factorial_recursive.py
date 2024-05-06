#!/usr/bin/python3

import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer using recursion.

    Parameters:
    - n (int): The integer for which factorial is to be calculated.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command line argument parsing
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)