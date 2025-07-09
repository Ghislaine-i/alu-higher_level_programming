#!/usr/bin/python3
"""
This module defines a Square class with private instance attributes for size and position,
including validation for their types and values, and methods to get, set, calculate its area,
and print the square with position.
"""

class Square:
    """
    Defines a square by its size and position, providing controlled access via properties,
    area computation, and a method to print the square.

    Attributes:
        __size (int): The size of the square (private instance attribute).
        __position (tuple): The position of the square (private instance attribute, tuple of 2 positive integers).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
                        Validation is handled by the size property setter.
            position (tuple): The position of the square (x, y coordinates). Defaults to (0, 0).
                              Validation is handled by the position property setter.
        """
        # Use setters to ensure validation is applied during instantiation
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the Square instance.

        Returns:
            tuple: The current position (x, y) of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the Square instance with validation.

        Args:
            value (tuple): The new position (x, y) for the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout with the character '#',
        considering its position.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print() # Print an empty line if size is 0
            return # Exit the method

        # Print vertical offset (empty lines) determined by position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square rows, each with horizontal offset (spaces)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
