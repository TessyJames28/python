#!/usr/bin/python3

# Technical Interview preparation
# function def roman_to_int(roman_string): that converts a Roman numeral to an integer

def roman_to_int(roman_string):
    roman = [{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }]


    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    prev = 0
    value = 0
    for chr in roman_string[::-1]:
        for val in roman:
            if prev > val[chr]:
                value -= 1
            else:
                value += val[chr]
            prev = val[chr]
    return value


# Input
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))