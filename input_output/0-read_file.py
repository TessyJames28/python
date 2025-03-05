#!/usr/bin/python3

""" File reading """

def read_file(filename=""):
    """Reading file"""
    with open(filename, 'r') as file:
       content = file.read() 
    print(content)


# Input Data
read_file("my_file_0.txt")