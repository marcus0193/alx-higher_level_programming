#!/usr/bin/python3
"""square class defination"""


class square:
    """square repernat"""

    def __init__(self, size=0, position=(0, 0)):
        """square initialzation.

	arguments:
		size (int): the length of the square side
		position (int, int): the new square positions
        """
        self.size = size
        self,position = position

    @property
    def size(self):
        """ Geting and setting the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(vlaue, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Getting and setting the square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the area of square

	Returns:
		the area of square
	"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square display like #s. """
        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for x in range(0, self.__size)]
            print("")
