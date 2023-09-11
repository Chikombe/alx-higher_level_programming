#!/usr/bin/python3
"""Defines an inheritated list class MyList."""


class MyList():
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
