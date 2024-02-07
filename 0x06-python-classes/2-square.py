#!/usr/bin/python3
"""module of square"""

class square:
    """definaton setp of square"""


    def __init__(self, size=0):
        """comments.

        arguments:
	    size: the length of the square side
        raises:
	    TypeError: type of the size
	    VlaueError: size equal or less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
