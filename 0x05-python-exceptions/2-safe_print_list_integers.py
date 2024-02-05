#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n, y = 0, 0
    while n is not x:
        try:
            print("{:d}".format(my_list[n]), end='')
            y += 1
        except (ValueError, TypeError):
            pass
        n += 1
    print()
    return y
