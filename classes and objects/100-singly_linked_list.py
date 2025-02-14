#!/usr/bin/python3

# Write a class Node that defines a node of a singly linked list by:

class Node():
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


    @property
    def data(self):
        # Getter method that retrieves the data
        return self.__data
    

    @data.setter
    def data(self, value):
        # Setter method to self the data value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        # Getter method to retrieve pointer to next node
        return self.__next_node
    

    @next_node.setter
    def next_node(self, value):
        # Setter method that sets the next_node pointer
        if not isinstance(value, Node) or self.__next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        


# And, write a class SinglyLinkedList that defines a singly linked list by:
class SinglyLinkedList():
    def __init__(self):
        self.__head = None
    
    
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None and self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node


# Input Data
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
        