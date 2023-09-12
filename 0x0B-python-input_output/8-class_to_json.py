#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """A function that returns the dictionary description with
    simple data structure, for JSON serialization of an object."""
    return obj.__dict__
