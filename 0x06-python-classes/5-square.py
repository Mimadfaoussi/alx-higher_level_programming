#!/usr/bin/python3
""" this module is about printing a square"""


class Square:
    """ square class with attributes setter and getter and methods"""
    def __init__(self, size=0):
        """ constructor for the Square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ getter of the square class that return the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter for the square class that set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ a class public instance method that retrieve the area """
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            i = 0
            while (i < self.__size):
                j = 0
                word = ''
                while (j < self.__size):
                    word = word + '#'
                    j += 1
                print(word)
                i += 1
