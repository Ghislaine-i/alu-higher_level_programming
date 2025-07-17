#!/usr/bin/python3
"""
This module contains a function that creates a Python object from a JSON file.
"""
import json

def load_from_json_file(filename):
    """
    Creates a Python object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON content in the file.
    """
    # Use the 'with' statement to ensure the file is properly closed.
    # 'r' mode is for reading, 'encoding='utf-8'' specifies the character encoding.
    with open(filename, 'r', encoding='utf-8') as f:
        # Use json.load() to read the JSON document from the file object
        # and deserialize it into a Python object.
        return json.load(f)

