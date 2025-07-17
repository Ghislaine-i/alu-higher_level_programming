#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation of an object.
"""
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    # Use json.dumps() to convert the Python object into a JSON formatted string.
    # This function handles various Python data types and converts them
    # to their corresponding JSON types.
    return json.dumps(my_obj)

