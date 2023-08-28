#!/usr/bin/python3

def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().

    Arguments:
        value (int): The integer to print.

    Returns:
        True if value has been correctly printed
        Otherwise, returns False"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
