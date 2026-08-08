#!/usr/bin/python3
"""Module containing the matrix_mul function."""


def matrix_mul(m_a, m_b):
        """Multiplies two matrices after thorough input validation.

            Args:
                        m_a (list of lists): The first matrix (integers or floats).
                                m_b (list of lists): The second matrix (integers or floats).

                                    Returns:
                                                list of lists: The resulting product matrix.

                                                    Raises:
                                                                TypeError: If m_a or m_b is not a list, not a list of lists,
                                                                                   contains non-integer/float elements, or rows are unequal.
                                                                                           ValueError: If m_a or m_b is empty, or if they cannot be multiplied.
                                                                                               """
                                                                                                   # 1. Check if m_a and m_b are lists
                                                                                                       if not isinstance(m_a, list):
                                                                                                               raise TypeError("m_a must be a list")
                                                                                                                   if not isinstance(m_b, list):
                                                                                                                           raise TypeError("m_b must be a list")

                                                                                                                               # 2. Check if m_a and m_b are list of lists
                                                                                                                                   if not all(isinstance(row, list) for row in m_a):
                                                                                                                                           raise TypeError("m_a must be a list of lists")
                                                                                                                                               if not all(isinstance(row, list) for row in m_b):
                                                                                                                                                       raise TypeError("m_b must be a list of lists")

                                                                                                                                                           # 3. Check if m_a or m_b is empty ([] or [[]])
                                                                                                                                                               if m_a == [] or m_a == [[]]:
                                                                                                                                                                       raise ValueError("m_a can't be empty")
                                                                                                                                                                           if m_b == [] or m_b == [[]]:
                                                                                                                                                                                   raise ValueError("m_b can't be empty")

                                                                                                                                                                                       # 4. Check if elements are integers or floats
                                                                                                                                                                                           for row in m_a:
                                                                                                                                                                                                   for elem in row:
                                                                                                                                                                                                               if type(elem) not in (int, float):
                                                                                                                                                                                                                               raise TypeError("m_a should contain only integers or floats")

                                                                                                                                                                                                                                   for row in m_b:
                                                                                                                                                                                                                                           for elem in row:
                                                                                                                                                                                                                                                       if type(elem) not in (int, float):
                                                                                                                                                                                                                                                                       raise TypeError("m_b should contain only integers or floats")

                                                                                                                                                                                                                                                                           # 5. Check if matrices are rectangular (all rows equal length)
                                                                                                                                                                                                                                                                               len_m_a = len(m_a[0])
                                                                                                                                                                                                                                                                                   if not all(len(row) == len_m_a for row in m_a):
                                                                                                                                                                                                                                                                                           raise TypeError("each row of m_a must be of the same size")

                                                                                                                                                                                                                                                                                               len_m_b = len(m_b[0])
                                                                                                                                                                                                                                                                                                   if not all(len(row) == len_m_b for row in m_b):
                                                                                                                                                                                                                                                                                                           raise TypeError("each row of m_b must be of the same size")

                                                                                                                                                                                                                                                                                                               # 6. Check if matrices can be multiplied (columns of m_a == rows of m_b)
                                                                                                                                                                                                                                                                                                                   if len_m_a != len(m_b):
                                                                                                                                                                                                                                                                                                                           raise ValueError("m_a and m_b can't be multiplied")

                                                                                                                                                                                                                                                                                                                               # Perform matrix multiplication
                                                                                                                                                                                                                                                                                                                                   result = []
                                                                                                                                                                                                                                                                                                                                       for i in range(len(m_a)):
                                                                                                                                                                                                                                                                                                                                               row_result = []
                                                                                                                                                                                                                                                                                                                                                       for j in range(len(m_b[0])):
                                                                                                                                                                                                                                                                                                                                                                   product_sum = 0
                                                                                                                                                                                                                                                                                                                                                                               for k in range(len(m_b)):
                                                                                                                                                                                                                                                                                                                                                                                               product_sum += m_a[i][k] * m_b[k][j]
                                                                                                                                                                                                                                                                                                                                                                                                           row_result.append(product_sum)
                                                                                                                                                                                                                                                                                                                                                                                                                   result.append(row_result)

                                                                                                                                                                                                                                                                                                                                                                                                                       return resulti
