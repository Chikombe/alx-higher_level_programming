#!/usr/bin/python3
"""Defines a function to check class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        object (any): The object to check.
        a_class (type): The class to match the type of object to.

    Returns:
        True if the object is exactly an instance of the specified class
        Otherwise False.
    """
    if type(object) == a_class:
        return True
    return False
