#!/usr/bin/python3
"""Defines say_my_name function"""

def say_my_name(first_name, last_name=""):
"""
    Prints a string with the provided first name and last names.

    Args:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to "".

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

        print("My name is {} {}".format(first_name, last_name))
