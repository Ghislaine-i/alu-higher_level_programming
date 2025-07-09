#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size.
"""

class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
                        No type/value verification is performed at this stage.
        """
        self.__size = size

