#!/usr/bin/python3

# function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    try:
        for index, val in enumerate(my_list):
            print(val, end="")
            if index + 1 == x:
                break
        print()
        return index + 1
    except IndexError:
        pass


# Input
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
            