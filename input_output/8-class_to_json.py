#!/usr/bin/python3
# MyClass = __import__('8-my_class').MyClass
MyClass = __import__('8-my_class_2').MyClass

""" Write a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""

def class_to_json(obj):
    """ class to json"""
    return obj.__dict__


# First Test Data
# m = MyClass("John")
# m.number = 89
# print(type(m))
# print(m)

# mj = class_to_json(m)
# print(type(mj))
# print(mj)

# Second Test data
m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)