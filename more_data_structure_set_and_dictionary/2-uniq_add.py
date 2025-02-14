#!/usr/bin/python3

# function that adds all unique integers in a list (only once for each integer)

def uniq_add(my_list=[]):
    my_set = set(my_list)
    return sum(my_set)
    # result = 0
    # for val in my_set:
    #     result += val
    # return result


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))