#!/usr/bin/python3
""" coordinates of a square module """


class Square:
    """ a class square with attributes and methods """
    def __init__(self, size=0, position=(0, 0)):
        """ constructor of the square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter of the size attribute of square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of the size attribute of square class"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter of the position of the square class"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setter of the position of square class """
        if not isinstance(value, (int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ public instance method for getting the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ printing a square in a  specific position """
        margin = ''
        if (self.position[0] > 0):
            i = 0
            while (i < self.position[0]):
                margin = margin + ' '
                i += 1
        if (self.__size == 0):
            print("")
        else:
            i = 0
            while (i < self.__size):
                j = 0
                word = margin
                while (j < self.__size):
                    word = word + '#'
                    j += 1
                print(word)
                i += 1
