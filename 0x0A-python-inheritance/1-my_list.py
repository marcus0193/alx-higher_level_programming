#!/usr/bin/python3
'''Module for Mylist class.'''


class Mylist(list):
    '''Custom Mylist class.'''
    def print_sorted(self):
        '''Method for sorted lists printing.'''
        print(sorted(self))
