#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """A class that defines a square."""

        def__init__(self, size=0, position=(0, 0)):
            """Initialize a Square."""
            self.size = size
            self.position = position

        @property
        def size(self):
            """Retrieve the size."""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size after validation."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")

            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value

        @property
        def position(self):
            """Retrieve the position."""
                return self.__position

        @position.setter
        def position(self, value):
            """Set the position after validation."""
            if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0
                or value[1] < 0
                                                                                                    ):
                raise TypeError("position must be a tuple of 2 positive integers")

            self.__position = value

        def area(self):
            """Return the area of the square."""
            return self.__size ** 2

        def my_print(self):
            """Print the square using # at the given position."""
            if self.__size == 0:
                print()
                return

            # Print blank lines first
            for _ in range(self.__position[1]):
                print()

            # Print the square
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
