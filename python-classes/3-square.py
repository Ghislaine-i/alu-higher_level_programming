#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size,
including validation for type and value, and a method to calculate its area.
"""

class Square:
    """
    Defines a square by its size and provides area computation.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
