"""Module containing the lazy_matrix_mul function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        ndarray: Matrix result of the multiplication.
    """
    return np.matmul(m_a, m_b)
