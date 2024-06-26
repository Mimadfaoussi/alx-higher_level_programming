#!/usr/bin/python3
""" Square that defines a square with attributes"""


class Square:
    """  Square class that defines a square with attributes"""
    def __init__(self, size=0):
        """ constructor for the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
