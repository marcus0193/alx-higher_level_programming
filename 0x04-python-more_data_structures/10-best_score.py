#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    hinum = 0
    hivar = None
    for n, val in a_dictionary.items():
        if val > hinum:
            hinum = val
            hivar = n
    return hivar
