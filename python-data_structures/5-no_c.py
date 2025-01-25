#!/usr/bin/python3

# Function that removes all characters c and C from a string
def no_c(my_string):
    new_string = ""
    for chr in my_string:
        if chr == "c" or chr =="C":
            continue
        new_string += chr
    return new_string



print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))