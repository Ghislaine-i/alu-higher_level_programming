#!/usr/bin/python3
"""
This module defines a Rectangle class with private instance attributes for width and height,
including validation via properties, and methods to calculate area and perimeter,
and custom string representations for both print() and repr().
"""

class Rectangle:
    """
    Defines a rectangle by its width and height, providing controlled access via properties,
    and methods for area and perimeter calculations, and custom printing.

    Attributes:
        __width (int): The width of the rectangle (private instance attribute).
        __height (int): The height of the rectangle (private instance attribute).
        number_of_instances (int): A public class attribute to count active Rectangle instances.
    """
    number_of_instances = 0 # Initialize the class attribute to 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
                         Validation is handled by the width property setter.
            height (int): The height of the rectangle. Defaults to 0.
                          Validation is handled by the height property setter.
        """
        # Use setters to ensure validation is applied during instantiation
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1 # Increment instance count upon creation

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle instance.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle instance with validation.

        Args:
            value (int): The new width for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle instance.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle instance with validation.

        Args:
            value (int): The new height for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the current area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the current perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
                 Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the '#' character.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # Create a list of strings, where each string is a row of '#' characters
        # and then join them with newline characters.
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate a new instance using eval().
        The format is: Rectangle(width, height)
        """
        return f"Rectangle({s
