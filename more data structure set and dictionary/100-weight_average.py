#!/usr/bin/python3

# function that returns the weighted average of all integers tuple (<score>, <weight>)

def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    
    score = 0
    result = 0
    weight = 0
    for tuple in my_list:
        score += tuple[0] * tuple[1]
        weight += tuple[1]
    result = score / weight
    return result


# Input
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))