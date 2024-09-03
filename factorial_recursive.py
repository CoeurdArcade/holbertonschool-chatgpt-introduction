#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    - n (int): The integer for which the factorial is calculated.

    Returns:
    - int: The factorial of the input integer.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: multiply n by factorial of (n-1)
        return n * factorial(n-1)

# Extract the command-line argument provided by the user
# and convert it to an integer to compute the factorial
argument = int(sys.argv[1])

# Calculate the factorial of the provided integer
result = factorial(argument)

# Print the factorial result
print(result)
