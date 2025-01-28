#!/usr/bin/python3


# function that replaces or adds key/value in a dictionary

def update_dictionary(a_dictionary, key, value):
    new_dict = {key: value}
    a_dictionary.update(new_dict)
    return a_dictionary


print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)