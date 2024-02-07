#!/usr/bin/python3
"""module of square"""


class square:
    """definaton setp of square"""

    def __init__(self, size=0):
        """comments.

	arguments:
		size: the length of the square.
	"""
        self.size = size

    @property
    def size(self):
        """property length of the square side

	raises:
		TypeError: type of the size
		VlaueError: size equal or less than 0
	"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(vlaue, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """the area of square

	Returns:
		the size of square
	"""
        return self.__size ** 2

    def my_print(self):
        """print the square. """
        for n in range(self.size):
            for y in range(self.size):
                print("#", end="\n" if y is self.size - 1 and n != y else "")
        print()
