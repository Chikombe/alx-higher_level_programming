#!/usr/bin/python3
# 4-print_square.py
"""A function that prints a square with the character #."""


def print_square(size):
    """Print a square with the # character.

    Arguments:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for itr in range(size):
        [print("#", end="") for index in range(size)]
        print("")
