#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" Write a script that adds all arguments to a Python list, and then save them to a file:
"""

def load_add_save():
    """
    load, add, save
    """
    filename = "add_item.json"
    with open(filename, 'a') as file:
        pass
    
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        try:
            my_list = load_from_json_file(filename)
        except:
            my_list = []
        my_list.append(sys.argv[i])
        save_to_json_file(my_list, filename)


load_add_save()
