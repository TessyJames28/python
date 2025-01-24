#!/usr/bin/python3

# Replaces an element of a list at a specific position (like in C)

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    
    for index, num in enumerate(my_list):
        if index == idx:
            my_list[index] = element
    return my_list
    

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)