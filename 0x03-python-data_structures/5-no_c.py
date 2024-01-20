#!/usr/bin/python3
def no_c(my_string):
    st = ""
    for n in range(len(my_string)):
        if (my_string[n] != 'c' and my_string[n] != 'C'):
            st += my_string[n]
    return st
