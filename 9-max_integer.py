#!/usr/bin/python3

# function that finds the biggest integer of a lis

def max_integer(my_list=[]):
    max = 0
    for val in my_list:
        if val > max:
            max = val
    return max


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))