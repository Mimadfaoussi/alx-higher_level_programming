#!/usr/bin/python3
""" creating a  square class"""


class Square:
    """ a square class with size and position and area and print """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if (len(value) == 2):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of \
                        2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        height = 0
        if (self.__size == 0):
            print("")
        for y in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print("_", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
