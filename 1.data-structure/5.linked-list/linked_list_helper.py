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

    # Add value into the end of linked list
    def append(self, data, head=None):
        curr = head or self.head
        node = Node(data)

        if curr is None:
            head = node
            self.head = node
            return head or self.head

        while curr.next is not None:
            curr = curr.next
        curr.next = node

        return head or self.head

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

    # Return the presencce boolean, works like in operator
    def has_value(self, value, head=None):
        curr = head or self.head

        while curr is not None:
            if curr.data == value:
                return True
            curr = curr.next

        return False

    # Insert value at any position of linked list,
    # pos is 1 base and on greater than length of linked list it throws out of range error
    def insert_at(self, head, pos, data):
        node = Node(data)

        # Insert at the beginning
        if pos == 1:
            node.next = head
            head = node
        else:
            # Insert in-between of linked list
            length = 0
            curr, prev = head, None
            while curr is not None:
                length += 1
                if length == pos:
                    prev.next = node
                    node.next = curr
                    break

                prev = curr
                curr = curr.next

            # Insert at the end of linked list
            if pos == length + 1:
                prev.next = node
            # Raise index error exception on position value greater than size of linked list
            else:
                raise IndexError("Value of pos is out of range")
            
        return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
