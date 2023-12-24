#!/usr/bin/python3
""" this module we will Write a class Square that defines a square by :
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0) """


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
