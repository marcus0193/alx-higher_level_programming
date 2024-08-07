#!/usr/bin/python3
'''Module for Rectangle class.'''


class Rectangle:
    '''This class define a simple Rectangle.'''

    number_of_instances = 0
    '''int: The number of active instances.'''

    print_symbol = '#'
    '''type: Print symbol, can be any type.'''

    def __init__(self, width=0, height=0):
        '''Constructor.

        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        '''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Property for the width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property for the height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of this rectangle.'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns perimeter of this rectangle.'''
        if not self.__width or not self.__height:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''Returns string representation.'''
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __reper__(self):
        '''Returns formal string representation.'''
        return "Rectangle(" + str(self.width) + ", " + str(sel.height) + ")"
    
    def __del__(self):
        '''Called at instance deletion.'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
