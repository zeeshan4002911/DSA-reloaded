# Linked list implementation of python with basic operation using class and methods


class LinkedList:
    def __init__(self):
        self.head = None

    # Create new linked list with a list based data
    def append_all(self, lst, pos=None):
        size = len(lst)
        if size < 1:
            return
        if pos is not None and not isinstance(pos, int):
            return "Value of pos should be number"

        node = Node(lst[0])
        self.head = node
        prev_node = node
        node_ref = None

        # Taking reference of node for circular linked list
        if pos is not None and pos - 1 == 0:
            node_ref = node

        for i in range(1, size):
            node = Node(lst[i])

            # Taking reference of node for circular linked list
            if pos is not None and pos - 1 == i:
                node_ref = node

            prev_node.next = node
            prev_node = node

        # Pointing the tail node to node reference for circular linked list
        if pos is not None and node_ref is not None:
            prev_node.next = node_ref

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
    def pretty_print(self, head=None, pos=None):
        curr = head or self.head

        fast = None
        if pos is not None and isinstance(pos, int) and pos > 0:
            fast = head

        while curr is not None:
            print(curr.data, end="")
            if curr.next is not None:
                print(" -> ", end="")
            curr = curr.next

            if fast is not None:
                fast = fast.next.next
                if curr == fast:
                    break
        print()

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

    def remove_at(self, head, pos):
        curr = head

        if curr is None:
            return curr

        # For the first position (head removal)
        if pos == 1:
            head = head.next
            curr.next = None
        # For the rest of position
        else:
            count = 0
            prev = None
            while curr is not None:
                count += 1
                if count == pos:
                    prev.next = curr.next
                    curr.next = None
                    break

                prev = curr
                curr = curr.next

        return head

    # For clear the linked list or reset to initial state
    def clear_all(self, head=None):
        curr = head or self.head
        prev = None

        while curr is not None:
            if prev is not None:
                prev.data = None
                prev.next = None
            prev = curr
            curr = curr.next

        if prev is not None:
            prev.data = None
            prev.next = None

        if head is not None:
            head.data = None
            head.next = None
        if self.head is not None:
            self.head.data = None
            self.head.next = None
            self.head = None

        return True


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append_all(self, lst):
        if lst is None:
            return None

        head = DNode(lst[0])
        prev_node_ref = head

        size = len(lst)
        for i in range(1, size):
            node = DNode(lst[i])

            # Forward connect of node (prev node -> next to point curr node)
            prev_node_ref.next = node
            # Backward connect of node (curr node -> prev to point to prev node)
            node.prev = prev_node_ref
            # Cache of curr node to prev node ref
            prev_node_ref = node

        self.head = head
        return head

    def pretty_print(self, head=None):
        curr = head or self.head
        while curr.next is not None:
            print(curr.data, "<-> ", end="")
            curr = curr.next
        print(curr.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
