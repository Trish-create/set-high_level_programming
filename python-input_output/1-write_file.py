#!/usr/bin/python3
"""Module for writing text to a file."""

def write_file(filename="", text=""):
    """this writes a string to a UFT-8 text file and returns the number of charcters written."""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
