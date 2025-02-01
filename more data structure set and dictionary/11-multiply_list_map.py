#!/usr/bin/python3

# function that returns a list with all values multiplied by a number without using any loops

def multiply_list_map(my_list=[], number=0):
    multiply_list = map(lambda x: x * number, my_list)
    return list(multiply_list)


# Input Data
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
