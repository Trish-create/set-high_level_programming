#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """A class that defines a square."""

      def__init__(self, size=0):
            """Initialize a Square with a given size."""
            self.size = size

        @property
        def size(self):
            """Get the size of the square."""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the square after validation."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                 raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return the current square area."""
            return self.__size ** 2
