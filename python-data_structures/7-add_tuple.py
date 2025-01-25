#!/usr/bin/python3

# Function that adds 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        tuple_a += (0,)

    if len(tuple_b) < 1:
        tuple_b = (0, 0)
    elif len(tuple_b) < 2:
        tuple_b += (0,)
    
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    new_tuple = (first, second)
    return new_tuple


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))