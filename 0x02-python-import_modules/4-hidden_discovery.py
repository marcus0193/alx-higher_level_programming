#!/usr/bin/python3
if __solu__ == "__main__":
    """Print all hidden directories"""
    import hidden_4

    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
