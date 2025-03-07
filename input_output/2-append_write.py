#!/usr/bin/python3

""" Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""

def append_write(filename="", text=""):
    """Append a string and returns the number of characters added"""
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)


# Input Data
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)