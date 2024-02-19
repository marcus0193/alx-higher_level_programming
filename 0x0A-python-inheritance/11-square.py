#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Subclass to represent a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method to represent the area of a square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns representation of the square on string.'''
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
