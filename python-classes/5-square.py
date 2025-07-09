#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size,
including validation for type and value, and methods to get, set, calculate its area,
and print the square.
"""

class Square:
    """
    Defines a square by its size, providing controlled access via properties
    and area computation, and a method to print the square.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
                        Validation is handled by the size property setter.
        """
        # Use the setter to ensure validation is applied during instantiation
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the Square instance.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square instance with validation.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout with the character '#'.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print() # Print an empty line
        else:
            for _ in range(self.__size): # Loop for each row
                print("#" * self.__size) # Print '#' character 'size' times for each row

