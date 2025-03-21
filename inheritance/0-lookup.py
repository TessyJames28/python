#!/usr/bin/python3

"""function that returns the list of available attributes and methods of an object:
"""

def lookup(obj):
    """Returns the list of an objects available attributes and methods
    """
    return dir(obj)


# Test data
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))