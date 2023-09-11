#!/usr/bin/python3
"""Defines a function for checking class inheritance."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj(any): The object to check.
        a_class(type): The class to match the the type of obj to.
    Returns:
        True if the object is an instance of a class that inherited.
        Otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
