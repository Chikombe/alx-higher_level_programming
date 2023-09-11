#!/usr/bin/python3
"""Defines a class and a function for checking inherited class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a_class.

    Args:
        object (any): The object to check
        a_class (type): The class to match the type of object to.
    Returns:
        True if the object is an instance or inherited instance of a_class.
        Otherwise False.
    """
    if isinstance(object, a_class):
        return True
    return False
