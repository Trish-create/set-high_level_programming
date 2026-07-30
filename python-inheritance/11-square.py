#!/usr/bin/python3
"""Module that defines the Square class."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
        """Square class."""

            def __init__(self, size):
                        """Initialize a Square."""
                                self.integer_validator("size", size)
                                        super().__init__(size, size)

                                            def __str__(self):
                                                        """Return the square description."""
                                                                return "[Square] {}/{}".format(
                                                                                    self._Rectangle__width,
                                                                                                self._Rectangle__height
                                                                                                        )
