#!/usr/bin/python3

"""Write a function that prints My name is <first name> <last name>"""

def say_my_name(first_name, last_name=""):
    """Print the first name and last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    # Input Data
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)