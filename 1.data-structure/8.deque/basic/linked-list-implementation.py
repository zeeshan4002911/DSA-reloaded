"""
A Deque (Double-Ended Queue) is a data structure that allows adding and removing elements from both the front and rear ends.
Using a doubly linked list to implement a deque makes these operations very efficient, as each node in the list has pointers to both the previous and next nodes. This means we can insert and delete elements from both ends in constant time.
Operations on Deque

The following four basic operations are typically performed on a deque:

    insertFront(): Adds an item at the front of the deque.
    insertRear(): Adds an item at the rear of the deque.
    deleteFront(): Removes an item from the front of the deque.
    deleteRear(): Removes an item from the rear of the deque.

Additionally, the following operations are also supported:

    getFront(): Retrieves the front item from the deque.
    getRear(): Retrieves the last item from the deque.
    isEmpty(): Checks if the deque is empty.
    size(): Returns the number of elements in the deque.
    erase(): Removes all elements from the deque.
"""


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insert_front(self, val):
        new_node = Node(val)

        # Assigning the new node at the front of the head of linked list
        new_node.next = self.head
        # Linking the head node prev pointer to new node
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

        # If deque was empty then pointing the tail to newly added node as well
        if self.tail is None:
            self.tail = new_node

        self._size += 1
        return True

    def insert_rear(self, val):
        new_node = Node(val)

        # Linking the prev pointer of new node to tail for adding new node at the end
        new_node.prev = self.tail
        # Linking the tail node next pointer of linked list to new node
        if self.tail is not None:
            self.tail.next = new_node
        # Changing the tail to new node
        self.tail = new_node

        # If deque was empty then pointing the head to newly added node as well
        if self.head is None:
            self.head = new_node

        self._size += 1
        return True

    def delete_front(self):
        if self.head is None:
            print("Deque is empty")
            return

        # Cache data of element to be removed for result
        data = self.head.data
        curr = self.head
        # Moving the head to next node
        self.head = self.head.next
        # Breaking the link next of previous head and prev of current head
        curr.next = None
        if self.head is not None:
            self.head.prev = None
        # If the deque becomes empty after removal, update tail to None
        if self.head is None:
            self.tail = None

        self._size -= 1
        return data

    def delete_back(self):
        if self.tail is None:
            print("Deque is empty")
            return

        # Cache data of element to be removed for result
        data = self.tail.data
        curr = self.tail
        # Moving the tail to previous node
        self.tail = self.tail.prev
        # Breaking the link prev of previous tail and next of current tail
        curr.prev = None
        if self.tail is not None:
            self.tail.next = None
        # If the deque becomes empty after removal, update tail to None
        if self.tail is None:
            self.head = None

        self._size -= 1
        return data

    def get_front(self):
        if self.head is None:
            print("Deque is empty")
            return
        return self.head.data

    def get_back(self):
        if self.tail is None:
            print("Deque is empty")
            return
        return self.tail.data

    def is_empty(self):
        return self.head is None and self.tail is None and self._size == 0

    def size(self):
        return self._size

    def erase(self):
        self.head = None
        self.tail = None
        return True

    def pretty_print(self):
        if self.head is None:
            print("Deque is empty")
            return

        curr = self.head
        while curr.next is not None:
            print(curr.data, "<->", end=" ")
            curr = curr.next
        print(curr.data, end="")
        print()

    def get_list(self):
        arr = []
        curr = self.head
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next
        return arr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def info():
    print(
        """
        pf <val> : push element at front of deque
        ppf : pop element from the front of deque
        pb <val> : push element at back of deque
        ppb : pop element from the back of deque
        gf : get front element of deque
        gb : get back elemenet of deque
        empty : Check whether the deque is empty or not
        clear : Clear or erase deque's all elements
        size : Get the size of deque
        pprint : Pretty print the deque
        list : Get the deque in list format
        q : exit
        """
    )


def main():
    print("Started!! Type info for available operations")
    deque = Deque()

    while True:
        user_input = input().strip().split()[:2]
        if len(user_input) < 1:
            print("Enter a valid operation, type info for operation list")
            continue
        op = user_input[0]
        if op == "pf" and len(user_input) == 2:
            deque.insert_front(user_input[1])
        elif op == "pb" and len(user_input) == 2:
            deque.insert_rear(user_input[1])
        elif op == "ppf":
            print("Element Removed:", deque.delete_front())
        elif op == "ppb":
            print("Element Removed:", deque.delete_back())
        elif op == "gf":
            print("Front Element:", deque.get_front())
        elif op == "gb":
            print("Back Element:", deque.get_back())
        elif op == "empty":
            print(deque.is_empty())
        elif op == "clear":
            deque.erase()
        elif op == "size":
            print(deque.size())
        elif op == "pprint":
            deque.pretty_print()
        elif op == "list":
            print(deque.get_list())
        elif (op).lower() == "info":
            info()
        elif op == "q":
            break
        else:
            print("No valid operation provided, type info for valid operation list")


if __name__ == "__main__":
    main()
