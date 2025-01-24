#!/usr/bin/python3

# Write a function that replaces an element in a list at a specific position without
# modifying the original list (like in C).

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return None
    for index, num in enumerate(my_list):
        if index == idx:
            new_list[index] = element
    return new_list


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)