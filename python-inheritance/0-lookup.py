#!urs/bin/python3
"""Module that returns available attributes and methods."""

def lookup(obj):
    """return the list of attributes and methods of an object."""
    return dir(obj)
