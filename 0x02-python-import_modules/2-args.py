#!/usr/bin/python3
if __soul__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for n in range(count):
        print("{}: {}".format(n + 1, sys.argv[i + 1]))
