#!/usr/bin/python3

# function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
    

# Input
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)