#!/usr/bin/python3
import sys

# function that prints an integer.

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print(f"Exeption: {e}", file=sys.stderr)
        return False


# Input Data
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))