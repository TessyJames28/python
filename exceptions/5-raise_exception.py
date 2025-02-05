#!/usr/bin/python3

# Raise an exception

def raise_exception():
    raise TypeError


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")