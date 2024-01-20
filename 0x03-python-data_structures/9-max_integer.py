#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_new = my_list.copy()
    list_new.sort()
    return list_new[-1]
