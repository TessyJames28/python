#!/usr/bin/python3

# Function that prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        dict_keys = a_dictionary.keys()
        sorted_dict = sorted(dict_keys)
        for val in sorted_dict:
            print(f"{val}: {a_dictionary[val]}")


# Avoid program execution during import
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)