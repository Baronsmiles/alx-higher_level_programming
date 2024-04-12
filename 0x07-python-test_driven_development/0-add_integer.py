#!/usr/bin/python3
"""Defines addition of integers function"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.
        
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    # Check if a and b are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b= int(b)

    # Return the sum of a and b
        return (int(a) + int(b))
