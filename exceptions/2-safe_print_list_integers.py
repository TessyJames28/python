#!/usr/bin/python3

# function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]), end="")
            count += 1
        except (ValueError, TypeError, NameError):
            continue
    print()
    return count
    

# Input Data
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
        