#!/usr/bin/python3
"""Defines the Pascal's Triangle Function."""


def pascal_triangle(n):
    """A function that returns a list of lists of integers
    representing the Pascal’s triangle of n:"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for itr in range(1, len(tri)):
            temp.append(tri[itr] + tri[itr - 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
