#!/usr/bin/python3
"""Defines an object attribute look up function."""


def lookup(obj):
    """A function that returns the list of available attributes
    and methods of an object"""
    return (dir(obj))
