#!/usr/bin/python3

# function that deletes keys with a specific value in a dictionary

def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if value == a_dictionary[key]:
            del a_dictionary[key]
        elif value != a_dictionary[key]:
            pass
    return a_dictionary


# Input Data
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)