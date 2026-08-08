#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: List of lists containing integers or floats.
        div: Number to divide every element by.

    Returns:
        A new matrix with divided values rounded to 2 decimals.

    Raises:
        TypeError: If matrix or div is invalid.
        ZeroDivisionError: If div is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(error)

    row_size = len(matrix[0])

    for row in matrix:
            if len(row) != row_size:
                raise TypeError(
                    "Each row of the matrix must have the same size"
                )

            for value in row:
                if not isinstance(value, (int, float)):
                    raise TypeError(error)

    return [
        [round(value / div, 2) for value in row]
        for row in matrix
                                                                                                    ]
