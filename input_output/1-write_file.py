#!/usr/bin/python3

"""Write a function that writes a string to a text file (UTF8) and
returns the number of characters written:
"""

def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
    


# Input Data
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)