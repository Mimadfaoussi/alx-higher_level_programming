#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """ append_write - appends a string at the end of a text file (UTF8) """
    with open(filename, 'a', encoding="UTF-8") as file:
        return file.write(text)
