#!/usr/bin/python3
def magic_calculation(a, b):
    calc = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            calc += a ** b / n
        except Exception:
            calc = b + a
            break
        return calc
