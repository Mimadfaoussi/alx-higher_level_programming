#!/usr/bin/python3
"""writes a string to a text file (UTF8) ."""


def write_file(filename="", text=""):
    """ Writing a string to a UTF8 text file.

    Args:
        filename: the name of the file.
        text: the text to write into the file.
    Returns:
        THE NB OF CHARS written.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
