#!/usr/bin/python3

# function that returns a set of common elements in two sets

def common_elements(set_1, set_2):
    new_set = set()
    for element in set_1:
        if element in set_2:
            new_set.add(element)
    return new_set


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))