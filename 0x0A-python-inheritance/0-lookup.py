#!/usr/bin/python3
'''Module for the lookup Method.'''


def lookup(obj):
    '''Looks up attributes and methods of objects.

    Args:
        obj (objects): the listed objects.

    Returns:
        list: list of object's attributes.
    '''
    return dir(obj)
