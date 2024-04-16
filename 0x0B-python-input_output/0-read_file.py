#!/usr/bin/python3
"""Defines a text file-reading function."""
def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open('filename.txt', 'r', encoding="UTF-8") as file:
        content = file.read()
        print("{}".format(content), end="")
