#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class
that inherited (directly or indirectly) from a specified class.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj's class is a subclass of a_class (but not a_class itself),
              False otherwise.
    """
    # Check if obj is an instance of a subclass of a_class
    # and also ensure it's not exactly an instance of a_class itself.
    return isinstance(obj, a_class) and type(obj) is not a_class
