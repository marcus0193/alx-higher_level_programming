#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass to represent a rectangle.'''
    def __init__(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("hieght", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that return the area of a rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''Method to represent a string.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
