#!/usr/bin/python3

# function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return None
    for k in a_dictionary.keys():
        if a_dictionary[k] > max:
            max = a_dictionary[k]

    return next((k for k, v in a_dictionary.items() if v == max), None)


# Input
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))