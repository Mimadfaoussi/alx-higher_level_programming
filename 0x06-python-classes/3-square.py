#!/usr/bin/python3
""" Area of a square"""


class Square:
    """ square class with size as a private attribute """
    def __init__(self, size=0):
        """ constructor of Square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ an instance method that return the current square area"""
        return (self.__size * self.__size)
