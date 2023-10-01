#!/usr/bin/python3

"""
0-pascal_triangle.py:

Defines the pascal_triangle function that returns
a list of lists of integers representing Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified n value.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        None.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        curr_row = [1]

        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
