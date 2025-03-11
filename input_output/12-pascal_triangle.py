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
            # elif val + 1 > 1 and i == val:
            #     val_list.append(1)
            else:
                for num in range(len(prev_list)):
                    if num != len(prev_list) - 1:
                        result = prev_list[num] + prev_list[num + 1]   
                        val_list.append(result)
                    elif num == len(prev_list) - 1:
                        val_list.append(1)
                break
    
        triangle.append(val_list)
        prev_list = val_list

    return triangle


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print(pascal_triangle(5))
