#!/usr/bin/python3
"""
Defines a class of Rectangle
"""


class Rectangle:
    """Rectangle repersentation"""
    def __init__(self, width=0, height=0):
        """Rectangle initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter of the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the retangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a printable rectangle's representation"""
        string = ""
        if self.__width != 0 and self.__heigth != 0:
            string += "\n".join("#" * self.width
                                for j in range(self.__heigth))
        return string
