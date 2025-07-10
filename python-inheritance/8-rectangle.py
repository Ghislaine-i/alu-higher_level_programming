#!/usr/bin/python3
"""
This module defines the BaseGeometry class and an integer validation function.
"""

class BaseGeometry:
    """
    A base class for geometric shapes, providing common validation.
    """
    def area(self):
        """
        Raises an Exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer and is positive.

        Args:
            name (str): The name of the value (e.g., "width", "height").
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not positive (> 0).
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0: # For dimensions like width/height, they must be positive
            raise ValueError(f"{name} must be greater than 0")
