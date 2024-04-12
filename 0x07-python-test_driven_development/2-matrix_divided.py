#!/usr/bin/python3
"""Defines Division of matrix function"""

def matrix_divided(matrix, div)i:
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor.
    
    Returns:
    list of lists: The new matrix with elements divided by the divisor.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
     # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
