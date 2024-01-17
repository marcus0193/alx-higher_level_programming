#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for i, c in enumerate(str):
        if i != n:
            nstr += c
    return nstr
