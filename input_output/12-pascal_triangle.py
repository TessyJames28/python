#!/usr/bin/python3

""" Create a function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n:
    """
    triangle = []
    prev_list = []
    if n <= 0:
        return []
    for val in range(n):
        val_list = []
        for i in range(val + 1):
            if i == 0:
                val_list.append(1)
            elif i == val:
                val_list.append(1)
            else:
                for index, num in enumerate(prev_list):
                    if index != len(prev_list):
                        result = num + (num + 1)
                        val_list.append(result)
            print(val_list)
            # triangle.append(val_list)
            prev_list = val_list

    # print(val_list)


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    pascal_triangle(5)
