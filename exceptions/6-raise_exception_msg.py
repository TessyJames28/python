#!/usr/bin/python3

# function that raises a name exception with a message.

def raise_exception_msg(message=""):
    raise NameError(message)


try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)