#!/usr/bin/python3
"""
This module provides a function to list attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings, where each string is the name of an attribute or method.
    """
    return dir(obj)
