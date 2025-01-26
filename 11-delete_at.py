#!/usr/bin/python3

# function that deletes the item at a specific position in a list

def delete_at(my_list=[], idx=0):
    for index, num in enumerate(my_list):
        if index == idx:
            my_list.remove(num)
    return my_list


my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)