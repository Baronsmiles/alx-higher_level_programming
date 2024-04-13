#!/usr/bin/python3
"""Define lazy_matrix_mul funtion"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    numpy.ndarray: The resulting matrix after multiplication.

    Raises:
    ValueError: If the matrices cannot be multiplied.
    """
    # Convert input matrices to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Perform matrix multiplication
    result = np.matmul(np_a, np_b)

    return result.tolist()
