#!/usr/bin/python3

# function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    new_list = []
    for val in my_list:
        if val == search:
            new_list.append(replace)
        else:
            new_list.append(val)
    return new_list


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)