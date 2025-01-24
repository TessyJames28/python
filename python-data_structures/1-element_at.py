#!/usr/bin/python3

# Function that retrieves an element from a list like in C

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    for index, num in enumerate(my_list):
        if index == idx:
            return num
        


my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))