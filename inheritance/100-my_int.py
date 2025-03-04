#!/usr/bin/python3

"""Write a class MyInt that inherits from int:
"""

class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __eq__(self, value):
        """Return the opposite value, '!='"""
        return super().__ne__(value)
    
    def __ne__(self, value):
        """Return the opposite, '=='"""
        return super().__eq__(value)
    

if __name__ == "__main__":
    # Input Data
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)