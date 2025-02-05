#!/usr/bin/python3

# function that divides element by element 2 lists

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
            new_list.append(result)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        finally:
            pass
    
    
    return new_list


# Input
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)