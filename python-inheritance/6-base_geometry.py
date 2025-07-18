#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""

class BaseGeometry:
    """
    A base class for geometric shapes.
    """
    def area(self):
        """
        Raises an Exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

