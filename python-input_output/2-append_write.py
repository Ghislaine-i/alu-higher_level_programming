#!/usr/bin/python3
"""
This module contains a function to append a string to a text file
and return the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns the
    number of characters added.

    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string.
        text (str): The string content to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters successfully added to the file.
    """
    # Use the 'with' statement to ensure the file is properly closed.
    # 'a' mode is for appending. It creates the file if it doesn't exist
    # and adds content to the end of the file if it already exists.
    # 'encoding='utf-8'' specifies the character encoding.
    with open(filename, 'a', encoding='utf-8') as f:
        # Write the string content to the end of the file.
        # The write() method returns the number of characters written.
        num_characters_added = f.write(text)
    
    # Return the count of characters added.
    return num_characters_added
