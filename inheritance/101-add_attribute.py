#!/usr/bin/python3

"""Write a function that adds a new attribute to an object if it’s possible:
"""

def add_attribute(obj, name, value):
    """Add a new attribute"""
    # Check if the object has a __dict__ attribute to determine
    # whether it can have dynamically added attributes
    
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)


if __name__ == "__main__":
    # Input Data
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))