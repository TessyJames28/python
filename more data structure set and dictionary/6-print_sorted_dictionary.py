#!/usr/bin/python3

# Function that prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    dict_keys = a_dictionary.keys()
    sorted_dict = sorted(dict_keys)
    for val in sorted_dict:
        print(f"{val}: {a_dictionary[val]}")

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)