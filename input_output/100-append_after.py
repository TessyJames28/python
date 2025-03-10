#!/usr/bin/python3

"""Write a function that inserts a line of text to a file, after each line containing a 
specific string (see example):
"""

def append_after(filename="", search_string="", new_string=""):
    """Append a line after a string in a file"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if search_string in line:
                lines.insert(lines.index(line) + 1, new_string)
        file.seek(0)
        file.writelines(lines)


# Input Data
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")