#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    # If n is less than or equal to 0, return an empty list as per requirements.
    if n <= 0:
        return []

    # Initialize the triangle with the first row.
    # The first row of Pascal's triangle is always [1].
    triangle = [[1]]

    # Loop from the second row up to the n-th row.
    # We already have the first row, so we start from row_num = 1 (second row).
    while len(triangle) < n:
        # Get the last row added to the triangle. This will be used to build the next row.
        last_row = triangle[-1]
        # Initialize the new row. It always starts with 1.
        new_row = [1]

        # Calculate the middle elements of the new row.
        # Each element is the sum of the two elements directly above it in the last_row.
        # We iterate from the second element (index 1) up to the second-to-last element
        # of the last_row.
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i+1])

        # The new row always ends with 1.
        new_row.append(1)

        # Add the newly generated row to the triangle.
        triangle.append(new_row)

    # Return the complete Pascal's triangle.
    return triangle

