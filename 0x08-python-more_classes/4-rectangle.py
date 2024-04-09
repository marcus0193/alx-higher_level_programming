#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """Rectangle representation"""
    def __init__(self, width=0, height=0):
        """Rectangle initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width sitter the private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """heigth private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height sitter of the private instance attrubite"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".joint("#" * self.__width
                                 for n in range(self.__height))
        return string

    def __reper__(self):
        """Instance return a string representation of the rectangle to be able to recreate a new"""
        return "Rectangle({:d}, {:d})".format(self.__width, sel.__height)
