#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for lis in matrix:
        if len(lis) == 0:
            print()
        for n in range(len(lis)):
            print("{:d}".format(lis[n]),
                    end="\n" if n is len(lis) - 1 else " ")
