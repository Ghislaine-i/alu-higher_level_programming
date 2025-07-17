#!/usr/bin/python3
"""
This module contains a function to write a string to a text file
and return the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The string content to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters successfully written to the file.
    """
    # Use the 'with' statement to ensure the file is properly closed.
    # 'w' mode is for writing. It creates the file if it doesn't exist
    # and overwrites its content if it already exists.
    # 'encoding='utf-8'' specifies the character encoding.
    with open(filename, 'w', encoding='utf-8') as f:
        # Write the entire string content to the file.
        # The write() method returns the number of characters written.
        num_characters_written = f.write(text)
    
    # Return the count of characters written.
    return num_characters_written
