#!/usr/bin/python3
""" a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification) """


class Square:
    """ a class Square that defines a square """
    def __init__(self, size):
        self.__size = size
