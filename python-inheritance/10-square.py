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
        print_symbol (any): A public class attribute used as the symbol for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(Rectangle.print_symbol) * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

