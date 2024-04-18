#!/usr/bin/python3

class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str): List of attributes to retrieve. If None, retrieves all attributes.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

