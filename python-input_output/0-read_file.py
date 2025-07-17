#!/usr/bin/python3
"""
This module contains a function to read a text file and print its content.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
                        It is expected to be a valid file path.
    """
    # Use the 'with' statement to ensure the file is properly closed
    # 'r' mode is for reading, 'encoding='utf-8'' specifies the character encoding
    with open(filename, 'r', encoding='utf-8') as f:
        # Read the entire content of the file
        content = f.read()
        # Print the content to standard output
        print(content, end='') # Use end='' to prevent adding an extra newline
                               # since f.read() already includes newlines from the file

