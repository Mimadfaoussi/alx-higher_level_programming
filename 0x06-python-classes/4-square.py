#!/usr/bin/python3
""" module that will include getters and setters of a class"""


class Square:
    """ square class with attributes and methods """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ public instance method that return square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ will retrieve the size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ will set the size (setter)"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
