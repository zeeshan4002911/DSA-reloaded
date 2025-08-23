# Linked list implementation of python with basic operation using class and methods

class LinkedList:
    def __init__(self):
        self.head = None

    # Create new linked list with a list based data
    def append_all(self, lst):
        size = len(lst)
        if size < 1:
            return

        node = Node(lst[0])
        self.head = node
        prev_node = node

        for i in range(1, size):
            node = Node(lst[i])
            prev_node.next = node
            prev_node = node

        return self.head

    # Print in pretty format
    def pretty_print(self, head=None):
        curr = head or self.head
        while curr is not None:
            print(curr.data, end="")
            if curr.next is not None:
                print(" -> ", end="")
            curr = curr.next

    # Return the list of the linked list
    def return_list(self, head=None):
        result = []
        curr = head or self.head

        while curr is not None:
            result.append(curr.data)
            curr = curr.next

        return result


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
