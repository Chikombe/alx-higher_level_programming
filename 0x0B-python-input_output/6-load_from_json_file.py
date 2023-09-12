#!/usr/bin/python3
"""Defines a funnction that creates an object from JSON file."""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”:"""
    with open(filename) as f:
        json.load(f)
