#!/usr/bin/python3
'''Module for the BaseGeometry class.'''


class BaseGeometry:
    '''BaseGeometry class.'''
    def area(self):
        '''Method to compute an area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for value validation.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
