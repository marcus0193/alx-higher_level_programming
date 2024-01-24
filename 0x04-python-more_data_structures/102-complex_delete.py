#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.key()):
        if a_dictionary[key] == vlaue:
            del a_dictionary[key]
    return a_dictionary
