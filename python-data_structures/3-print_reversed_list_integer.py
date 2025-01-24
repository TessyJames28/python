#!/usr/bin/python3

# Print a list of integers of a list in reverse order

def print_reversed_list_integer(my_list=[]):
    for num in my_list[::-1]:
        print(num)


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)