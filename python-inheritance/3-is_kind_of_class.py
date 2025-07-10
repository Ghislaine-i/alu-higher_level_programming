#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or inherited from, a specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass thereof,
              False otherwise.
    """
    return isinstance(obj, a_class)
