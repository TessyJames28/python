#!/usr/bin/python3

# Write a function that returns True if the object is an instance of,
# or if the object is an instance of a class that inherited from,
# the specified class ; otherwise False.

def is_kind_of_class(obj, a_class):
    """Return True if an instance of a class, else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False


# Test Data
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))