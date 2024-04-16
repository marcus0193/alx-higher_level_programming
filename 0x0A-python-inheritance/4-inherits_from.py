#!/usr/bin/python3
'''module for inherits_from Method.'''


def inherits_from(obj, a_class):
    '''See if the object is a Subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) is not a_class
