#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    p_int = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        p_int = False
    return p_int
