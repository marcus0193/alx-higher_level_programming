#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(sings, str):
        return 0
    amount = 0
    n = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in reversed(sings):
        n = romans[x]
        amount += n if amount < n * 5 else -n
    return amount
