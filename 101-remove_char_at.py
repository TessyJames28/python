#!/usr/bin/python3

def remove_char_at(str, n):
    new_string = ""
    for index, chr in enumerate(str):
        if index == n:
            continue
        new_string += chr
            
    return new_string


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))