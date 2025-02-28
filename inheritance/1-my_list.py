#!/usr/bin/python3

"""
Write a class MyList that inherits from list:
"""

class MyList(list):
    """Inheritance
    """

    def print_sorted(self):
        """Print sorted list of integers
        """
        print(sorted(self))


if __name__ == "__main__":
    # Test data
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)